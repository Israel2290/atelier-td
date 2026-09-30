#!/usr/bin/env python3
"""Generate faithful Markdown exam sources and browser data from local originals."""
from __future__ import annotations
import json, re, subprocess, zipfile, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'content' / 'epreuves'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# Stable IDs; source filenames and the source documents themselves are preserved.
EXAMS = [
 ('EP-001','ÉPREUVE DE SPÉCIALITÉ LUNDI.docx','Épreuve de spécialité SIL — Lundi','Spécialité SIL','Lundi'),
 ('EP-002','Epreuve_Specialite_SIL_MARDI.docx','Épreuve de spécialité SIL — Mardi','Spécialité SIL','Mardi'),
 ('EP-003','Epreuve_Specialite_SIL_MERCREDI.docx','Épreuve de spécialité SIL — Mercredi','Spécialité SIL','Mercredi'),
 ('EP-004','EPREUVE_DE_SPECIALITE_jeudi.pdf','Épreuve de spécialité SIL — Jeudi','Spécialité SIL','Jeudi'),
 ('EP-005','EPREUVE_DE_SPECIALITE_SIL_Mercredi.pdf','Épreuve de spécialité SIL — Mercredi (PDF)','Spécialité SIL','Mercredi'),
 ('EP-006','Tronc_Commun_LUNDI.docx','Épreuve de tronc commun — Lundi','Tronc commun','Lundi'),
 ('EP-007','Tronc_Commun_b.docx','Épreuve de tronc commun — Version b','Tronc commun','Version b'),
 ('EP-008','Tronc_Commun_MARDI.docx','Épreuve de tronc commun — Mardi','Tronc commun','Mardi'),
 ('EP-009','Tronc_Commun_MERCREDI.docx','Épreuve de tronc commun — Mercredi','Tronc commun','Mercredi'),
 ('EP-010','Tronc_Commun_JEUDI.docx','Épreuve de tronc commun — Jeudi','Tronc commun','Jeudi'),
 ('EP-011','Tronc_Commun_VENDREDI.docx','Épreuve de tronc commun — Vendredi','Tronc commun','Vendredi'),
 ('EP-012','APPLICATION1.pdf','Application 1 — Adressage IPv4 /24','Réseaux','Non précisée'),
 ('EP-013','APPLICATION 2.pdf','Application 2 — Adressage IPv4 /27','Réseaux','Non précisée'),
 ('EP-014','APPLICATION3.pdf','Application 3 — Adressage IPv4 /29','Réseaux','Non précisée'),
 ('EP-015','QCM_Subnetting_EXERCICE .pdf','QCM de sous-réseautage IPv4','Réseaux','Non précisée'),
]
DUPLICATES = {'EP-007':'EP-006'}
SOURCE_LIMITATIONS = {
 'EP-007':'Cette variante est proche du sujet du lundi ; les différences exactes de formulation et de numérotation restent à vérifier.',
 'EP-010':'La dernière consigne est tronquée après « applique une remise de » ; le taux manque dans la source.',
}

def node_questions():
    code = r"""
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(process.argv[1],'utf8');
const inline=html.match(/<script>([\s\S]*?)<\/script>/);
if(!inline) throw new Error('Inline question bank not found');
const src=inline[1], start=src.indexOf('const documents = ['), marker='questions.splice(0, 24);', end=src.indexOf(marker,start);
if(start<0||end<0) throw new Error('Could not locate question bank boundaries');
const context={}; vm.createContext(context);
process.stdout.write(vm.runInContext(src.slice(start,end+marker.length)+'\nJSON.stringify(questions);',context));
"""
    return json.loads(subprocess.run(['node','-e',code,str(ROOT/'atelier-epreuves.html')],check=True,capture_output=True,text=True).stdout)

def node_templates():
    code="const fs=require('fs'),vm=require('vm'),c={window:{}};vm.createContext(c);vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),c);process.stdout.write(JSON.stringify(c.window.ATELIER_TEMPLATES));"
    return json.loads(subprocess.run(['node','-e',code,str(ROOT/'templates-data.js')],check=True,capture_output=True,text=True).stdout)

def para_text(node):
    out=[]
    for item in node.iter():
        if item.tag == W+'t': out.append(item.text or '')
        elif item.tag == W+'tab': out.append('\t')
        elif item.tag in (W+'br',W+'cr'): out.append('  \n')
    return ''.join(out).strip()

def md_cell(text): return text.replace('|','\\|').replace('\n','<br>')

def word_table(table):
    rows=[]
    for row in table.findall(W+'tr'):
        cells=[]
        for cell in row.findall(W+'tc'):
            value='<br>'.join(filter(None,(para_text(p) for p in cell.findall('.//'+W+'p'))))
            cells.append(md_cell(value))
        if cells: rows.append(cells)
    if not rows: return ''
    width=max(len(r) for r in rows); rows=[r+['']*(width-len(r)) for r in rows]
    return '\n'.join(['| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*width)+' |']+['| '+' | '.join(r)+' |' for r in rows[1:]])

def word_markdown(path):
    with zipfile.ZipFile(path) as doc: root=ET.fromstring(doc.read('word/document.xml'))
    body=root.find('.//'+W+'body'); blocks=[]
    for child in list(body):
        if child.tag==W+'p':
            text=para_text(child)
            if not text: continue
            if re.match(r'^(DOSSIER|Dossier)\s+\d+',text,re.I): blocks.append('# '+text)
            elif re.match(r'^Question\s+\d+',text,re.I): blocks.append('## '+text)
            elif re.match(r'^(Travail demandé|Consignes générales|Annexes?)\b',text,re.I): blocks.append('## '+text.rstrip(':'))
            elif re.match(r'^ÉPREUVE\b',text,re.I): blocks.append('# '+text)
            else: blocks.append(text.replace('\n','  \n'))
        elif child.tag==W+'tbl':
            table=word_table(child)
            if table: blocks.append(table)
    return '\n\n'.join(blocks)

def pdf_markdown(path):
    info=subprocess.run(['pdfinfo',str(path)],check=True,capture_output=True,text=True).stdout
    page_count=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1)); pages=[]
    for n in range(1,page_count+1):
        page=subprocess.run(['pdftotext','-layout','-enc','UTF-8','-f',str(n),'-l',str(n),str(path),'-'],check=True,capture_output=True,text=True).stdout.strip('\n')
        if page.strip(): pages.append(f'## Page {n}\n\n{page}')
    return '\n\n---\n\n'.join(pages),page_count

def answer_letter(question):
    opts,correct=question.get('options'),question.get('correct')
    if isinstance(opts,list) and isinstance(correct,int) and 0<=correct<len(opts): return f'{chr(65+correct)}. {opts[correct]}'
    return ''

def correction_entries(exam, bank, templates):
    source='Tronc_Commun_LUNDI.docx' if exam['id']=='EP-007' else exam['source']
    matches=[q for q in bank if q.get('source')==source]
    result=[]; counters={}
    for q in matches:
        linked=[t for t in templates if q.get('id') in t.get('examIds',[])]
        section=q.get('section','Question'); subject=q.get('subject','')
        key=(subject,section); counters[key]=counters.get(key,0)+1
        prompt=q.get('prompt',''); scored=re.search(r'\b(\d+(?:[.,]\d+)?)\s*(?:pts?|points?)\b',prompt,re.I)
        result.append({'id':q.get('id'),'section':section,'subject':subject,'questionNumber':counters[key],'points':scored.group(1) if scored else None,'prompt':prompt,'type':q.get('type','written'),'answer':answer_letter(q),'model':q.get('model',''),'explanation':q.get('explanation',''),'templateIds':[t['id'] for t in linked],'templateTitles':[t['title'] for t in linked]})
    return result

def correction_md(exam, entries):
    out=[f"# Corrigé type — {exam['title']}",f"\n- Identifiant : {exam['id']}",f"- Statut de vérification : {exam['correction_status']}","\n> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir."]
    for n,item in enumerate(entries,1):
        points=re.search(r'\((\d+(?:[.,]\d+)?)\s*(?:pts?|points?)\)',item['prompt'],re.I)
        score=f" — {points.group(1)} points" if points else ''
        out += [f"\n## {item['subject']} — question {item['questionNumber']} — {item['section']}{score}",f"\n### Énoncé / tâche associée\n{item['prompt']}"]
        minimum=item['answer'] or item['model'].split('. ',1)[0].strip()
        if minimum: out.append(f"\n### Niveau 1 — réponse minimale\n{minimum}")
        if item['model']:
            model=item['model'].strip()
            if '\n' in model or model.startswith(('SELECT','CREATE TABLE','class ','public class')):
                lang='sql' if 'SELECT' in model or 'CREATE TABLE' in model else 'java'
                out.append(f"\n### Niveau 2 — réponse complète / solution type\n```{lang}\n{model}\n```")
            else: out.append(f"\n### Niveau 2 — réponse complète / solution type\n{model}")
        if item['explanation']:
            out.append(f"\n### Niveau 3 — explication pédagogique\n{item['explanation']}")
            out.append("\n### Méthode\nRepérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.")
        out.append("\n### Points à retenir\nRespecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.")
        if item['templateTitles']: out.append('\n### Templates associés\n'+'\n'.join(f"- {title}" for title in item['templateTitles']))
    return '\n'.join(out).rstrip()+'\n'

def grading_note(source_text):
    dossiers=re.findall(r'(?im)^\s*DOSSIER\s+(\d+)[^\n]{0,120}?\((\d+(?:[.,]\d+)?)\s*points?\)',source_text)
    if dossiers:
        detail=', '.join(f'Dossier {number} : {score} points' for number,score in dossiers)
        return f'Barème indiqué par dossier : {detail}. Aucun total ajouté.'
    if re.search(r'\(\s*\d+(?:[.,]\d+)?\s*(?:pts?|points?)\s*\)',source_text,re.I):
        return 'Barème par question/sous-question présent dans la source et conservé dans la transcription ; total global non précisé.'
    if re.search(r'\bBarème\s*:\s*\d+(?:[.,]\d+)?\s*(?:pts?|points?)',source_text,re.I):
        return 'Barème partiel mentionné dans la source ; répartition/total global non précisé.'
    return 'Non précisé dans le document original.'

def main():
    bank=node_questions(); templates=node_templates(); OUTPUT.mkdir(parents=True,exist_ok=True)
    ids={}; app=[]; rows=['# Inventaire des épreuves','','Année, durée, coefficient et barème sont notés « non précisé » lorsqu’ils ne sont pas indiqués par la source. Tous les PDF ont du texte extractible ; aucun média image intégré n’a été détecté dans les DOCX. Les statuts restent PARTIEL tant que la relecture humaine intégrale n’est pas terminée.','','| ID | Épreuve | Année | Matière | Source | Statut transcription | Statut corrigé |','| --- | --- | --- | --- | --- | --- | --- |']
    for stable_id,source,title,subject,session in EXAMS:
        if stable_id in ids: raise ValueError(f'Identifiant dupliqué: {stable_id}')
        ids[stable_id]=source; path=ROOT/source
        if not path.is_file(): raise FileNotFoundError(path)
        if path.suffix.lower()=='.pdf': transcription,pages=pdf_markdown(path)
        else: transcription,pages=word_markdown(path),None
        grading=grading_note(transcription)
        correction_status='⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.'
        if stable_id in ('EP-001','EP-002','EP-003'):
            correction_status='⚠️ PARTIEL — réponses regroupées par dossier ; vérification détaillée des sous-questions et du barème à effectuer.'
        elif stable_id=='EP-007':
            correction_status='⚠️ PARTIEL — variante proche du sujet EP-006 ; écarts de formulation et de numérotation à vérifier.'
        elif stable_id=='EP-010':
            correction_status='⚠️ PARTIEL — taux de remise absent de la source ; corrigé de cette sous-question incomplet.'
        exam={'id':stable_id,'source':source,'title':title,'subject':subject,'session':session,'year':None,'duration':None,'coefficient':None,'barème':grading,'transcription_status':'⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.','correction_status':correction_status,'source_limitation':SOURCE_LIMITATIONS.get(stable_id),'duplicate_of':DUPLICATES.get(stable_id)}
        folder=OUTPUT/stable_id; folder.mkdir(parents=True,exist_ok=True)
        source_page_count=f'{pages} pages PDF' if pages else 'DOCX'
        note=f"\n- Variante proche de {exam['duplicate_of']}." if exam['duplicate_of'] else ''
        header=f"# {title}\n\n## Informations générales\n\n- ID : {stable_id}\n- Année : Non précisée dans le document original.\n- Session : {session}\n- Matière : {subject}\n- Durée : Non précisée dans le document original.\n- Coefficient : Non précisé dans le document original.\n- Barème : {grading}\n- Source : `{source}` ({source_page_count}){note}\n- Statut de transcription : {exam['transcription_status']}\n\n---\n\n## Transcription fidèle\n\n> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.\n\n"
        (folder/'epreuve.md').write_text(header+transcription.strip()+'\n',encoding='utf-8')
        entries=correction_entries(exam,bank,templates)
        if stable_id!='EP-007' and not entries:
            correction_status='❌ TODO — aucune carte de réponse reliée à cette source.'
            exam['correction_status']=correction_status
        (folder/'corrige.md').write_text(correction_md(exam,entries),encoding='utf-8')
        meta={**exam,'source_url':'../../../'+source}
        (folder/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        rows.append(f"| {stable_id} | {title} | Non précisée | {subject} | `{source}` | {exam['transcription_status']} | {exam['correction_status']} |")
        app.append({**exam,'correctionStatus':exam['correction_status'],'transcriptionStatus':exam['transcription_status'],'sourceLimitation':exam['source_limitation'],'sourceUrl':source,'transcription':transcription,'corrections':entries})
    (OUTPUT/'index.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    (ROOT/'epreuves-data.js').write_text('window.ATELIER_EXAMS = '+json.dumps(app,ensure_ascii=False).replace('</','<\\/')+';\n',encoding='utf-8')
    print(f"Généré : {len(app)} épreuves, {sum(len(e['corrections']) for e in app)} fiches de correction, {OUTPUT.relative_to(ROOT)}")
    for exam in app: print(f"{exam['id']}\t{exam['source']}\tcorrections={len(exam['corrections'])}\t{exam['correction_status']}")

if __name__=='__main__': main()
