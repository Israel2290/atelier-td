# Corrigé type — Épreuve de spécialité SIL — Mardi

- Identifiant : EP-002
- Statut de vérification : ⚠️ PARTIEL — réponses regroupées par dossier ; vérification détaillée des sous-questions et du barème à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Bases de données — question 1 — Spécialité · mardi · dossier 1

### Énoncé / tâche associée
Schéma CLIENT(IdClient,Nom,Prenom,Telephone,Ville), PRODUIT(IdProduit,Designation,Prix,Stock), COMMANDE(IdCommande,DateCommande,IdClient), LIGNE_COMMANDE(IdCommande,IdProduit,Quantite). Réponds aux 12 demandes : PK/FK/composite ; toutes clés ; clients de Cotonou ; produits >50 000 ; commandes avec client ; produits commandés/quantités ; montant de chaque ligne ; commandes par client ; stock <10 ; rôle GROUP BY ; différence WHERE/HAVING avec exemples.

### Niveau 1 — réponse minimale
PK identifie une ligne ; FK référence une autre table ; PK composée combine plusieurs colonnes

### Niveau 2 — réponse complète / solution type
PK identifie une ligne ; FK référence une autre table ; PK composée combine plusieurs colonnes. PK : IdClient, IdProduit, IdCommande, (IdCommande,IdProduit). FK : COMMANDE.IdClient→CLIENT ; LIGNE_COMMANDE.IdCommande→COMMANDE et IdProduit→PRODUIT. Les requêtes utilisent WHERE Ville='Cotonou', Prix>50000, JOIN CLIENT/COMMANDE, JOIN lignes/produits ; montant = Prix*Quantite ; COUNT(IdCommande) GROUP BY client ; stock<10. GROUP BY forme des groupes pour agrégats ; WHERE filtre les lignes avant groupe, HAVING filtre après (ex. HAVING COUNT(*)>2).

### Niveau 3 — explication pédagogique
La clé composée empêche deux lignes identiques pour un même produit et une même commande.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Lire des données avec SELECT
- Filtrer avec WHERE
- Relier des tables avec INNER JOIN
- Compter par groupe avec GROUP BY
- Filtrer les groupes avec HAVING
- Déclarer clés primaires et étrangères
- Repérer PK, FK et table mère/fille

## UML — question 1 — Spécialité · mardi · dossier 2

### Énoncé / tâche associée
Bibliothèque : étudiants recherchent, empruntent et rendent des ouvrages ; un ouvrage appartient à une catégorie ; un bibliothécaire enregistre prêts/retours. Donne acteurs, ≥8 cas, diagramme de cas, scénarios emprunter/rendre/rechercher, ≥6 classes, ≥4 attributs pour Etudiant/Ouvrage/Emprunt/Bibliothecaire, associations et cardinalités, diagramme de classes et rôle central d’Emprunt.

### Niveau 1 — réponse minimale
Acteurs : Étudiant, Bibliothécaire, éventuellement Administrateur

### Niveau 2 — réponse complète / solution type
Acteurs : Étudiant, Bibliothécaire, éventuellement Administrateur. Cas : rechercher/consulter ouvrage, emprunter, retourner, renouveler, consulter emprunts, gérer ouvrages/catégories, enregistrer adhérent, gérer retards. Scénario emprunt : rechercher disponibilité, identifier étudiant, vérifier quota, enregistrer Emprunt(dateDébut,dateRetourPrévue), marquer exemplaire indisponible. Retour : retrouver emprunt ouvert, enregistrer dateRetour, libérer exemplaire. Classes : Etudiant(id,nom,matricule,email), Ouvrage(id,titre,auteur,ISBN), Emprunt(id,dateEmprunt,dateRetour,statut), Bibliothecaire(id,nom,email), Categorie, Exemplaire. Étudiant 1—0..* Emprunt ; Ouvrage 1—0..* Emprunt ; Bibliothécaire 1—0..* Emprunt ; Catégorie 1—0..* Ouvrage. Emprunt porte les dates/statut reliant usager et ouvrage.

### Niveau 3 — explication pédagogique
Un exemplaire physique peut nécessiter une classe séparée si le même titre possède plusieurs copies.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Modéliser une relation plusieurs-à-plusieurs

## Réseaux — question 1 — Spécialité · mardi · dossier 3

### Énoncé / tâche associée
Définis IP/masque/passerelle/broadcast ; distingue switch/routeur ; propose architecture 3 services avec VLAN ; VLSM de 192.168.50.0/24 pour Administration 25, Comptabilité 15, Informatique 10 (plages complètes) ; explique passerelle/DHCP ; diagnostique 169.254, panne Internet malgré LAN (≥5 vérifications) ; distingue TCP/UDP.

### Niveau 1 — réponse minimale
IP identifie une interface ; masque délimite réseau/hôte ; passerelle route hors sous-réseau ; broadcast atteint tous les hôtes du sous-réseau

### Niveau 2 — réponse complète / solution type
IP identifie une interface ; masque délimite réseau/hôte ; passerelle route hors sous-réseau ; broadcast atteint tous les hôtes du sous-réseau. Switch commute des trames MAC ; routeur achemine entre réseaux IP. VLSM : Administration 25 → /27 .0–.31 (hôtes .1–.30, broadcast .31) ; Comptabilité 15 → /27 .32–.63 (hôtes .33–.62, broadcast .63) ; Informatique 10 → /28 .64–.79 (hôtes .65–.78, broadcast .79). Passerelle : sortie du réseau. DHCP : bail IP et paramètres. 169.254 indique souvent DHCP indisponible. Panne Internet : lien, IP/masque, ping loopback/passerelle, table routes, ping IP Internet, DNS/nslookup, pare-feu/FAI. TCP fiable/ordonné (web/fichiers), UDP faible latence (voix/DNS).

### Niveau 3 — explication pédagogique
Avec VLSM, /27 fournit 30 hôtes et /28 en fournit 14 ; allouer les plus grands besoins d’abord.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR
- Reconnaître une panne DHCP avec DORA
- Diagnostiquer une perte de connectivité

## Java — question 1 — Spécialité · mardi · dossier 4

### Énoncé / tâche associée
Employe(matricule, nom, prénom, salaire, service) : définis classe/objet/attribut/méthode/constructeur ; déclare la classe encapsulée, constructeur, getters/setters, afficherInformations(), augmenterSalaire(pourcentage), estCadre() si salaire ≥500 000 ; main avec trois employés ; Manager extends Employe ; exemple de polymorphisme ; surcharge vs redéfinition.

### Niveau 1 — réponse minimale
class Employe { private String matricule,nom,prenom,service; private double salaire; public Employe(String m,String n,String p,double s,String d){matricule=m;nom=n;prenom=p;salaire=s;service=d;} public double getSalaire(){return salaire;} public void setSalaire(double s){if(s>=0)salaire=s;} public void afficherInformations(){System.out.println(nom+" "+prenom+" "+salaire);} public void augmenterSalaire(double pct){if(pct>0)salaire*=1+pct/100;} public boolean estCadre(){return salaire>=500000;} } class Manager extends Employe { public Manager(...){super(...);} } Employe e=new Manager(...); surcharge : même nom/signatures différentes ; redéfinition : même signature héritée avec nouveau comportement (@Override).

### Niveau 2 — réponse complète / solution type
```java
class Employe { private String matricule,nom,prenom,service; private double salaire; public Employe(String m,String n,String p,double s,String d){matricule=m;nom=n;prenom=p;salaire=s;service=d;} public double getSalaire(){return salaire;} public void setSalaire(double s){if(s>=0)salaire=s;} public void afficherInformations(){System.out.println(nom+" "+prenom+" "+salaire);} public void augmenterSalaire(double pct){if(pct>0)salaire*=1+pct/100;} public boolean estCadre(){return salaire>=500000;} } class Manager extends Employe { public Manager(...){super(...);} } Employe e=new Manager(...); surcharge : même nom/signatures différentes ; redéfinition : même signature héritée avec nouveau comportement (@Override).
```

### Niveau 3 — explication pédagogique
Pour manipuler trois employés, créer une liste Employe[] contenant aussi des Manager puis appeler les méthodes redéfinies.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Déclarer une classe
- Déclarer un attribut
- Choisir public, private ou protected
- Écrire un constructeur
- Écrire un getter
- Écrire un setter
- Écrire une méthode
- Créer un objet et appeler une méthode
- Appliquer l’encapsulation
- Hériter avec extends
- Distinguer surcharge et redéfinition
