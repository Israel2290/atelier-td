# Corrigé type — Épreuve de spécialité SIL — Jeudi

- Identifiant : EP-004
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Bases de données — question 1 — SIL PDF · jeudi · SQL

### Énoncé / tâche associée
QCM clinique : (a) rôle de CONSULTATION.IdPatient ? (b) pourquoi ON DELETE RESTRICT refuse la suppression du patient 7 ? (c) agrégat des tarifs ? (d) résultat d’un INNER JOIN MEDECIN–CONSULTATION ?

### Niveau 1 — réponse minimale
(a) B : clé étrangère vers PATIENT

### Niveau 2 — réponse complète / solution type
(a) B : clé étrangère vers PATIENT. (b) B : des consultations référencent ce patient. (c) C : SUM. (d) B : uniquement les médecins ayant au moins une consultation.

### Niveau 3 — explication pédagogique
Une clé étrangère lie les tables ; RESTRICT protège les lignes référencées ; INNER JOIN ne conserve que les correspondances.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Compter par groupe avec GROUP BY
- Filtrer les groupes avec HAVING
- Calculer SUM, AVG, MIN et MAX

## Bases de données — question 2 — SIL PDF · jeudi · SQL

### Énoncé / tâche associée
Vrai ou faux : (1) SERVICE est mère de MEDECIN ; (2) WHERE filtre les groupes ; (3) COUNT(*) compte les lignes même si certaines colonnes sont NULL ; (4) une clé étrangère peut référencer une valeur mère inexistante.

### Niveau 1 — réponse minimale
(1) Vrai

### Niveau 2 — réponse complète / solution type
(1) Vrai. (2) Faux : HAVING filtre les groupes, WHERE filtre avant regroupement. (3) Vrai. (4) Faux : cela viole l’intégrité référentielle (sauf NULL autorisé).

### Niveau 3 — explication pédagogique
COUNT(*) compte les lignes ; COUNT(colonne) ignore les NULL de cette colonne.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Repérer PK, FK et table mère/fille

## Bases de données — question 3 — SIL PDF · jeudi · SQL

### Énoncé / tâche associée
Complète la requête qui sélectionne les médecins ayant plus de 5 consultations : SELECT m.Nom, COUNT(c.IdConsultation) AS nb FROM MEDECIN m ___ JOIN CONSULTATION c ON m.IdMedecin=c.IdMedecin ___ BY m.IdMedecin,m.Nom ___ COUNT(c.IdConsultation)>5.

### Niveau 1 — réponse minimale
LEFT (ou INNER) JOIN ; GROUP ; HAVING

### Niveau 2 — réponse complète / solution type
LEFT (ou INNER) JOIN ; GROUP ; HAVING. Une version : SELECT m.Nom, COUNT(c.IdConsultation) AS nb FROM MEDECIN m LEFT JOIN CONSULTATION c ON m.IdMedecin=c.IdMedecin GROUP BY m.IdMedecin,m.Nom HAVING COUNT(c.IdConsultation)>5;

### Niveau 3 — explication pédagogique
HAVING filtre l’agrégat COUNT après GROUP BY ; LEFT JOIN conserve aussi les médecins sans consultation, mais ils ne satisfont pas >5.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Bases de données — question 4 — SIL PDF · jeudi · SQL

### Énoncé / tâche associée
Classe les clauses SQL : ORDER BY, WHERE, SELECT, HAVING, FROM, GROUP BY.

### Niveau 1 — réponse minimale
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY.

### Niveau 2 — réponse complète / solution type
```sql
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY.
```

### Niveau 3 — explication pédagogique
WHERE filtre les lignes avant le groupement ; HAVING filtre les groupes après.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Compter par groupe avec GROUP BY
- Filtrer les groupes avec HAVING
- Trier et supprimer les doublons

## Bases de données — question 5 — SIL PDF · jeudi · SQL

### Énoncé / tâche associée
Clinique : (a) médecins de Pédiatrie ; (b) total des tarifs par médecin ; (c) patients jamais consultés.

### Niveau 1 — réponse minimale
(a) SELECT m.Nom,m.Specialite FROM MEDECIN m JOIN SERVICE s ON s.IdService=m.IdService WHERE s.NomService='Pédiatrie'; (b) SELECT m.Nom,SUM(c.Tarif) AS total FROM MEDECIN m JOIN CONSULTATION c ON c.IdMedecin=m.IdMedecin GROUP BY m.IdMedecin,m.Nom; (c) SELECT p.Nom,p.Prenom FROM PATIENT p LEFT JOIN CONSULTATION c ON c.IdPatient=p.IdPatient WHERE c.IdConsultation IS NULL;

### Niveau 2 — réponse complète / solution type
(a) SELECT m.Nom,m.Specialite FROM MEDECIN m JOIN SERVICE s ON s.IdService=m.IdService WHERE s.NomService='Pédiatrie'; (b) SELECT m.Nom,SUM(c.Tarif) AS total FROM MEDECIN m JOIN CONSULTATION c ON c.IdMedecin=m.IdMedecin GROUP BY m.IdMedecin,m.Nom; (c) SELECT p.Nom,p.Prenom FROM PATIENT p LEFT JOIN CONSULTATION c ON c.IdPatient=p.IdPatient WHERE c.IdConsultation IS NULL;

### Niveau 3 — explication pédagogique
LEFT JOIN suivi de IS NULL est une méthode classique pour trouver les lignes sans correspondance.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Lire des données avec SELECT
- Filtrer avec WHERE
- Relier des tables avec INNER JOIN
- Compter par groupe avec GROUP BY
- Calculer SUM, AVG, MIN et MAX

## UML — question 1 — SIL PDF · jeudi · UML

### Énoncé / tâche associée
QCM UML commandes : (a) signe + devant un attribut ; (b) rôle de « extend » ; (c) diagramme des états d’une commande ; (d) multiplicité côté Client quand chaque commande a un client.

### Niveau 1 — réponse minimale
(a) B : visibilité publique

### Niveau 2 — réponse complète / solution type
(a) B : visibilité publique. (b) A : comportement facultatif qui étend le cas de base. (c) B : diagramme d’états-transitions. (d) B : 1 client par commande.

### Niveau 3 — explication pédagogique
La multiplicité lue du côté Client décrit le nombre de clients associés à une commande.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 2 — SIL PDF · jeudi · UML

### Énoncé / tâche associée
Associe : commande passée par exactement un client ; client avec zéro ou plusieurs commandes ; commande contenant au moins un plat ; au plus un livreur. Multiplicités : A 1..*, B 0..1, C 1, D 0..*.

### Niveau 1 — réponse minimale
1 → C (1 client)

### Niveau 2 — réponse complète / solution type
1 → C (1 client). 2 → D (0..* commandes). 3 → A (1..* plats). 4 → B (0..1 livreur).

### Niveau 3 — explication pédagogique
Chaque multiplicité se lit depuis l’objet opposé dans l’association.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 3 — SIL PDF · jeudi · UML

### Énoncé / tâche associée
Vrai ou faux : (1) héritage : triangle creux dirigé de fille vers mère ; (2) une association plusieurs-à-plusieurs Commande–Plat peut devenir une classe LigneCommande ; (3) un acteur est toujours une personne ; (4) le diagramme de séquence montre la structure statique des classes.

### Niveau 1 — réponse minimale
(1) Vrai

### Niveau 2 — réponse complète / solution type
(1) Vrai. (2) Vrai. (3) Faux : un acteur peut être un système externe ou un rôle. (4) Faux : le diagramme de classes décrit la structure statique ; la séquence décrit les échanges temporels.

### Niveau 3 — explication pédagogique
LigneCommande porte notamment quantité et prix au moment de la commande.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 4 — SIL PDF · jeudi · UML

### Énoncé / tâche associée
Identifie les acteurs de la commande de repas et propose au moins cinq cas d’utilisation reliés aux acteurs.

### Niveau 1 — réponse minimale
Acteurs : Client (consulter menu, commander, payer, suivre commande), Restaurant/restaurateur (gérer menu, accepter commande), Livreur (prendre et livrer commande), Administrateur (superviser)

### Niveau 2 — réponse complète / solution type
Acteurs : Client (consulter menu, commander, payer, suivre commande), Restaurant/restaurateur (gérer menu, accepter commande), Livreur (prendre et livrer commande), Administrateur (superviser). Cas : consulter menu, passer commande, payer, suivre livraison, gérer menu, accepter/refuser commande, livrer, administrer.

### Niveau 3 — explication pédagogique
Les acteurs sont externes au système ; les cas d’utilisation décrivent des objectifs observables.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## UML — question 5 — SIL PDF · jeudi · UML

### Énoncé / tâche associée
Propose le diagramme de classes de la commande de repas avec Client, Commande, Plat, Restaurant, Livreur et LigneCommande ; trois attributs typés par classe et cardinalités.

### Niveau 1 — réponse minimale
Client(id:int, nom:String, email:String) 1—0..* Commande(id:int,date:Date,statut:String)

### Niveau 2 — réponse complète / solution type
Client(id:int, nom:String, email:String) 1—0..* Commande(id:int,date:Date,statut:String). Commande 1—1..* LigneCommande(quantite:int,prixUnitaire:Decimal) *—1 Plat(id:int,nom:String,prix:Decimal). Restaurant(id:int,nom:String,adresse:String) 1—0..* Plat. Livreur(id:int,nom:String,telephone:String) 0..1—0..* Commande (une commande au plus un livreur ; un livreur peut livrer plusieurs commandes). La quantité appartient à LigneCommande.

### Niveau 3 — explication pédagogique
La classe d’association résout le plusieurs-à-plusieurs Commande–Plat et stocke la quantité commandée.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Modéliser une relation plusieurs-à-plusieurs

## Réseaux — question 1 — SIL PDF · jeudi · réseau

### Énoncé / tâche associée
QCM : (a) rôle du switch ; (b) hôtes utilisables d’un /26 ; (c) résolution nom-IP ; (d) commande Windows de chemin réseau.

### Niveau 1 — réponse minimale
(a) B : commute selon MAC

### Niveau 2 — réponse complète / solution type
(a) B : commute selon MAC. (b) B : 62. (c) B : DNS. (d) C : tracert.

### Niveau 3 — explication pédagogique
Un /26 laisse 6 bits hôte, donc 64 adresses dont 2 réservées.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — SIL PDF · jeudi · réseau

### Énoncé / tâche associée
Associe switch, routeur, TCP, HTTP et câble RJ45 aux couches OSI 1, 2, 3, 4, 7.

### Niveau 1 — réponse minimale
Switch : couche 2

### Niveau 2 — réponse complète / solution type
Switch : couche 2. Routeur : couche 3. TCP : couche 4. HTTP : couche 7. Câble : couche 1.

### Niveau 3 — explication pédagogique
Les équipements/protocoles sont associés à la couche où se situe leur fonction principale.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — SIL PDF · jeudi · réseau

### Énoncé / tâche associée
Classe l’encapsulation d’une donnée émise par une application : trame, segment, bits, paquet, données.

### Niveau 1 — réponse minimale
Données → segment → paquet → trame → bits.

### Niveau 2 — réponse complète / solution type
Données → segment → paquet → trame → bits.

### Niveau 3 — explication pédagogique
À l’émission, chaque couche ajoute ses informations ; à la réception, l’ordre est inversé.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 4 — SIL PDF · jeudi · réseau

### Énoncé / tâche associée
VLSM depuis 192.168.50.0/24 : Technique 60 postes, Commercial 28, Comptabilité 20, Direction 10. Donne préfixe, masque, réseau, première/dernière IP et broadcast.

### Niveau 1 — réponse minimale
Technique : /26, 255.255.255.192, réseau .0, hôtes .1–.62, broadcast .63

### Niveau 2 — réponse complète / solution type
Technique : /26, 255.255.255.192, réseau .0, hôtes .1–.62, broadcast .63. Commercial : /27, 255.255.255.224, réseau .64, hôtes .65–.94, broadcast .95. Comptabilité : /27, réseau .96, hôtes .97–.126, broadcast .127. Direction : /28, 255.255.255.240, réseau .128, hôtes .129–.142, broadcast .143.

### Niveau 3 — explication pédagogique
Allouer du plus grand au plus petit. Capacités : /26=62, /27=30, /27=30, /28=14 hôtes.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 5 — SIL PDF · jeudi · réseau

### Énoncé / tâche associée
Comptabilité reçoit 169.254.x.x. Que signifie cette adresse et quelles trois vérifications faire dans l’ordre ?

### Niveau 1 — réponse minimale
C’est une adresse APIPA/link-local, souvent attribuée parce que le client n’a pas reçu de bail DHCP

### Niveau 2 — réponse complète / solution type
C’est une adresse APIPA/link-local, souvent attribuée parce que le client n’a pas reçu de bail DHCP. Vérifier : (1) câble/lien et VLAN ; (2) configuration IP et portée DHCP (ipconfig /all, renouveler ipconfig /release puis /renew) ; (3) serveur/relai DHCP, connectivité et journaux (ping, tests depuis un autre poste).

### Niveau 3 — explication pédagogique
Une adresse 169.254/16 permet seulement une connectivité locale limitée ; elle ne prouve pas à elle seule la cause exacte.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Reconnaître une panne DHCP avec DORA
- Diagnostiquer une perte de connectivité

## Java — question 1 — SIL PDF · jeudi · Java

### Énoncé / tâche associée
QCM : (a) résultat de 7/2 en Java ; (b) boucle garantie au moins une fois ; (c) encapsulation ; (d) mot-clé de l’objet courant.

### Niveau 1 — réponse minimale
(a) B : 3 (division entière)

### Niveau 2 — réponse complète / solution type
(a) B : 3 (division entière). (b) C : do…while. (c) B : masquer l’état et l’exposer par des méthodes contrôlées. (d) B : this.

### Niveau 3 — explication pédagogique
Comme les deux opérandes sont int, 7/2 tronque la partie décimale.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Java — question 2 — SIL PDF · jeudi · Java

### Énoncé / tâche associée
Vrai ou faux : (1) void ne retourne pas de valeur ; (2) une fille hérite des membres publics de la mère ; (3) == compare le contenu des String ; (4) la taille d’un tableau Java est modifiable.

### Niveau 1 — réponse minimale
(1) Vrai

### Niveau 2 — réponse complète / solution type
(1) Vrai. (2) Vrai, sous réserve des règles d’héritage et d’accès. (3) Faux : == compare les références ; utiliser equals(). (4) Faux : la longueur du tableau est fixe après création.

### Niveau 3 — explication pédagogique
Pour comparer le texte, utiliser a.equals(b), en traitant éventuellement a == null.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Distinguer surcharge et redéfinition
- Comparer des chaînes Java

## Java — question 3 — SIL PDF · jeudi · Java

### Énoncé / tâche associée
Complète le code de deposer et getSolde : if (montant ___ 0) { solde ___ montant; } ; public double getSolde() { ___ solde; }

### Niveau 1 — réponse minimale
if (montant > 0) { solde += montant; } ; public double getSolde() { return solde; }

### Niveau 2 — réponse complète / solution type
if (montant > 0) { solde += montant; } ; public double getSolde() { return solde; }

### Niveau 3 — explication pédagogique
Le dépôt doit être strictement positif ; += ajoute le montant et return renvoie le solde.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Écrire un getter
- Écrire une méthode

## Java — question 4 — SIL PDF · jeudi · Java

### Énoncé / tâche associée
Pour t={4,7,2,9}, le programme initialise max=t[0] et remplace max par chaque t[i] supérieur. Qu’affiche-t-il et quel est son rôle ?

### Niveau 1 — réponse minimale
Il affiche 9

### Niveau 2 — réponse complète / solution type
Il affiche 9. Il parcourt le tableau et mémorise la plus grande valeur rencontrée.

### Niveau 3 — explication pédagogique
L’invariant est que max contient le maximum des éléments déjà parcourus.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Parcourir un tableau et trouver son maximum

## Java — question 5 — SIL PDF · jeudi · Java

### Énoncé / tâche associée
Écris une classe CompteBancaire (numéro, titulaire, solde), dépôt positif, retrait refusé si solde insuffisant, puis un main qui teste les opérations.

### Niveau 1 — réponse minimale
class CompteBancaire { private String numero, titulaire; private double solde; public CompteBancaire(String n,String t,double s){numero=n;titulaire=t;solde=s;} public void deposer(double m){if(m>0) solde+=m;} public boolean retirer(double m){if(m<=0 || m>solde) return false; solde-=m; return true;} public double getSolde(){return solde;} } Dans main : créer un compte, appeler deposer(10000), retirer(3000), puis afficher getSolde() : 7000 si solde initial nul.

### Niveau 2 — réponse complète / solution type
```java
class CompteBancaire { private String numero, titulaire; private double solde; public CompteBancaire(String n,String t,double s){numero=n;titulaire=t;solde=s;} public void deposer(double m){if(m>0) solde+=m;} public boolean retirer(double m){if(m<=0 || m>solde) return false; solde-=m; return true;} public double getSolde(){return solde;} } Dans main : créer un compte, appeler deposer(10000), retirer(3000), puis afficher getSolde() : 7000 si solde initial nul.
```

### Niveau 3 — explication pédagogique
Valider les montants empêche dépôts/retraits négatifs. Utiliser BigDecimal plutôt que double pour des montants monétaires en production.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer une classe
- Écrire un constructeur
- Écrire une méthode
- Créer un objet et appeler une méthode
- Appliquer l’encapsulation
