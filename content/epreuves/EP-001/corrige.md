# Corrigé type — Épreuve de spécialité SIL — Lundi

- Identifiant : EP-001
- Statut de vérification : ⚠️ PARTIEL — réponses regroupées par dossier ; vérification détaillée des sous-questions et du barème à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Bases de données — question 1 — Spécialité · lundi · dossier 1

### Énoncé / tâche associée
Schéma ETUDIANT(IdEtudiant, Nom, Prenom, DateNaissance), FORMATION(IdFormation, Libelle, Niveau), INSCRIPTION(IdInscription, DateInscription, IdEtudiant, IdFormation). Réponds aux 6 demandes : différence PK/FK et exemple ; identifie PK/FK ; liste nom/prénom des étudiants ; étudiants inscrits à IdFormation=3 ; nom, prénom, formation, date d’inscription avec jointures ; effectif par formation.

### Niveau 1 — réponse minimale
PK identifie une ligne ; FK référence une PK

### Niveau 2 — réponse complète / solution type
PK identifie une ligne ; FK référence une PK. PK : les Id de chaque table. FK : INSCRIPTION.IdEtudiant→ETUDIANT et IdFormation→FORMATION. SELECT Nom,Prenom FROM ETUDIANT; pour formation 3 : SELECT e.Nom,e.Prenom FROM ETUDIANT e JOIN INSCRIPTION i ON i.IdEtudiant=e.IdEtudiant WHERE i.IdFormation=3; détails : joindre ETUDIANT, INSCRIPTION et FORMATION. Effectifs : SELECT f.Libelle,COUNT(i.IdInscription) FROM FORMATION f LEFT JOIN INSCRIPTION i ON i.IdFormation=f.IdFormation GROUP BY f.IdFormation,f.Libelle;

### Niveau 3 — explication pédagogique
Le LEFT JOIN conserve les formations sans inscription et COUNT(IdInscription) leur donne zéro.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Lire des données avec SELECT
- Relier des tables avec INNER JOIN
- Conserver toutes les lignes avec LEFT JOIN
- Compter par groupe avec GROUP BY
- Déclarer clés primaires et étrangères
- Repérer PK, FK et table mère/fille

## UML — question 1 — Spécialité · lundi · dossier 2

### Énoncé / tâche associée
Plateforme : étudiants consultent cours et passent évaluations ; étudiants/cours sont plusieurs-à-plusieurs ; un cours a plusieurs évaluations ; un étudiant obtient une note par évaluation. Identifie acteurs, 6 cas d’utilisation et relations, classes, ≥3 attributs typés par Etudiant/Cours/Evaluation, associations/cardinalités, puis spécifie le diagramme de classes.

### Niveau 1 — réponse minimale
Acteurs : Étudiant, Administrateur/enseignant

### Niveau 2 — réponse complète / solution type
Acteurs : Étudiant, Administrateur/enseignant. Cas : se connecter, consulter catalogue, s’inscrire/suivre cours, consulter contenu, passer évaluation, consulter note ; enseignant crée cours/évaluations et publie résultats. Classes : Etudiant(id:int, nom:String, email:String), Cours(id:int,titre:String,description:String), Evaluation(id:int,titre:String,date:Date), Inscription(id:int,date:Date) et Resultat(note:Decimal,date:Date). Étudiant 1—0..* Inscription *—1 Cours ; Cours 1—1..* Evaluation ; Étudiant et Evaluation sont liés par Resultat (note), chaque résultat concerne un étudiant et une évaluation.

### Niveau 3 — explication pédagogique
Les classes d’association Inscription et Resultat portent les données propres aux relations plusieurs-à-plusieurs.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Modéliser une relation plusieurs-à-plusieurs

## Réseaux — question 1 — Spécialité · lundi · dossier 3

### Énoncé / tâche associée
Définis LAN/MAN/WAN ; explique les équipements d’interconnexion de trois sites ; propose le schéma siège + deux agences ; découpe 192.168.10.0/24 pour 40, 20 et 12 postes avec réseau, masque, première/dernière adresse et broadcast ; explique DHCP ; diagnostique une panne d’accès aux serveurs d’une autre agence.

### Niveau 1 — réponse minimale
LAN : site local ; MAN : ville ; WAN : sites éloignés

### Niveau 2 — réponse complète / solution type
LAN : site local ; MAN : ville ; WAN : sites éloignés. Chaque site a switch et routeur ; relier les routeurs via WAN/VPN opérateur et faire du routage inter-sites. VLSM : siège 40 → /26, .0/26, masque .192, hôtes .1–.62, broadcast .63 ; agence 20 → /27, .64/27, masque .224, hôtes .65–.94, broadcast .95 ; agence 12 → /28, .96/28, masque .240, hôtes .97–.110, broadcast .111. DHCP attribue IP/masque/passerelle/DNS. Diagnostic : lien/VLAN, ipconfig, ping passerelle, ping IP distante, tracert, routes/pare-feu, DNS si seul le nom échoue.

### Niveau 3 — explication pédagogique
Allouer du plus grand au plus petit. Chaque plage possède assez d’hôtes et ne chevauche pas la suivante.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Diagnostiquer une perte de connectivité

## Java — question 1 — Spécialité · lundi · dossier 4

### Énoncé / tâche associée
Étudiant(matricule, nom, prénom, moyenne) : explique classe/objet/attribut/méthode ; écris la classe, constructeur, méthode d’affichage, admis() (moyenne ≥10), main qui crée deux étudiants et affiche admission ; distingue encapsulation, héritage et polymorphisme.

### Niveau 1 — réponse minimale
Une classe définit structure/comportements ; objet en est une instance ; attribut stocke l’état ; méthode réalise une action

### Niveau 2 — réponse complète / solution type
Une classe définit structure/comportements ; objet en est une instance ; attribut stocke l’état ; méthode réalise une action. Exemple : class Etudiant { private String matricule,nom,prenom; private double moyenne; public Etudiant(String m,String n,String p,double moy){matricule=m;nom=n;prenom=p;moyenne=moy;} public void afficher(){System.out.println(matricule+" "+nom+" "+prenom+" "+moyenne);} public boolean admis(){return moyenne>=10;} } Dans main créer e1,e2, appeler afficher() et admis(). Encapsulation masque les champs ; héritage spécialise une classe avec extends ; polymorphisme permet de manipuler une sous-classe via le type parent et d’appeler une méthode redéfinie.

### Niveau 3 — explication pédagogique
Garder les champs private et exposer des méthodes ; la décision admis() est true à 10 inclus.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer une classe
- Déclarer un attribut
- Écrire un constructeur
- Écrire une méthode
- Créer un objet et appeler une méthode
