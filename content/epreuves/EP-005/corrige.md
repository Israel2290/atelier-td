# Corrigé type — Épreuve de spécialité SIL — Mercredi (PDF)

- Identifiant : EP-005
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Bases de données — question 1 — SIL PDF · mercredi · SQL

### Énoncé / tâche associée
QCM bibliothèque : (a) définition d’une clé étrangère ; (b) insertion d’un emprunt avec adhérent inexistant ; (c) filtre sur agrégats ; (d) tables mères d’EMPRUNT.

### Niveau 1 — réponse minimale
(a) B : référence la clé primaire d’une autre table

### Niveau 2 — réponse complète / solution type
(a) B : référence la clé primaire d’une autre table. (b) B : insertion refusée par intégrité référentielle. (c) B : HAVING. (d) B : ADHERENT et LIVRE.

### Niveau 3 — explication pédagogique
La contrainte de clé étrangère garantit l’existence de l’adhérent et du livre référencés.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Filtrer les groupes avec HAVING
- Déclarer clés primaires et étrangères
- Choisir les contraintes d’une colonne
- Insérer une ligne avec INSERT
- Repérer PK, FK et table mère/fille

## Bases de données — question 2 — SIL PDF · mercredi · SQL

### Énoncé / tâche associée
Vrai ou faux : (1) LIVRE est fille de CATEGORIE et mère d’EMPRUNT ; (2) RESTRICT autorise la suppression d’un adhérent encore emprunté ; (3) une clé primaire accepte NULL ; (4) l’emprunt doit être inséré avant l’adhérent.

### Niveau 1 — réponse minimale
(1) Vrai

### Niveau 2 — réponse complète / solution type
(1) Vrai. (2) Faux : RESTRICT refuse la suppression référencée. (3) Faux : une clé primaire est non NULL. (4) Faux : insérer d’abord l’adhérent et le livre, puis l’emprunt.

### Niveau 3 — explication pédagogique
Les parents doivent exister avant d’insérer la ligne enfant qui les référence.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer clés primaires et étrangères
- Choisir les contraintes d’une colonne
- Insérer une ligne avec INSERT
- Modifier ou supprimer une ligne
- Repérer PK, FK et table mère/fille

## Bases de données — question 3 — SIL PDF · mercredi · SQL

### Énoncé / tâche associée
Complète : créer d’abord les tables ___ et ___ ; IdAdherent est une clé ___ qui référence la clé ___ d’ADHERENT ; cela garantit l’___ ___.

### Niveau 1 — réponse minimale
ADHERENT ; LIVRE ; étrangère ; primaire ; intégrité référentielle.

### Niveau 2 — réponse complète / solution type
ADHERENT ; LIVRE ; étrangère ; primaire ; intégrité référentielle.

### Niveau 3 — explication pédagogique
Créer les tables référencées avant la table EMPRUNT qui porte leurs clés étrangères.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer clés primaires et étrangères

## Bases de données — question 4 — SIL PDF · mercredi · SQL

### Énoncé / tâche associée
Associe WHERE, GROUP BY, ORDER BY, COUNT() et JOIN…ON aux rôles : trier, relier tables, compter lignes, regrouper, filtrer avant regroupement.

### Niveau 1 — réponse minimale
WHERE : filtrer les lignes

### Niveau 2 — réponse complète / solution type
WHERE : filtrer les lignes. GROUP BY : regrouper. ORDER BY : trier. COUNT() : compter. JOIN…ON : relier les tables.

### Niveau 3 — explication pédagogique
WHERE intervient avant le regroupement ; HAVING intervient après.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Compter par groupe avec GROUP BY
- Trier et supprimer les doublons

## Bases de données — question 5 — SIL PDF · mercredi · SQL

### Énoncé / tâche associée
Bibliothèque : (a) livres de catégorie Informatique ; (b) nombre de livres par catégorie en conservant les catégories vides ; (c) adhérents n’ayant jamais emprunté.

### Niveau 1 — réponse minimale
(a) SELECT l.Titre,l.Auteur FROM LIVRE l JOIN CATEGORIE c ON c.IdCategorie=l.IdCategorie WHERE c.Libelle='Informatique'; (b) SELECT c.Libelle,COUNT(l.IdLivre) FROM CATEGORIE c LEFT JOIN LIVRE l ON l.IdCategorie=c.IdCategorie GROUP BY c.IdCategorie,c.Libelle; (c) SELECT a.Nom,a.Prenom FROM ADHERENT a LEFT JOIN EMPRUNT e ON e.IdAdherent=a.IdAdherent WHERE e.IdEmprunt IS NULL;

### Niveau 2 — réponse complète / solution type
(a) SELECT l.Titre,l.Auteur FROM LIVRE l JOIN CATEGORIE c ON c.IdCategorie=l.IdCategorie WHERE c.Libelle='Informatique'; (b) SELECT c.Libelle,COUNT(l.IdLivre) FROM CATEGORIE c LEFT JOIN LIVRE l ON l.IdCategorie=c.IdCategorie GROUP BY c.IdCategorie,c.Libelle; (c) SELECT a.Nom,a.Prenom FROM ADHERENT a LEFT JOIN EMPRUNT e ON e.IdAdherent=a.IdAdherent WHERE e.IdEmprunt IS NULL;

### Niveau 3 — explication pédagogique
Pour compter zéro sur une jointure gauche, compter une clé non NULL de la table fille, pas COUNT(*).

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Lire des données avec SELECT
- Filtrer avec WHERE
- Relier des tables avec INNER JOIN
- Conserver toutes les lignes avec LEFT JOIN
- Compter par groupe avec GROUP BY
- Tester une plage ou une valeur absente

## UML — question 1 — SIL PDF · mercredi · UML

### Énoncé / tâche associée
QCM covoiturage : (a) définition d’un acteur ; (b) sens de include ; (c) diagramme des messages chronologiques ; (d) sens de 0..* côté Trajet.

### Niveau 1 — réponse minimale
(a) B : entité externe interagissant avec le système

### Niveau 2 — réponse complète / solution type
(a) B : entité externe interagissant avec le système. (b) B : le comportement inclus est obligatoire. (c) C : diagramme de séquence. (d) C : un conducteur peut publier zéro, un ou plusieurs trajets.

### Niveau 3 — explication pédagogique
« Include » réutilise obligatoirement un comportement commun ; « extend » est optionnel.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 2 — SIL PDF · mercredi · UML

### Énoncé / tâche associée
Associe : trajet publié par un conducteur exact ; conducteur publie zéro ou plusieurs trajets ; trajet a au moins une étape ; réservation a au plus une note. Multiplicités A 0..1, B 1, C 0..*, D 1..*.

### Niveau 1 — réponse minimale
1 → B (1 conducteur par trajet)

### Niveau 2 — réponse complète / solution type
1 → B (1 conducteur par trajet). 2 → C (0..* trajets). 3 → D (1..* étapes). 4 → A (0..1 note).

### Niveau 3 — explication pédagogique
La note est facultative et au plus une par réservation.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 3 — SIL PDF · mercredi · UML

### Énoncé / tâche associée
Vrai ou faux : (1) en composition la partie ne survit pas au tout ; (2) une classe abstraite s’instancie directement ; (3) « - » signifie privé ; (4) un diagramme d’activités décrit la structure statique.

### Niveau 1 — réponse minimale
(1) Vrai

### Niveau 2 — réponse complète / solution type
(1) Vrai. (2) Faux : on instancie une sous-classe concrète. (3) Vrai. (4) Faux : un diagramme de classes décrit la structure ; activités décrit le flux de travail.

### Niveau 3 — explication pédagogique
La composition exprime une dépendance de cycle de vie entre partie et tout.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 4 — SIL PDF · mercredi · UML

### Énoncé / tâche associée
Identifie les acteurs de la plateforme de covoiturage et propose cinq cas d’utilisation.

### Niveau 1 — réponse minimale
Acteurs : Conducteur, Passager, Administrateur

### Niveau 2 — réponse complète / solution type
Acteurs : Conducteur, Passager, Administrateur. Cas : créer compte, publier trajet, rechercher trajet, réserver place, annuler réservation, noter conducteur, valider compte conducteur, suspendre compte.

### Niveau 3 — explication pédagogique
Un cas d’utilisation décrit un objectif du système vu par un acteur externe.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 5 — SIL PDF · mercredi · UML

### Énoncé / tâche associée
Décris les classes Conducteur, Passager, Trajet, Reservation avec attributs typés/visibilités, associations, multiplicités et stockage de la note.

### Niveau 1 — réponse minimale
Conducteur(-id:int,-nom:String,-email:String) 1—0..* Trajet(-depart:String,-destination:String,-date:Date,-prixPlace:Decimal,-places:int)

### Niveau 2 — réponse complète / solution type
Conducteur(-id:int,-nom:String,-email:String) 1—0..* Trajet(-depart:String,-destination:String,-date:Date,-prixPlace:Decimal,-places:int). Passager(-id:int,-nom:String,-email:String) 1—0..* Reservation(-date:Date,-nbPlaces:int,-note:Integer?). Trajet 1—0..* Reservation. Chaque réservation lie exactement un passager et un trajet ; note nullable, 0..1 par réservation.

### Niveau 3 — explication pédagogique
Reservation est la classe d’association entre passager et trajet et porte la note après le trajet.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Modéliser une relation plusieurs-à-plusieurs

## Réseaux — question 1 — SIL PDF · mercredi · réseau

### Énoncé / tâche associée
QCM réseau : (a) équipement reliant réseaux différents ; (b) hôtes utilisables d’un /27 ; (c) adresse IPv4 privée ; (d) port UDP DHCP.

### Niveau 1 — réponse minimale
(a) C : routeur

### Niveau 2 — réponse complète / solution type
(a) C : routeur. (b) B : 30. (c) C : 192.168.20.7. (d) B : port serveur UDP 67 (client UDP 68).

### Niveau 3 — explication pédagogique
Un /27 fournit 32 adresses totales, soit 30 hôtes classiques ; 192.168.0.0/16 est privé.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — SIL PDF · mercredi · réseau

### Énoncé / tâche associée
Associe HTTPS, DNS, SSH, SMTP et FTP contrôle à leurs ports par défaut.

### Niveau 1 — réponse minimale
HTTPS 443 ; DNS 53 ; SSH 22 ; SMTP 25 ; FTP contrôle 21.

### Niveau 2 — réponse complète / solution type
HTTPS 443 ; DNS 53 ; SSH 22 ; SMTP 25 ; FTP contrôle 21.

### Niveau 3 — explication pédagogique
Le FTP de contrôle utilise 21 ; le canal de données dépend du mode actif/passif.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — SIL PDF · mercredi · réseau

### Énoncé / tâche associée
Classe les étapes DHCP : Request, Discover, Acknowledge, Offer.

### Niveau 1 — réponse minimale
Discover → Offer → Request → Acknowledge (DORA).

### Niveau 2 — réponse complète / solution type
Discover → Offer → Request → Acknowledge (DORA).

### Niveau 3 — explication pédagogique
Le serveur propose un bail après découverte ; le client le demande puis le serveur confirme.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Reconnaître une panne DHCP avec DORA

## Réseaux — question 4 — SIL PDF · mercredi · réseau

### Énoncé / tâche associée
VLSM depuis 192.168.20.0/24 : Administration 50 postes, salle informatique 25, bibliothèque 10. Donne préfixe, masque, réseau, hôtes et broadcast.

### Niveau 1 — réponse minimale
Administration : /26, 255.255.255.192, .0, hôtes .1–.62, broadcast .63

### Niveau 2 — réponse complète / solution type
Administration : /26, 255.255.255.192, .0, hôtes .1–.62, broadcast .63. Salle : /27, 255.255.255.224, .64, hôtes .65–.94, broadcast .95. Bibliothèque : /28, 255.255.255.240, .96, hôtes .97–.110, broadcast .111.

### Niveau 3 — explication pédagogique
VLSM alloue les plus grands besoins d’abord ; ces trois plages ne se chevauchent pas.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 5 — SIL PDF · mercredi · réseau

### Énoncé / tâche associée
Un poste de salle communique avec son réseau local mais ni avec les serveurs d’administration ni Internet. Propose cinq étapes de diagnostic et commandes.

### Niveau 1 — réponse minimale
1) Vérifier câble/Wi-Fi et lien du switch

### Niveau 2 — réponse complète / solution type
1) Vérifier câble/Wi-Fi et lien du switch. 2) ipconfig /all : IP, masque, passerelle, DHCP. 3) ping 127.0.0.1 puis ping sa propre IP. 4) ping un pair puis la passerelle ; contrôler VLAN, masque et route. 5) ping une IP externe puis nslookup un nom ; diagnostiquer routage/pare-feu ou DNS selon le résultat.

### Niveau 3 — explication pédagogique
Procéder du lien physique vers IP locale, passerelle, Internet par IP, puis résolution DNS.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Diagnostiquer une perte de connectivité

## Java — question 1 — SIL PDF · mercredi · Java

### Énoncé / tâche associée
QCM Java : (a) mot-clé pour créer un objet ; (b) accès à private ; (c) constructeur ; (d) héritage de classe.

### Niveau 1 — réponse minimale
(a) B : new

### Niveau 2 — réponse complète / solution type
(a) B : new. (b) B : dans la classe qui déclare le membre, via son interface publique ailleurs. (c) A : même nom que la classe, aucun type de retour. (d) B : extends.

### Niveau 3 — explication pédagogique
implements sert aux interfaces ; un constructeur initialise l’objet créé par new.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Choisir public, private ou protected
- Déclarer et implémenter une interface

## Java — question 2 — SIL PDF · mercredi · Java

### Énoncé / tâche associée
Vrai ou faux : (1) plusieurs constructeurs avec paramètres différents ; (2) main doit être non statique ; (3) int et double sont des classes ; (4) chaque objet a ses valeurs d’attributs.

### Niveau 1 — réponse minimale
(1) Vrai : surcharge de constructeur

### Niveau 2 — réponse complète / solution type
(1) Vrai : surcharge de constructeur. (2) Faux : point d’entrée classique public static void main(String[] args). (3) Faux : int et double sont des types primitifs. (4) Vrai pour les attributs d’instance.

### Niveau 3 — explication pédagogique
Les champs static sont partagés par la classe, contrairement aux champs d’instance.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Java — question 3 — SIL PDF · mercredi · Java

### Énoncé / tâche associée
Complète : visibilité de reference ; nom du constructeur ; objet courant pour affecter reference.

### Niveau 1 — réponse minimale
private String reference; public Produit(String reference,double prix) { this.reference = reference; this.prix = prix; } Les trois réponses : private ; Produit ; this.

### Niveau 2 — réponse complète / solution type
private String reference; public Produit(String reference,double prix) { this.reference = reference; this.prix = prix; } Les trois réponses : private ; Produit ; this.

### Niveau 3 — explication pédagogique
this distingue le champ d’instance du paramètre portant le même nom.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer un attribut
- Écrire un constructeur

## Java — question 4 — SIL PDF · mercredi · Java

### Énoncé / tâche associée
Pour i de 1 à 5, ajoute i à somme si i est pair, sinon soustrais 1. Qu’affiche le programme ?

### Niveau 1 — réponse minimale
Initial somme=0 : i=1 → -1 ; i=2 → 1 ; i=3 → 0 ; i=4 → 4 ; i=5 → 3

### Niveau 2 — réponse complète / solution type
Initial somme=0 : i=1 → -1 ; i=2 → 1 ; i=3 → 0 ; i=4 → 4 ; i=5 → 3. Le programme affiche 3.

### Niveau 3 — explication pédagogique
Les valeurs paires ajoutent 2 puis 4 ; les trois valeurs impaires retranchent 1 chacune.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Java — question 5 — SIL PDF · mercredi · Java

### Énoncé / tâche associée
Écris une classe Produit encapsulée (référence, désignation, prix, quantité), valeurStock(), estEnRupture(), puis un exemple de main avec deux produits.

### Niveau 1 — réponse minimale
class Produit { private String reference, designation; private double prixUnitaire; private int quantite; public Produit(String r,String d,double p,int q){reference=r;designation=d;prixUnitaire=p;quantite=q;} public double valeurStock(){return prixUnitaire*quantite;} public boolean estEnRupture(){return quantite==0;} public String getDesignation(){return designation;} } Dans main, créer deux Produit, afficher getDesignation(), valeurStock() et estEnRupture().

### Niveau 2 — réponse complète / solution type
```java
class Produit { private String reference, designation; private double prixUnitaire; private int quantite; public Produit(String r,String d,double p,int q){reference=r;designation=d;prixUnitaire=p;quantite=q;} public double valeurStock(){return prixUnitaire*quantite;} public boolean estEnRupture(){return quantite==0;} public String getDesignation(){return designation;} } Dans main, créer deux Produit, afficher getDesignation(), valeurStock() et estEnRupture().
```

### Niveau 3 — explication pédagogique
En production, valider prix/quantité et préférer BigDecimal aux double pour les montants.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer une classe
- Écrire une méthode
- Créer un objet et appeler une méthode
- Appliquer l’encapsulation
