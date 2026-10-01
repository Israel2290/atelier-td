(() => {
  const exams = window.ATELIER_EXAMS || [];
  const courses = window.ATELIER_EXAM_COURSES || {};
  const templates = window.ATELIER_TEMPLATES || [];
  const layout = document.getElementById('appLayout');
  const listView = document.getElementById('correctedExamsView');
  const detailView = document.getElementById('examDetailView');
  const grid = document.getElementById('correctedExamGrid');
  const search = document.getElementById('correctedExamSearch');
  const subjectFilter = document.getElementById('correctedExamSubject');
  const statusFilter = document.getElementById('correctedExamStatus');
  const priority = { '✅ VALIDÉ': 0, '⚠️ PARTIEL': 1, '❌ TODO': 2, '🐛 À CORRIGER': 3 };
  let selectedExam = null;
  let currentMode = 'attempt';
  const normalizeText = value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('fr');

  function libraryProgress() { return progress.__examLibrary || {}; }
  function examProgress(examId) { return libraryProgress()[examId] || { revealed: [] }; }
  function saveExamProgress(examId, next) {
    progress.__examLibrary = { ...libraryProgress(), [examId]: next };
    saveProgress();
  }
  function setNavigation(view) {
    const corrected = view === 'corrected';
    layout.dataset.view = view;
    document.getElementById('examView').hidden = view !== 'exams';
    document.getElementById('templatesView').hidden = view !== 'templates';
    listView.hidden = !corrected || Boolean(selectedExam);
    detailView.hidden = !corrected || !selectedExam;
    document.querySelectorAll('[data-view-target]').forEach(button => {
      const active = button.dataset.viewTarget === view;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    if (corrected) selectedExam ? renderDetail() : renderList();
  }

  function mdInline(text) {
    return escapeHTML(text)
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  }

  function renderMarkdown(markdown) {
    const lines = String(markdown || '').replace(/\r/g, '').split('\n');
    const output = [];
    let paragraph = [];
    let list = null;
    const flushParagraph = () => {
      if (paragraph.length) output.push(`<p>${paragraph.map(mdInline).join('<br>')}</p>`);
      paragraph = [];
    };
    const flushList = () => {
      if (list) output.push(`</${list}>`);
      list = null;
    };
    for (let index = 0; index < lines.length; index++) {
      const line = lines[index];
      if (line.startsWith('```')) {
        flushParagraph(); flushList();
        const language = line.slice(3).trim();
        const code = [];
        index++;
        while (index < lines.length && !lines[index].startsWith('```')) code.push(lines[index++]);
        output.push(`<pre class="exam-markdown-code"><code>${escapeHTML(code.join('\n'))}</code><button type="button" data-copy-exam-code>Copier</button></pre>`);
        continue;
      }
      if (!line.trim()) { flushParagraph(); flushList(); continue; }
      if (/^\|.+\|$/.test(line) && index + 1 < lines.length && /^\|[\s:|-]+\|$/.test(lines[index + 1])) {
        flushParagraph(); flushList();
        const rows = [line]; index += 2;
        while (index < lines.length && /^\|.*\|$/.test(lines[index])) rows.push(lines[index++]);
        index--;
        const cells = rows.map(row => row.split('|').slice(1, -1).map(cell => cell.trim()));
        const head = cells.shift() || [];
        output.push(`<div class="exam-table-scroll"><table><thead><tr>${head.map(cell => `<th>${mdInline(cell)}</th>`).join('')}</tr></thead><tbody>${cells.map(row => `<tr>${row.map(cell => `<td>${mdInline(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`);
        continue;
      }
      const heading = line.match(/^(#{1,4})\s+(.+)$/);
      if (heading) { flushParagraph(); flushList(); const level = heading[1].length; output.push(`<h${level}>${mdInline(heading[2])}</h${level}>`); continue; }
      if (/^---+$/.test(line.trim())) { flushParagraph(); flushList(); output.push('<hr>'); continue; }
      const unordered = line.match(/^\s*[-*]\s+(.+)$/);
      const ordered = line.match(/^\s*\d+[.)]\s+(.+)$/);
      if (unordered || ordered) {
        flushParagraph(); const wanted = unordered ? 'ul' : 'ol';
        if (list !== wanted) { flushList(); list = wanted; output.push(`<${list}>`); }
        output.push(`<li>${mdInline((unordered || ordered)[1])}</li>`);
        continue;
      }
      const quote = line.match(/^>\s?(.*)$/);
      if (quote) { flushParagraph(); flushList(); output.push(`<blockquote>${mdInline(quote[1])}</blockquote>`); continue; }
      paragraph.push(line.trim());
    }
    flushParagraph(); flushList();
    return output.join('\n');
  }

  function statusLabel(value) {
    if (!value) return 'À commencer';
    if (value.includes('PARTIEL')) return 'Partiel';
    if (value.includes('TODO')) return 'À compléter';
    if (value.includes('VALIDÉ')) return 'Validé';
    return value;
  }

  function renderList() {
    const query = normalizeText(search.value).trim().split(/\s+/).filter(Boolean);
    const subject = subjectFilter.value;
    const status = statusFilter.value;
    const shown = exams.filter(exam => {
      const text = normalizeText([exam.id, exam.title, exam.subject, exam.session, exam.source, exam.transcription, ...(exam.corrections || []).flatMap(item => [item.prompt, item.model, item.explanation])].join(' '));
      return (!subject || exam.subject === subject)
        && (!status || (status === 'available' ? exam.corrections.length > 0 : status === 'partial' ? exam.correctionStatus.includes('PARTIEL') : exam.corrections.length === 0 || exam.correctionStatus.includes('TODO') || exam.correctionStatus.includes('À CORRIGER')))
        && query.every(term => text.includes(term));
    });
    document.getElementById('correctedExamCount').textContent = exams.length;
    document.getElementById('correctedExamResults').textContent = `${shown.length} épreuve${shown.length === 1 ? '' : 's'}`;
    grid.innerHTML = shown.length ? shown.map(exam => {
      const statusClass = exam.correctionStatus.includes('PARTIEL') ? 'partial' : 'validated';
      const availabilityLabel = exam.corrections.length ? 'Corrigé type disponible' : 'Corrigé à compléter';
      return `<article class="exam-library-card">
        <div class="question-meta"><span class="tag">${escapeHTML(exam.subject)}</span><span>${escapeHTML(exam.id)}</span><span class="question-number">${exam.corrections.length} questions liées</span></div>
        <h2>${escapeHTML(exam.title)}</h2>
        <p>${escapeHTML(exam.session)} · Année ${exam.year || 'non précisée'} · ${escapeHTML(exam.source)}</p>
        <p><span class="exam-status ${statusClass}">${availabilityLabel}</span><span class="exam-status-detail">${escapeHTML(statusLabel(exam.correctionStatus))} · ${escapeHTML(exam.correctionStatus)}</span></p>
        <div class="exam-card-actions"><button class="action-button" type="button" data-open-exam="${escapeHTML(exam.id)}">Voir l’épreuve</button><button class="text-action" type="button" data-open-correction="${escapeHTML(exam.id)}">Voir le corrigé</button></div>
      </article>`;
    }).join('') : '<div class="template-empty">Aucune épreuve ne correspond à la recherche.</div>';
    grid.querySelectorAll('[data-open-exam]').forEach(button => button.addEventListener('click', () => openExam(button.dataset.openExam, 'attempt')));
    grid.querySelectorAll('[data-open-correction]').forEach(button => button.addEventListener('click', () => openExam(button.dataset.openCorrection, 'correction')));
  }

  function renderCorrection(item, index) {
    const score = item.points ? ` · ${item.points} points` : '';
    const answer = item.answer ? `<p class="exam-answer"><strong>Réponse attendue :</strong> ${escapeHTML(item.answer)}</p>` : '';
    const model = item.model ? `<div class="exam-correction-model"><h4>Réponse type / solution</h4>${renderModel(item.model)}</div>` : '';
    const explanation = item.explanation ? `<div class="exam-correction-explanation"><h4>Explication</h4><p>${escapeHTML(item.explanation)}</p><h4>Méthode</h4><p>Repérer les éléments demandés, répondre dans le même ordre et contrôler le résultat avec les données de l’énoncé.</p><h4>À retenir</h4><p>Respecter les noms, unités, clés et contraintes du sujet.</p></div>` : '';
    const links = (item.templateIds || []).map(id => templates.find(template => template.id === id)).filter(Boolean);
    const templateButtons = links.length ? `<div class="exam-template-links"><span>Templates associés :</span>${links.map(template => `<button type="button" data-exam-template="${escapeHTML(template.id)}">${escapeHTML(template.title)}</button>`).join('')}</div>` : '';
    const title = `${item.subject ? `${escapeHTML(item.subject)} · ` : ''}Question ${item.questionNumber || index + 1} — ${escapeHTML(item.section || 'Question')}${score}`;
    return `<details class="exam-correction-item" data-correction-id="${escapeHTML(item.id || `correction-${index}`)}"><summary>${title}</summary><div class="exam-correction-body"><p class="exam-question-prompt">${escapeHTML(item.prompt)}</p>${answer}${model}${explanation}${templateButtons}</div></details>`;
  }

  function renderModel(model) {
    const text = String(model).trim();
    const looksLikeCode = text.includes('\n') || /^(SELECT|CREATE TABLE|INSERT INTO|UPDATE |DELETE FROM|class |public class|if\s*\(|public\s+\w+\s+\w+\s*\()/i.test(text);
    return looksLikeCode
      ? `<pre class="exam-markdown-code"><code>${escapeHTML(text)}</code><button type="button" data-copy-exam-code>Copier</button></pre>`
      : `<p>${escapeHTML(text)}</p>`;
  }

  function renderDetail() {
    if (!selectedExam) return;
    const exam = selectedExam;
    const saved = examProgress(exam.id);
    const mode = currentMode;
    const attemptMode = mode === 'attempt';
    const courseMode = mode === 'course';
    const showTranscription = attemptMode || mode === 'transcription';
    const showCorrections = attemptMode || mode === 'correction';
    const revealedCount = (saved.revealed || []).length;
    const percent = exam.corrections.length ? Math.round(revealedCount / exam.corrections.length * 100) : 0;
    detailView.innerHTML = `<button type="button" class="text-action exam-back" id="backToExamList">← Toutes les épreuves</button>
      <div class="intro exam-detail-intro"><div><div class="eyebrow">${escapeHTML(exam.id)} · ${escapeHTML(exam.subject)}</div><h1>${escapeHTML(exam.title)}</h1><p>${exam.sourceLimitation ? escapeHTML(exam.sourceLimitation) : escapeHTML(exam.correctionStatus)}</p></div><div class="session-mark"><strong>${exam.corrections.length}</strong>fiches de correction</div></div>
      <section class="exam-metadata" aria-label="Informations de l’épreuve"><div><span>Année</span><strong>${exam.year || 'Non précisée'}</strong></div><div><span>Session</span><strong>${escapeHTML(exam.session)}</strong></div><div><span>Durée</span><strong>${exam.duration || 'Non précisée'}</strong></div><div><span>Barème</span><strong>${escapeHTML(exam.barème || 'Non précisé')}</strong></div></section>
      <div class="exam-detail-toolbar"><button type="button" class="mode-button ${attemptMode ? 'selected' : ''}" data-exam-mode="attempt">Faire l’épreuve</button><button type="button" class="mode-button ${courseMode ? 'selected' : ''}" data-exam-mode="course">Cours</button><button type="button" class="mode-button ${mode === 'transcription' ? 'selected' : ''}" data-exam-mode="transcription">Transcription</button><button type="button" class="mode-button ${mode === 'correction' ? 'selected' : ''}" data-exam-mode="correction">Corrigé</button><a class="text-action" href="${escapeHTML(exam.sourceUrl)}" target="_blank" rel="noopener">PDF / DOCX original</a></div>
  <div class="exam-reveal-progress"><span>${revealedCount} corrigé${revealedCount === 1 ? '' : 's'} consulté${revealedCount === 1 ? '' : 's'}</span><div class="progress-track"><div class="progress-fill" style="width:${percent}%"></div></div><span>${percent} %</span></div>
      <section class="exam-transcription" ${showTranscription ? '' : 'hidden'}><h2>Énoncé original retranscrit</h2><div class="exam-markdown">${renderMarkdown(exam.transcription)}</div></section>
      <section class="exam-transcription" ${courseMode ? '' : 'hidden'}><h2>Cours nécessaire pour cette épreuve</h2><div class="exam-markdown">${renderMarkdown((courses[exam.id] || 'Cours non disponible pour cette épreuve.').replace(/^# Cours\s*/i, ''))}</div></section>
      <section class="exam-correction-section" ${showCorrections ? '' : 'hidden'}><h2>${attemptMode ? 'Corrigé progressif' : 'Corrigé type'}</h2><p class="written-hint">${attemptMode ? 'Essaie d’abord chaque question, puis ouvre uniquement le corrigé voulu.' : 'Ouvre les questions une à une pour consulter les réponses et explications.'}</p>${exam.correctionStatus.includes('PARTIEL') ? `<div class="feedback wrong"><strong>Corrigé partiel — vérification restante</strong>${escapeHTML(exam.correctionStatus)}</div>` : ''}<div class="exam-correction-list">${exam.corrections.map(renderCorrection).join('')}</div></section>`;
    detailView.querySelector('#backToExamList').addEventListener('click', () => { selectedExam = null; detailView.hidden = true; listView.hidden = false; renderList(); });
    detailView.querySelectorAll('[data-exam-mode]').forEach(button => button.addEventListener('click', () => {
      currentMode = button.dataset.examMode;
      saveExamProgress(exam.id, { ...examProgress(exam.id), mode: currentMode });
      renderDetail();
    }));
    detailView.querySelectorAll('[data-correction-id]').forEach(item => item.addEventListener('toggle', () => {
      if (!item.open) return;
      const state = examProgress(exam.id);
      const revealed = new Set(state.revealed || []);
      revealed.add(item.dataset.correctionId);
      saveExamProgress(exam.id, { ...state, started: true, revealed: [...revealed] });
      updateRevealProgress(exam);
    }));
    detailView.querySelectorAll('[data-exam-template]').forEach(button => button.addEventListener('click', () => openTemplate(button.dataset.examTemplate)));
    attachCodeCopy(detailView);
  }

  function updateRevealProgress(exam) {
    const state = examProgress(exam.id);
    const count = (state.revealed || []).length;
    const percent = exam.corrections.length ? Math.round(count / exam.corrections.length * 100) : 0;
    const bar = detailView.querySelector('.exam-reveal-progress .progress-fill');
    if (bar) bar.style.width = `${percent}%`;
    const labels = detailView.querySelectorAll('.exam-reveal-progress span');
    if (labels.length) labels[0].textContent = `${count} corrigé${count === 1 ? '' : 's'} consulté${count === 1 ? '' : 's'}`;
    if (labels.length > 1) labels[1].textContent = `${percent} %`;
  }

  function attachCodeCopy(container) {
    container.querySelectorAll('[data-copy-exam-code]').forEach(button => button.addEventListener('click', async () => {
      const code = button.parentElement.querySelector('code');
      if (!code) return;
      try {
        if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(code.textContent);
        else {
          const area = document.createElement('textarea'); area.value = code.textContent; area.style.position = 'fixed'; area.style.opacity = '0'; document.body.appendChild(area); area.select();
          const copied = document.execCommand('copy'); area.remove(); if (!copied) throw new Error('copy failed');
        }
        button.textContent = 'Copié !'; window.setTimeout(() => { if (button.isConnected) button.textContent = 'Copier'; }, 1500);
      } catch { button.textContent = 'Copie indisponible'; window.setTimeout(() => { if (button.isConnected) button.textContent = 'Copier'; }, 1800); }
    }));
  }

  function openTemplate(templateId) {
    const template = templates.find(item => item.id === templateId);
    if (!template) return;
    const nav = document.querySelector('[data-view-target="templates"]');
    nav.click();
    document.getElementById('templateSearch').value = template.title;
    document.getElementById('templateLanguage').value = template.language;
    document.getElementById('templateCategory').value = '';
    document.getElementById('templateType').value = '';
    document.getElementById('templateState').value = '';
    document.getElementById('templateSearch').dispatchEvent(new Event('input', { bubbles: true }));
  }

  function openExam(examId, mode='attempt', questionId='') {
    selectedExam = exams.find(exam => exam.id === examId);
    if (!selectedExam) return;
    currentMode = mode;
    saveExamProgress(examId, { ...examProgress(examId), started: mode === 'attempt' || examProgress(examId).started, mode });
    listView.hidden = true; detailView.hidden = false;
    renderDetail();
    if (questionId) {
      const target = detailView.querySelector(`[data-correction-id="${CSS.escape(questionId)}"]`);
      if (target) {
        target.open = true;
        target.scrollIntoView({ block: 'center' });
      }
    }
  }

  function renderGlobalSearch() {
    const input = document.getElementById('globalSearch');
    const panel = document.getElementById('globalSearchResults');
    const terms = normalizeText(input.value).trim().split(/\s+/).filter(Boolean);
    if (!terms.length) { panel.hidden = true; panel.innerHTML = ''; return; }
    const matches = text => {
      const normalized = normalizeText(text);
      return terms.every(term => normalized.includes(term));
    };
    const templateMatches = templates.filter(template => matches([
      template.title, template.language, template.category, template.type, template.description,
      template.syntax, template.example, template.exercise, ...(template.tags || []),
      ...(template.remember || []), ...(template.pitfalls || [])
    ].join(' '))).slice(0, 8);
    const examMatches = [];
    exams.forEach(exam => {
      const hits = (exam.corrections || []).filter(item => matches([item.prompt, item.answer, item.model, item.explanation, ...(item.templateIds || []).map(id => templates.find(template => template.id === id)?.title || '')].join(' ')));
      if (hits.length) hits.slice(0, 3).forEach(item => examMatches.push({exam, item}));
      else if (matches([exam.id, exam.title, exam.subject, exam.session, exam.source, exam.transcription].join(' '))) examMatches.push({exam, item: null});
    });
    const sections = [];
    if (templateMatches.length) sections.push(`<section><h2>Templates</h2>${templateMatches.map(template => `<button type="button" role="option" data-global-template="${escapeHTML(template.id)}"><strong>${escapeHTML(template.title)}</strong><span>${escapeHTML(template.language)} · ${escapeHTML(template.category)}</span></button>`).join('')}</section>`);
    if (examMatches.length) sections.push(`<section><h2>Épreuves et corrigés</h2>${examMatches.slice(0, 10).map(({exam,item}) => `<button type="button" role="option" data-global-exam="${escapeHTML(exam.id)}" data-global-question="${escapeHTML(item?.id || '')}"><strong>${escapeHTML(exam.title)}${item ? ` — ${escapeHTML(item.section)}` : ''}</strong><span>${escapeHTML(exam.id)}${item ? ` · ${escapeHTML(item.prompt)}` : ` · ${escapeHTML(exam.subject)}`}</span></button>`).join('')}</section>`);
    panel.innerHTML = sections.length ? sections.join('') : '<div class="template-empty">Aucun résultat.</div>';
    panel.hidden = false;
    panel.querySelectorAll('[data-global-template]').forEach(button => button.addEventListener('click', () => {
      const template = templates.find(item => item.id === button.dataset.globalTemplate);
      document.querySelector('[data-view-target="templates"]').click();
      document.getElementById('templateSearch').value = template?.title || '';
      document.getElementById('templateLanguage').value = template?.language || '';
      document.getElementById('templateCategory').value = '';
      document.getElementById('templateType').value = '';
      document.getElementById('templateState').value = '';
      document.getElementById('templateSearch').dispatchEvent(new Event('input', {bubbles:true}));
      panel.hidden = true;
    }));
    panel.querySelectorAll('[data-global-exam]').forEach(button => button.addEventListener('click', () => {
      document.querySelector('[data-view-target="corrected"]').click();
      openExam(button.dataset.globalExam, button.dataset.globalQuestion ? 'correction' : 'attempt', button.dataset.globalQuestion);
      panel.hidden = true;
    }));
  }

  function populateSubjects() {
    const subjects = [...new Set(exams.map(exam => exam.subject))].sort((a,b)=>a.localeCompare(b,'fr'));
    subjectFilter.innerHTML = '<option value="">Toutes les matières</option>' + subjects.map(item=>`<option>${escapeHTML(item)}</option>`).join('');
  }

  populateSubjects();
  document.getElementById('globalSearch').addEventListener('input', renderGlobalSearch);
  document.getElementById('globalSearch').addEventListener('keydown', event => { if (event.key === 'Escape') event.currentTarget.blur(), document.getElementById('globalSearchResults').hidden = true; });
  document.addEventListener('click', event => {
    if (!event.target.closest('.global-search-wrap')) document.getElementById('globalSearchResults').hidden = true;
  });
  search.addEventListener('input', renderList);
  subjectFilter.addEventListener('change', renderList);
  statusFilter.addEventListener('change', renderList);
  document.querySelector('[data-view-target="corrected"]').addEventListener('click', () => setNavigation('corrected'));
  document.querySelectorAll('[data-view-target="exams"], [data-view-target="templates"]').forEach(button => button.addEventListener('click', () => {
    selectedExam = null;
    listView.hidden = true;
    detailView.hidden = true;
  }));
  renderList();
  window.ATELIER_OPEN_EXAM = openExam;
})();
