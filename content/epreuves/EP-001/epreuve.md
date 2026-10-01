# Épreuve de spécialité SIL — Lundi

## Informations générales

- ID : EP-001
- Année : Non précisée dans le document original.
- Session : Lundi
- Matière : Spécialité SIL
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Barème partiel mentionné dans la source ; répartition/total global non précisé.
- Source : `ÉPREUVE DE SPÉCIALITÉ LUNDI.docx` (DOCX)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

# Cours

## 1. Comprendre la matière

Cette épreuve de spécialité SIL combine base de données/SQL, modélisation UML, réseaux et programmation Java. Il faut savoir passer d’un besoin concret à un schéma, une requête, une architecture ou un petit programme objet.

## 2. Notions essentielles

### SQL et modèle relationnel
Une table contient des lignes et des colonnes. Une clé primaire identifie une ligne ; une clé étrangère relie une table à une autre. Une inscription relie un étudiant à une formation.

### UML
Un acteur est externe au système. Un cas d’utilisation décrit un objectif. Une classe possède des attributs et des méthodes ; une association indique qui est lié à qui, avec des cardinalités comme `1`, `0..*` ou `1..*`. Une relation plusieurs-à-plusieurs se traduit souvent par une classe d’association.

### Réseaux
LAN, MAN et WAN désignent des étendues différentes. Un switch relie les postes d’un LAN ; un routeur relie des réseaux IP. Pour un sous-réseau, distinguer adresse réseau, hôtes utilisables et broadcast. DHCP attribue automatiquement une configuration IP.

### Java et POO
Une classe décrit un type, un objet est une instance, un attribut stocke l’état et une méthode réalise une action. L’encapsulation rend les attributs privés et fournit des méthodes d’accès. L’héritage réutilise une classe avec `extends` ; le polymorphisme permet d’utiliser une sous-classe via le type parent.

## 3. Méthodes pour résoudre les exercices

### SQL
1. Repérer les tables et les clés dans l’énoncé.
2. Choisir la table de départ.
3. Ajouter les `JOIN ... ON` nécessaires.
4. Filtrer avec `WHERE`.
5. Ajouter `GROUP BY` puis `COUNT`, `SUM` ou `HAVING` si un regroupement est demandé.

### UML
Lister les acteurs et objectifs, puis les classes et leurs attributs. Pour chaque association, écrire les cardinalités des deux côtés. Vérifier qu’une donnée propre au lien, comme une note ou une date, est portée par une classe d’association.

### Réseau
Pour un besoin de n hôtes, choisir le plus petit bloc tel que `2^bits_hôte - 2 >= n`. Puis calculer les blocs dans l’ordre du plus grand besoin au plus petit.

### Java
Écrire les attributs privés, le constructeur, les méthodes demandées, puis un `main` qui crée des objets et appelle les méthodes. Vérifier les conditions limites comme moyenne `>= 10`.

## 4. Astuces et pièges à éviter

- Ne pas confondre clé primaire et clé étrangère.
- `WHERE` filtre les lignes ; `HAVING` filtre les groupes.
- Une classe UML n’est pas un acteur.
- Un `/27` fournit 30 hôtes utilisables, pas 32.
- Un constructeur Java n’a pas de type de retour.
- Les chaînes Java se comparent avec `equals`, pas avec `==`.

## 5. Ce qu’il faut retenir

La copie doit suivre l’ordre de la question : identifier, relier, calculer, puis justifier. Les quatre réflexes centraux sont PK/FK en SQL, cardinalités en UML, réseau/broadcast en IP et encapsulation en Java.
---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

# ÉPREUVE DE SPÉCIALITÉ

Spécialités : SIL

## Consignes générales

Lisez attentivement chaque dossier avant de répondre.

Justifiez vos réponses lorsque cela est demandé.

Les schémas doivent être propres, lisibles et correctement légendés.

Toute réponse doit être présentée de manière claire et méthodique.

# DOSSIER 1 – BASE DE DONNÉES ET REQUÊTES SQL

Une école souhaite informatiser la gestion de ses étudiants, formations et inscriptions.

On considère les relations suivantes :

ETUDIANT(IdEtudiant, Nom, Prenom, DateNaissance)

FORMATION(IdFormation, Libelle, Niveau)

INSCRIPTION(IdInscription, DateInscription, IdEtudiant, IdFormation)

## Travail demandé

1. Expliquer la différence entre une clé primaire et une clé étrangère. Donner un exemple dans le schéma proposé.

2. Identifier les clés primaires des trois relations et préciser les clés étrangères.

3. Écrire une requête SQL permettant d'afficher le nom et le prénom de tous les étudiants.

4. Écrire une requête SQL permettant d'afficher les étudiants inscrits à la formation dont IdFormation = 3.

5. Écrire une requête SQL permettant d'afficher :

Nom étudiant – Prénom – Libellé de la formation – Date d'inscription.

La requête devra utiliser les jointures appropriées.

6. Écrire une requête permettant de compter le nombre d'étudiants inscrits dans chaque formation.

# DOSSIER 2 – MODÉLISATION UML

Une plateforme de formation en ligne permet aux étudiants de consulter des cours et de passer des évaluations.

Un étudiant peut s'inscrire à plusieurs cours.
Un cours peut être suivi par plusieurs étudiants.
Chaque cours comporte plusieurs évaluations.
Un étudiant peut obtenir une note à une évaluation.

## Travail demandé

1. Identifier les principaux acteurs du système.

2. Donner au moins six cas d'utilisation correspondant au fonctionnement de la plateforme.

3. Décrire textuellement le diagramme de cas d'utilisation en précisant les relations entre les acteurs et les cas d'utilisation.

4. Identifier les principales classes nécessaires à la modélisation du système.

5. Pour les classes Etudiant, Cours et Evaluation, proposer au minimum trois attributs pertinents pour chacune.

6. Déterminer les associations et cardinalités entre les classes.

7. Réaliser un diagramme de classes UML cohérent représentant le système.

# DOSSIER 3 – TÉLÉINFORMATIQUE ET RÉSEAUX

Barème : 5 points

Une entreprise possède un siège et deux agences. Le siège dispose de 40 postes, la première agence de 20 postes et la deuxième de 12 postes.

Les différents sites doivent communiquer entre eux. Chaque site dispose d'un commutateur et d'un routeur.

## Travail demandé

1. Expliquer la différence entre un LAN, un MAN et un WAN.

2. Identifier les équipements réseau nécessaires pour interconnecter les trois sites et préciser le rôle de chacun.

3. Proposer une architecture réseau permettant l'interconnexion du siège et des deux agences. Présenter votre proposition sous forme d'un schéma.

4. L'entreprise utilise le réseau 192.168.10.0/24.
Proposer un découpage en sous-réseaux permettant d'affecter un sous-réseau à chacun des trois sites.

Pour chaque sous-réseau proposé, préciser :

adresse réseau ;

masque ;

première adresse utilisable ;

dernière adresse utilisable ;

adresse de broadcast.

5. Expliquer le rôle du protocole DHCP dans cette infrastructure.

6. Un utilisateur peut communiquer avec les postes de son réseau local mais ne peut pas accéder aux serveurs d'une autre agence.

Présenter une démarche de diagnostic permettant d'identifier l'origine de la panne.

# DOSSIER 4 – PROGRAMMATION JAVA

Barème : 5 points

Une application Java doit permettre de gérer les étudiants d'un établissement.

Chaque étudiant possède :

un matricule ;

un nom ;

un prénom ;

une moyenne.

## Travail demandé

1. Expliquer les notions suivantes en programmation orientée objet :

classe ;

objet ;

attribut ;

méthode.

2. Déclarer une classe Etudiant comportant les attributs nécessaires.

3. Écrire un constructeur permettant d'initialiser un étudiant.

4. Écrire une méthode permettant d'afficher les informations d'un étudiant.

5. Écrire une méthode admis() retournant true si la moyenne de l'étudiant est supérieure ou égale à 10, et false dans le cas contraire.

6. Écrire un programme principal permettant de :

créer deux étudiants ;

afficher leurs informations ;

déterminer pour chacun s'il est admis ou non.

7. Expliquer la différence entre encapsulation, héritage et polymorphisme en Java.
