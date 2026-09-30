# Épreuve de spécialité SIL — Jeudi

## Informations générales

- ID : EP-004
- Année : Non précisée dans le document original.
- Session : Jeudi
- Matière : Spécialité SIL
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Barème indiqué par dossier : Dossier 1 : 5 points, Dossier 2 : 5 points, Dossier 3 : 5 points, Dossier 4 : 5 points. Aucun total ajouté.
- Source : `EPREUVE_DE_SPECIALITE_jeudi.pdf` (9 pages PDF)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

## Page 1

                                                                  HOREB ACADEMY — Épreuve de Spécialité SIL



                                      HOREB ACADEMY
                            École Supérieure des Technologies Numériques



                          ÉPREUVE DE SPÉCIALITÉ
                                          Spécialité : SIL


 Consignes générales
 Lisez attentivement chaque dossier avant de répondre.
 Les questions sont de types variés : QCM, Vrai/Faux, association, classement, texte à compléter,
 calcul et rédaction.
 Pour les QCM : une seule réponse exacte. Pour les Vrai/Faux : justifiez les réponses « Faux ».
 Les schémas doivent être propres, lisibles et légendés. Le code doit être correctement indenté.
 Répondez sur la copie en indiquant clairement le numéro du dossier et de la question.



Dossier          Thème                                                                    Points
1                Base de données et requêtes SQL                                          5
2                Modélisation UML                                                         5
3                Téléinformatique et réseaux                                              5
4                Programmation Java                                                       5




                                                 Page 1


---

## Page 2

                                                                 HOREB ACADEMY — Épreuve de Spécialité SIL


DOSSIER 1 — BASE DE DONNÉES ET REQUÊTES SQL (5 points)

Une clinique souhaite informatiser la gestion de ses médecins, de ses patients et des consultations.
On considère les relations suivantes :
 SERVICE      (IdService, NomService)
 MEDECIN      (IdMedecin, Nom, Specialite, #IdService)
 PATIENT      (IdPatient, Nom, Prenom, DateNaissance)
 CONSULTATION (IdConsultation, DateConsultation, Motif, Tarif, #IdPatient, #IdMedecin)

Les clés étrangères sont précédées du signe #.

Question 1 — QCM (1 pt)
a) Dans la table CONSULTATION, la colonne IdPatient est :
       A. la clé primaire de CONSULTATION
       B. une clé étrangère qui référence la table PATIENT
       C. un attribut calculé
       D. un index unique
b) Avec ON DELETE RESTRICT, la suppression du patient n° 7 est refusée. La cause la plus probable
est que :
        A. la table PATIENT est vide
        B. des consultations référencent encore ce patient
        C. IdPatient vaut NULL
        D. la base de données est verrouillée
c) Quelle fonction d'agrégation permet de calculer le total des tarifs ?
       A. COUNT
       B. AVG
       C. SUM
       D. MAX
d) Un INNER JOIN entre MEDECIN et CONSULTATION retourne :
       A. tous les médecins, même ceux sans consultation
       B. uniquement les médecins ayant au moins une consultation
       C. toutes les consultations, même sans médecin
       D. le produit cartésien des deux tables

Question 2 — Vrai / Faux (1 pt)
Justifiez chaque réponse « Faux ».
1. La table SERVICE est la table mère de la table MEDECIN.
2. La clause WHERE permet de filtrer les groupes créés par GROUP BY.
3. COUNT(*) compte les lignes, même lorsque certaines colonnes contiennent NULL.
4. Une table fille peut contenir une valeur de clé étrangère qui n'existe pas dans la table mère.

Question 3 — Texte à compléter (0,5 pt)
Recopiez et complétez les trois espaces de la requête qui affiche les médecins ayant effectué plus de
5 consultations :
 SELECT m.Nom, COUNT(c.IdConsultation) AS nb
 FROM MEDECIN m
 (1) ________ JOIN CONSULTATION c ON m.IdMedecin = c.IdMedecin


                                                 Page 2


---

## Page 3

                                                                 HOREB ACADEMY — Épreuve de Spécialité SIL

 (2) ________ BY m.IdMedecin, m.Nom
 (3) ________ COUNT(c.IdConsultation) > 5;

Question 4 — Classement (0,5 pt)
Remettez dans l'ordre d'écriture correct les six clauses d'une requête SQL complète :

a) ORDER BY
b) WHERE
c) SELECT
d) HAVING
e) FROM
f) GROUP BY

Question 5 — Requêtes SQL (2 pts)
a) (0,5 pt) Afficher le nom et la spécialité des médecins du service « Pédiatrie ».
b) (0,75 pt) Afficher, pour chaque médecin, son nom et le montant total des tarifs de ses
consultations.
c) (0,75 pt) Afficher le nom et le prénom des patients qui n'ont jamais eu de consultation.




                                                 Page 3


---

## Page 4

                                                                     HOREB ACADEMY — Épreuve de Spécialité SIL


DOSSIER 2 — MODÉLISATION UML (5 points)

Une application de commande de repas en ligne met en relation des clients, des restaurants et des
livreurs.

   • Un client passe plusieurs commandes ; chaque commande est passée par un seul client.
   • Une commande contient plusieurs plats, chacun avec une quantité (ligne de commande).
   • Chaque plat appartient à un seul restaurant ; un restaurant propose plusieurs plats.
   • Une commande est livrée par un livreur ; un livreur peut effectuer plusieurs livraisons. Une
     commande n'a pas de livreur tant qu'elle n'est pas prise en charge.
   • Le client paie en ligne ; le restaurateur gère son menu ; l'administrateur supervise la
     plateforme.

Question 1 — QCM (1 pt)
a) Dans un diagramme de classes, le signe « + » devant un attribut indique une visibilité :
       A. privée
       B. publique
       C. protégée
       D. statique
b) La relation « extend » entre deux cas d'utilisation indique que :
        A. le cas étendant ajoute un comportement facultatif au cas de base
        B. le cas étendant est obligatoirement exécuté
        C. un acteur hérite d'un autre acteur
        D. un cas d'utilisation est supprimé
c) Quel diagramme décrit les états successifs d'un objet (par exemple une commande : créée,
payée, livrée) ?
        A. Diagramme de classes
        B. Diagramme d'états-transitions
        C. Diagramme de déploiement
        D. Diagramme d'objets
d) Chaque commande est passée par un seul client. La multiplicité placée du côté de Client dans
l'association Client–Commande est :
         A. 0..*
         B. 1
         C. 0..1
         D. 1..*

Question 2 — Association (1 pt)
Associez chaque phrase (1 à 4) à la multiplicité UML qui convient (A à D).

 Phrase                                                                   Multiplicité
 1. Une commande est passée par exactement un client.                     A. 1..*
 2. Un client peut n'avoir passé aucune commande ou en avoir passé        B. 0..1
 plusieurs.
 3. Une commande contient au moins un plat.                               C. 1



                                                  Page 4


---

## Page 5

                                                                  HOREB ACADEMY — Épreuve de Spécialité SIL


 Phrase                                                                  Multiplicité
 4. Une commande a au plus un livreur.                                   D. 0..*



Question 3 — Vrai / Faux (1 pt)
Justifiez chaque réponse « Faux ».
1. L'héritage se représente par une flèche à triangle creux, de la classe fille vers la classe mère.
2. Une association plusieurs-à-plusieurs entre Commande et Plat peut être modélisée par une classe
d'association (ligne de commande).
3. Un acteur est toujours une personne physique.
4. Un diagramme de séquence représente les relations statiques entre les classes.

Question 4 — Rédaction (0,5 pt)
Identifier les acteurs de l'application et proposer au moins cinq cas d'utilisation, en indiquant
l'acteur concerné par chacun.

Question 5 — Diagramme de classes (1,5 pt)
Réaliser le diagramme de classes UML du système avec au minimum les classes Client, Commande,
Plat, Restaurant, Livreur et la classe d'association LigneCommande. Vous préciserez :

   • au moins trois attributs pertinents par classe (avec leur type) ;
   • les associations, leurs noms et leurs multiplicités ;
   • l'attribut qui porte la quantité commandée et la classe à laquelle il appartient.




                                                  Page 5


---

## Page 6

                                                                 HOREB ACADEMY — Épreuve de Spécialité SIL


DOSSIER 3 — TÉLÉINFORMATIQUE ET RÉSEAUX (5 points)

Une entreprise organise son réseau local en quatre services :

 Service                                                 Nombre de postes
 Technique                                               60
 Commercial                                              28
 Comptabilité                                            20
 Direction                                               10


Chaque service est relié à un commutateur ; un routeur interconnecte les quatre réseaux et donne
accès à Internet. L'entreprise dispose du bloc d'adresses privé 192.168.50.0/24.

Question 1 — QCM (1 pt)
a) Un commutateur (switch) :
       A. relie des réseaux différents
       B. transmet les trames uniquement vers le port du destinataire, selon l'adresse MAC
       C. attribue automatiquement des adresses IP
       D. traduit les noms de domaine en adresses IP
b) Combien d'adresses d'hôtes utilisables contient un réseau /26 ?
      A. 30
      B. 62
      C. 64
      D. 126
c) Quel protocole traduit un nom de domaine en adresse IP ?
       A. DHCP
       B. DNS
       C. SMTP
       D. ARP
d) Quelle commande Windows permet d'afficher le chemin suivi par les paquets vers une
destination ?
        A. ipconfig
        B. ping
        C. tracert
        D. netstat

Question 2 — Association (0,75 pt)
Associez chaque élément (1 à 5) à la couche du modèle OSI dans laquelle il fonctionne (a à e).

 Élément                                            Couche OSI
 1. Commutateur (switch)                            a) Couche 7 — Application
 2. Routeur                                         b) Couche 4 — Transport
 3. Protocole TCP                                   c) Couche 2 — Liaison de données
 4. Protocole HTTP                                  d) Couche 1 — Physique



                                                Page 6


---

## Page 7

                                                                    HOREB ACADEMY — Épreuve de Spécialité SIL


 Élément                                               Couche OSI
 5. Câble RJ45                                         e) Couche 3 — Réseau



Question 3 — Classement (0,5 pt)
Remettez dans l'ordre les étapes de l'encapsulation d'une donnée émise par une application :

a) Trame
b) Segment
c) Bits
d) Paquet
e) Données

Question 4 — Plan d'adressage (calcul) (2 pts)
a) (0,75 pt) Pour chaque service, déterminer le préfixe CIDR minimal permettant d'accueillir tous les
postes. Justifier par un calcul.
b) (1,25 pt) En partant de 192.168.50.0/24 et en allouant les sous-réseaux du plus grand au plus
petit (méthode VLSM), compléter le tableau ci-dessous.
 Service           Préfixe   Masque            Adresse          1re adresse    Dernière       Broadcast
                                               réseau
 Technique


 Commercial


 Comptabilité


 Direction




Question 5 — Diagnostic (0,75 pt)
Les postes du service Comptabilité n'obtiennent plus d'adresse IP automatiquement et affichent une
adresse du type 169.254.x.x.

a) Que signifie ce type d'adresse et quelle en est la cause probable ?
b) Citez trois vérifications à effectuer, dans l'ordre, pour rétablir le service.




                                                   Page 7


---

## Page 8

                                                                 HOREB ACADEMY — Épreuve de Spécialité SIL


DOSSIER 4 — PROGRAMMATION JAVA (5 points)

Une banque souhaite gérer ses comptes en Java. Chaque compte possède : un numéro (String), un
titulaire (String) et un solde (double).

Question 1 — QCM (1 pt)
a) Qu'affiche l'instruction System.out.println(7 / 2); ?
       A. 3.5
       B. 3
       C. 4
       D. Une erreur de compilation
b) Quelle boucle s'exécute toujours au moins une fois ?
       A. for
       B. while
       C. do … while
       D. for each
c) L'encapsulation consiste à :
        A. hériter des attributs d'une autre classe
        B. cacher les attributs et n'y donner accès que par des méthodes
        C. définir plusieurs constructeurs
        D. définir plusieurs méthodes portant le même nom
d) Quel mot-clé désigne l'objet courant à l'intérieur d'une méthode ?
       A. super
       B. this
       C. new
       D. static

Question 2 — Vrai / Faux (1 pt)
Justifiez chaque réponse « Faux ».
1. Une méthode déclarée void ne retourne aucune valeur.
2. Une classe fille hérite des attributs et des méthodes publics de sa classe mère.
3. En Java, on utilise == pour comparer le contenu de deux chaînes de caractères.
4. La taille d'un tableau Java peut être modifiée après sa création.

Question 3 — Texte à compléter (0,5 pt)
Recopiez et complétez les trois espaces du code suivant :
 public class CompteBancaire {
     private double solde;

      public void deposer(double montant) {
          if (montant (1) ____ 0) {
              solde (2) ____ montant;
          }
      }

      public double getSolde() {
          (3) ________ solde;
      }

                                                  Page 8


---

## Page 9

                                                                HOREB ACADEMY — Épreuve de Spécialité SIL

 }

Question 4 — Analyse de code (0,5 pt)
Qu'affiche le programme suivant ? Quel est son rôle ?
 int[] t = {4, 7, 2, 9};
 int max = t[0];
 for (int i = 1; i < t.length; i++) {
     if (t[i] > max) {
         max = t[i];
     }
 }
 System.out.println(max);

Question 5 — Programmation (2 pts)
a) (0,75 pt) Écrire la classe CompteBancaire avec ses trois attributs (encapsulés) et un constructeur
permettant de les initialiser.
b) (0,25 pt) Écrire la méthode deposer(double montant) qui ajoute le montant au solde si celui-ci
est strictement positif.
c) (0,5 pt) Écrire la méthode retirer(double montant) qui retourne false si le solde est
insuffisant, et qui sinon débite le compte et retourne true.
d) (0,5 pt) Écrire un programme principal qui crée un compte, y dépose un montant, tente un
retrait, puis affiche le solde final.

                                        — Fin de l'épreuve —




                                                Page 9
