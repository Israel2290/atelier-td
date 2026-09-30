# Épreuve de spécialité SIL — Mardi

## Informations générales

- ID : EP-002
- Année : Non précisée dans le document original.
- Session : Mardi
- Matière : Spécialité SIL
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Non précisé dans le document original.
- Source : `Epreuve_Specialite_SIL_MARDI.docx` (DOCX)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

# ÉPREUVE DE SPÉCIALITÉ – SIL

Spécialité : Systèmes Informatiques et Logiciels (SIL)

## Consignes générales

Lire attentivement chaque dossier.

Justifier les réponses lorsque cela est demandé.

Les requêtes SQL doivent être correctement structurées.

Les schémas UML et réseaux doivent être propres et légendés.

Pour les programmes Java, respecter la syntaxe et les principes de la programmation orientée objet.

# DOSSIER 1 – BASES DE DONNÉES ET SQL

Une entreprise souhaite mettre en place une application pour gérer ses clients, produits et commandes.

CLIENT (IdClient, Nom, Prenom, Telephone, Ville)

PRODUIT (IdProduit, Designation, Prix, Stock)

COMMANDE (IdCommande, DateCommande, IdClient)

LIGNE_COMMANDE (IdCommande, IdProduit, Quantite)

1. Expliquer la différence entre une clé primaire, une clé étrangère et une clé composée.

2. Identifier les clés primaires de chaque table.

3. Identifier toutes les clés étrangères présentes dans le modèle.

4. Écrire une requête SQL permettant d'afficher tous les clients habitant à Cotonou.

5. Écrire une requête permettant d'afficher les produits dont le prix est supérieur à 50 000 FCFA.

6. Écrire une requête permettant d'afficher les commandes avec l'identifiant de commande, la date de commande, le nom du client et son prénom.

7. Écrire une requête permettant d'afficher la désignation des produits commandés et les quantités correspondantes.

8. Écrire une requête permettant de calculer le montant total de chaque ligne de commande : Montant = Prix × Quantité.

9. Écrire une requête permettant de connaître le nombre de commandes effectuées par chaque client.

10. Écrire une requête permettant d'afficher les produits dont le stock est inférieur à 10 unités.

11. Expliquer le rôle de la clause GROUP BY.

12. Quelle différence existe entre WHERE et HAVING ? Donner un exemple pour chacune.

# DOSSIER 2 – MODÉLISATION UML

Une bibliothèque universitaire souhaite informatiser la gestion de ses ouvrages.

Un étudiant peut rechercher des ouvrages, emprunter plusieurs ouvrages et retourner les ouvrages empruntés.

Un ouvrage appartient à une catégorie. Un bibliothécaire enregistre les emprunts et les retours.

1. Identifier les différents acteurs du système.

2. Identifier au moins 8 cas d'utilisation.

3. Construire le diagramme de cas d'utilisation UML.

4. Donner trois scénarios possibles correspondant à : emprunter un ouvrage ; retourner un ouvrage ; rechercher un ouvrage.

5. Identifier au moins 6 classes nécessaires à la modélisation.

6. Pour les classes Etudiant, Ouvrage, Emprunt et Bibliothecaire, proposer au minimum 4 attributs par classe.

7. Identifier les principales associations entre les classes.

8. Déterminer les cardinalités appropriées.

9. Réaliser le diagramme de classes UML complet.

10. Expliquer pourquoi la classe Emprunt peut être considérée comme une classe importante dans cette modélisation.

# DOSSIER 3 – TÉLÉINFORMATIQUE ET RÉSEAUX

Une entreprise dispose de trois services :

Service Administration : 25 postes ;

Service Comptabilité : 15 postes ;

Service Informatique : 10 postes.

L'entreprise dispose d'un accès Internet et souhaite séparer logiquement les trois services.

Réseau de départ : 192.168.50.0/24

1. Définir les notions suivantes : adresse IP ; masque de sous-réseau ; passerelle par défaut ; adresse de broadcast.

2. Expliquer la différence entre switch et routeur.

3. Proposer une architecture réseau adaptée à cette entreprise et la représenter sous forme de schéma.

4. À partir du réseau 192.168.50.0/24, proposer un découpage permettant d'obtenir trois sous-réseaux adaptés aux besoins des services. Pour chaque sous-réseau, préciser l'adresse réseau, le masque, la première IP utilisable, la dernière IP utilisable et le broadcast.

5. Quel est le rôle de la passerelle par défaut ?

6. Un ordinateur possède : IP 192.168.50.25 ; Masque 255.255.255.224 ; Passerelle 192.168.50.1. Déterminer l'adresse réseau, l'adresse de broadcast et le nombre maximal d'hôtes utilisables.

7. Expliquer le fonctionnement général de DHCP.

8. Un poste obtient une adresse 169.254.x.x. Que peut-on suspecter ? Proposer une démarche de diagnostic.

9. Un utilisateur peut accéder aux autres ordinateurs de son réseau local mais pas à Internet. Donner au moins cinq vérifications successives permettant de rechercher la panne.

10. Expliquer la différence entre TCP et UDP et donner un exemple d'utilisation pour chacun.

# DOSSIER 4 – PROGRAMMATION JAVA / POO

On souhaite développer une application Java permettant de gérer les employés d'une entreprise.

Chaque employé possède : un matricule ; un nom ; un prénom ; un salaire ; un service.

1. Définir les notions suivantes : classe ; objet ; attribut ; méthode ; constructeur.

2. Déclarer une classe Employe contenant les attributs nécessaires.

3. Déclarer les attributs en utilisant le principe d'encapsulation.

4. Écrire un constructeur permettant d'initialiser un employé.

5. Écrire les méthodes get et set nécessaires.

6. Écrire une méthode afficherInformations() permettant d'afficher les informations de l'employé.

7. Écrire une méthode augmenterSalaire(double pourcentage) permettant d'augmenter le salaire d'un employé selon un pourcentage donné.

8. Écrire une méthode estCadre() retournant true lorsque le salaire est supérieur ou égal à 500 000 FCFA, et false dans le cas contraire.

9. Écrire un programme principal permettant de créer trois employés, afficher leurs informations, augmenter le salaire d'un employé et déterminer les employés considérés comme cadres.

10. On souhaite créer une classe Manager qui hérite de Employe. Expliquer comment mettre en œuvre cet héritage en Java.

11. Donner un exemple concret de polymorphisme avec Employe et Manager.

12. Expliquer la différence entre surcharge de méthode et redéfinition de méthode.
