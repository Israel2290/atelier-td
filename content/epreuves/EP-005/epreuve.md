# Épreuve de spécialité SIL — Mercredi (PDF)

## Informations générales

- ID : EP-005
- Année : Non précisée dans le document original.
- Session : Mercredi
- Matière : Spécialité SIL
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Barème indiqué par dossier : Dossier 1 : 5 points, Dossier 2 : 5 points, Dossier 3 : 5 points, Dossier 4 : 5 points. Aucun total ajouté.
- Source : `EPREUVE_DE_SPECIALITE_SIL_Mercredi.pdf` (9 pages PDF)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

## Page 1

                                                          HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet



                                     HOREB ACADEMY
                           École Supérieure des Technologies Numériques



                         ÉPREUVE DE SPÉCIALITÉ
                                          Spécialité : SIL


Consignes générales
Lisez attentivement chaque dossier avant de répondre.
Les questions sont de types variés : QCM, Vrai/Faux, association, classement, texte à compléter,
calcul et rédaction.
Pour les QCM : une seule réponse exacte, sauf indication contraire. Pour les Vrai/Faux : justifiez les
réponses « Faux ».
Les schémas doivent être propres, lisibles et légendés. Le code doit être correctement indenté.
Répondez sur la copie en indiquant clairement le numéro du dossier et de la question.




                                                 Page 1


---

## Page 2

                                                              HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


DOSSIER 1 — BASE DE DONNÉES ET REQUÊTES SQL (5 points)

Une bibliothèque universitaire souhaite informatiser la gestion de ses livres et des emprunts de ses
adhérents. On considère les relations suivantes :
 ADHERENT (IdAdherent, Nom, Prenom, Telephone)
 CATEGORIE (IdCategorie, Libelle)
 LIVRE     (IdLivre, Titre, Auteur, AnneeEdition, #IdCategorie)
 EMPRUNT   (IdEmprunt, DateEmprunt, DateRetour, #IdAdherent, #IdLivre)

Les clés étrangères sont précédées du signe #. DateRetour vaut NULL tant que le livre n'est pas rendu.

Question 1 — QCM (1 pt)
a) Une clé étrangère est :
       A. une colonne qui identifie de façon unique chaque ligne de sa table
       B. une colonne qui reprend la valeur de la clé primaire d'une autre table
       C. une colonne qui ne peut jamais contenir de doublon
       D. un index créé automatiquement par le SGBD
b) On insère dans EMPRUNT une ligne avec IdAdherent = 500, alors qu'aucun adhérent n'a cet
identifiant. Le SGBD :
         A. accepte l'insertion sans rien signaler
         B. refuse l'insertion (violation d'intégrité référentielle)
         C. accepte l'insertion et met IdAdherent à NULL
         D. crée automatiquement l'adhérent 500
c) Quelle clause permet de filtrer les résultats d'un regroupement (par exemple les catégories ayant
plus de 10 livres) ?
        A. WHERE
        B. HAVING
        C. ORDER BY
        D. DISTINCT
d) Par rapport à la table EMPRUNT, quelles sont les tables mères ?
        A. EMPRUNT elle-même
        B. ADHERENT et LIVRE
        C. CATEGORIE uniquement
        D. Aucune : les quatre tables sont indépendantes

Question 2 — Vrai / Faux (1 pt)
Justifiez chaque réponse « Faux ».
1. La table LIVRE est à la fois fille de CATEGORIE et mère de EMPRUNT.
2. Avec ON DELETE RESTRICT, on peut supprimer un adhérent qui a encore des emprunts.
3. Une clé primaire peut contenir la valeur NULL.
4. Il faut insérer un emprunt avant d'insérer l'adhérent concerné.

Question 3 — Texte à compléter (0,5 pt)
Mots proposés : ADHERENT — LIVRE — primaire — étrangère — intégrité — référentielle.
Pour créer la table EMPRUNT, on doit d'abord créer les tables (1) ________ et (2) ________. La
colonne IdAdherent de EMPRUNT est une clé (3) ________ qui référence la clé (4) ________ de la
table ADHERENT. Cette contrainte garantit l'(5) ________ (6) ________.

                                                     Page 2


---

## Page 3

                                                              HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


Question 4 — Association (0,5 pt)
Associez chaque élément SQL (1 à 5) à son rôle (a à e). Exemple de réponse : 1 → c.

 Élément SQL                                     Rôle
 1. WHERE                                        a) Trier le résultat
 2. GROUP BY                                     b) Relier deux tables par leurs clés
 3. ORDER BY                                     c) Compter le nombre de lignes
 4. COUNT( )                                     d) Regrouper les lignes ayant une valeur commune
 5. JOIN … ON                                    e) Filtrer les lignes avant regroupement



Question 5 — Requêtes SQL (2 pts)
a) (0,5 pt) Afficher le titre et l'auteur des livres de la catégorie « Informatique ».
b) (0,75 pt) Afficher, pour chaque catégorie, son libellé et le nombre de livres qu'elle contient. Les
catégories sans aucun livre doivent apparaître avec le nombre 0.
c) (0,75 pt) Afficher le nom et le prénom des adhérents qui n'ont jamais emprunté de livre.




                                                   Page 3


---

## Page 4

                                                             HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


DOSSIER 2 — MODÉLISATION UML (5 points)

Une plateforme de covoiturage met en relation des conducteurs, qui proposent des trajets, et des
passagers, qui réservent des places.

   • Un conducteur peut publier plusieurs trajets ; chaque trajet est publié par un seul conducteur.
   • Un trajet possède un lieu de départ, une destination, une date, un prix par place et un nombre
     de places.
   • Un passager peut effectuer plusieurs réservations ; un trajet peut recevoir plusieurs
     réservations.
   • Après un trajet, un passager peut noter le conducteur (une note au plus par réservation).
   • L'administrateur valide les comptes des conducteurs et peut suspendre un compte.

Question 1 — QCM (1 pt)
a) Dans un diagramme de cas d'utilisation, un acteur est :
       A. une classe interne du système
       B. une entité externe qui interagit avec le système
       C. une base de données
       D. un attribut d'une classe
b) La relation « include » entre deux cas d'utilisation signifie que :
        A. le second cas est facultatif
        B. le cas de base inclut obligatoirement le comportement du second cas
        C. les deux cas sont des acteurs
        D. le second cas remplace le premier
c) Quel diagramme montre l'ordre chronologique des messages échangés entre des objets ?
       A. Diagramme de classes
       B. Diagramme de cas d'utilisation
       C. Diagramme de séquence
       D. Diagramme de composants
d) Dans l'association Conducteur–Trajet, la multiplicité 0..* placée du côté de Trajet signifie qu'un
conducteur peut publier :
       A. exactement un trajet
       B. au moins un trajet
       C. zéro, un ou plusieurs trajets
       D. zéro ou un trajet

Question 2 — Association (1 pt)
Associez chaque phrase (1 à 4) à la multiplicité UML qui convient (A à D).

 Phrase                                                                   Multiplicité
 1. Un trajet est publié par exactement un conducteur.                    A. 0..1
 2. Un conducteur peut ne publier aucun trajet ou en publier plusieurs.   B. 1
 3. Un trajet comporte au moins une étape (point d'arrêt).                C. 0..*
 4. Une réservation peut avoir au plus une note.                          D. 1..*




                                                    Page 4


---

## Page 5

                                                             HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


Question 3 — Vrai / Faux (1 pt)
Justifiez chaque réponse « Faux ».
1. Dans une composition, la partie ne peut pas exister sans le tout.
2. Une classe abstraite peut être instanciée directement.
3. En UML, un attribut précédé du signe « - » est privé.
4. Un diagramme d'activités décrit la structure statique des classes.

Question 4 — Rédaction (0,5 pt)
Identifier les acteurs de la plateforme et proposer au moins cinq cas d'utilisation, en indiquant
l'acteur concerné par chacun.

Question 5 — Diagramme de classes (1,5 pts)
Réaliser le diagramme de classes UML du système avec au minimum les classes Conducteur,
Passager, Trajet et Reservation. Vous préciserez :

   • au moins trois attributs pertinents par classe (avec leur type et leur visibilité) ;
   • les associations, leurs noms et leurs multiplicités ;
   • la place de la classe Reservation entre Passager et Trajet, et l'endroit où l'on mémorise la note.




                                                  Page 5


---

## Page 6

                                                            HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


DOSSIER 3 — TÉLÉINFORMATIQUE ET RÉSEAUX (5 points)

Un établissement scolaire est composé de trois bâtiments :

 Bâtiment                                                   Nombre de postes
 Administration                                             50
 Salle informatique                                         25
 Bibliothèque                                               10


Chaque bâtiment dispose d'un commutateur. Un routeur interconnecte les trois réseaux locaux et
donne accès à Internet. L'établissement dispose du bloc d'adresses privé 192.168.20.0/24.

Question 1 — QCM (1 pt)
a) Quel équipement relie des réseaux différents et achemine les paquets entre eux ?
       A. Concentrateur (hub)
       B. Commutateur (switch)
       C. Routeur
       D. Répéteur
b) Combien d'adresses d'hôtes utilisables contient un réseau /27 ?
      A. 14
      B. 30
      C. 32
      D. 62
c) Laquelle de ces adresses est une adresse IPv4 privée ?
       A. 8.8.8.8
       B. 172.32.4.5
       C. 192.168.20.7
       D. 200.10.10.1
d) Sur quel port UDP écoute par défaut un serveur DHCP ?
        A. 53
        B. 67
        C. 80
        D. 443

Question 2 — Association (0,75 pt)
Associez chaque protocole (1 à 5) à son port par défaut (a à e).

 Protocole                                          Port
 1. HTTPS                                           a) 21
 2. DNS                                             b) 25
 3. SSH                                             c) 53
 4. SMTP                                            d) 443
 5. FTP (contrôle)                                  e) 22




                                                Page 6


---

## Page 7

                                                         HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


Question 3 — Classement (0,5 pt)
Remettez dans l'ordre chronologique les quatre étapes de l'attribution d'une adresse par DHCP :

a) Request (le client demande l'adresse proposée)
b) Discover (le client cherche un serveur)
c) Acknowledge (le serveur confirme le bail)
d) Offer (le serveur propose une adresse)

Question 4 — Plan d'adressage (calcul) (2 pts)
a) (0,75 pt) Pour chaque bâtiment, déterminer le préfixe CIDR minimal permettant d'accueillir tous
les postes. Justifier par un calcul.
b) (1,25 pt) En partant de 192.168.20.0/24 et en allouant les sous-réseaux du plus grand au plus
petit (méthode VLSM), compléter le tableau ci-dessous.
 Bâtiment         Préfixe   Masque   Adresse   1re       Dernière   Broadcast
                                     réseau    adresse
 Administration


 Salle
 informatique

 Bibliothèque




Question 5 — Diagnostic (0,75 pt)
Un poste de la salle informatique communique avec les autres postes de son réseau et avec son
commutateur, mais n'accède ni aux serveurs de l'Administration ni à Internet. Présentez une
démarche de diagnostic en cinq étapes (avec les commandes utilisées) permettant de localiser la
panne.




                                                Page 7


---

## Page 8

                                                          HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


DOSSIER 4 — PROGRAMMATION JAVA (5 points)

Une boutique souhaite gérer ses produits en Java. Chaque produit possède : une référence (String),
une désignation (String), un prix unitaire (double) et une quantité en stock (int).

Question 1 — QCM (1 pt)
a) Quel mot-clé permet de créer un objet ?
       A. class
       B. new
       C. this
       D. static
b) Un attribut déclaré private est accessible :
       A. depuis toutes les classes
       B. uniquement à l'intérieur de sa propre classe
       C. uniquement dans les classes filles
       D. uniquement dans les classes du même package
c) Le constructeur d'une classe :
        A. porte le même nom que la classe et n'a pas de type de retour
        B. doit obligatoirement s'appeler main
        C. retourne toujours un entier
        D. est toujours déclaré void
d) Quel mot-clé permet à une classe d'hériter d'une autre classe ?
       A. implements
       B. extends
       C. inherits
       D. import

Question 2 — Vrai / Faux (1 pt)
Justifiez chaque réponse « Faux ».
1. Une classe peut posséder plusieurs constructeurs ayant des paramètres différents.
2. La méthode main doit être déclarée non statique pour démarrer un programme.
3. En Java, int et double sont des classes.
4. Deux objets créés à partir de la même classe ont chacun leurs propres valeurs d'attributs.

Question 3 — Texte à compléter (0,5 pt)
Recopiez et complétez les trois espaces du code suivant :
 public class Produit {
     (1) ________ String reference;
     private double prix;

      public (2) ________ (String reference, double prix) {
          (3) ________.reference = reference;
          this.prix = prix;
      }
 }




                                                 Page 8


---

## Page 9

                                                          HOREB ACADEMY — Épreuve de Spécialité SIL — Sujet


Question 4 — Analyse de code (0,5 pt)
Qu'affiche le programme suivant ? Détaillez les valeurs de somme à chaque tour de boucle.
 int somme = 0;
 for (int i = 1; i <= 5; i++) {
     if (i % 2 == 0) {
         somme += i;
     } else {
         somme -= 1;
     }
 }
 System.out.println(somme);

Question 5 — Programmation (2 pts)
a) (0,75 pt) Écrire la classe Produit avec ses quatre attributs (encapsulés) et un constructeur
permettant de les initialiser.
b) (0,25 pt) Écrire la méthode valeurStock() qui retourne la valeur totale du stock du produit (prix
× quantité).
c) (0,25 pt) Écrire la méthode estEnRupture() qui retourne true si la quantité en stock est égale à
0, et false sinon.
d) (0,75 pt) Écrire un programme principal qui crée deux produits, affiche pour chacun sa
désignation et la valeur de son stock, puis indique s'il est en rupture de stock.

                                         — Fin de l'épreuve —




                                                 Page 9
