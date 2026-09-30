# Corrigé type — Épreuve de spécialité SIL — Mercredi

- Identifiant : EP-003
- Statut de vérification : ⚠️ PARTIEL — réponses regroupées par dossier ; vérification détaillée des sous-questions et du barème à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Bases de données — question 1 — Spécialité · mercredi · dossier 1

### Énoncé / tâche associée
Schéma hôtel : CLIENT(IdClient,Nom,Prenom,Telephone,Email), CHAMBRE(IdChambre,Numero,TypeChambre,PrixNuit,Etat), RESERVATION(IdReservation,DateArrivee,DateDepart,Statut,IdClient,IdChambre), PAIEMENT(IdPaiement,DatePaiement,Montant,ModePaiement,IdReservation). Réponds aux 11 questions : PK/FK, rôle de Numero, chambres disponibles, détails réservation/client/chambre, prix 30 000–75 000, coût du séjour, nombre de réservations par chambre, clients ≥2 réservations, total paiements, INNER vs LEFT JOIN.

### Niveau 1 — réponse minimale
PK : IdClient, IdChambre, IdReservation, IdPaiement

### Niveau 2 — réponse complète / solution type
PK : IdClient, IdChambre, IdReservation, IdPaiement. FK : RESERVATION.IdClient→CLIENT, IdChambre→CHAMBRE ; PAIEMENT.IdReservation→RESERVATION. Numero peut changer/se répéter selon site : IdChambre est stable. Disponible : SELECT * FROM CHAMBRE WHERE Etat='Disponible'. Réservations : joindre CLIENT→RESERVATION→CHAMBRE. Prix : WHERE PrixNuit BETWEEN 30000 AND 75000. Coût : DATEDIFF(DateDepart,DateArrivee)*PrixNuit (syntaxe selon SGBD). Réservations/chambre : LEFT JOIN + COUNT(IdReservation) + GROUP BY chambre. Clients ≥2 : GROUP BY client HAVING COUNT(*)>=2. Paiements : SUM(Montant) GROUP BY IdReservation. INNER garde les correspondances ; LEFT conserve toutes les lignes gauches.

### Niveau 3 — explication pédagogique
Pour inclure chambres ou clients sans réservation, utiliser LEFT JOIN et compter une clé non NULL de la table jointe.

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
- Calculer SUM, AVG, MIN et MAX
- Tester une plage ou une valeur absente
- Déclarer clés primaires et étrangères
- Modifier ou supprimer une ligne
- Repérer PK, FK et table mère/fille

## UML — question 1 — Spécialité · mercredi · dossier 2

### Énoncé / tâche associée
Hôtel : clients consultent chambres, réservent et voient leur historique ; réception gère clients/réservations/paiements/états ; responsable consulte statistiques. Donne acteurs, ≥8 cas, cas inclus dans réserver, ≥7 classes, 4 attributs pour Client/Chambre/Reservation/Paiement, associations/multiplicités, diagramme de classes et scénario nominal.

### Niveau 1 — réponse minimale
Acteurs : Client, Réceptionniste, Responsable

### Niveau 2 — réponse complète / solution type
Acteurs : Client, Réceptionniste, Responsable. Cas : consulter chambres, réserver, consulter historique, enregistrer client, confirmer/annuler réservation, enregistrer paiement, signaler état, consulter statistiques. Réserver peut inclure vérifier disponibilité, calculer prix, enregistrer réservation. Classes : Client, Chambre, Reservation, Paiement, TypeChambre, Employé, Facture. Client 1—0..* Réservation ; Chambre 1—0..* Réservation ; Réservation 1—0..* Paiement. Chaque Réservation référence 1 Client et 1 Chambre ; champs typiques : identifiants, coordonnées, numéro/type/prix/état, dates/statut, date/montant/mode. Scénario : rechercher dates, choisir chambre disponible, saisir données, valider disponibilité/prix, créer réservation, confirmer et notifier.

### Niveau 3 — explication pédagogique
Une réservation sert d’association historisée entre un client et une chambre sur une période.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 1 — Spécialité · mercredi · dossier 3

### Énoncé / tâche associée
Hôtel : dessine logiquement Internet, routeur, pare-feu, switch, serveurs, AP Wi-Fi ; explique pare-feu, séparation clients/interne et 3 réseaux/VLAN. Depuis 192.168.60.0/24, VLSM Administration 20, Services 40, Wi-Fi 80 avec détails complets ; calcule réseau/broadcast de 192.168.60.34/27 ; DHCP ; pourquoi serveur inaccessible depuis Wi-Fi ; procédure physique→réseau ; DNS vs DHCP.

### Niveau 1 — réponse minimale
Architecture : Internet→routeur/pare-feu→switch cœur→VLAN Administration/Services/Wi-Fi ; serveurs dans VLAN contrôlé, AP clients en VLAN isolé

### Niveau 2 — réponse complète / solution type
Architecture : Internet→routeur/pare-feu→switch cœur→VLAN Administration/Services/Wi-Fi ; serveurs dans VLAN contrôlé, AP clients en VLAN isolé. Pare-feu filtre flux ; isolation empêche les clients d’atteindre systèmes internes. VLSM plus grand d’abord : Wi-Fi 80 → /25 255.255.255.128, réseau .0, hôtes .1–.126, broadcast .127 ; Services 40 → /26 .128/26 masque .192, hôtes .129–.190, broadcast .191 ; Administration 20 → /27 .192/27 masque .224, hôtes .193–.222, broadcast .223. 192.168.60.34/27 : réseau .32, broadcast .63. DHCP distribue IP/masque/passerelle/DNS. Accès bloqué par ACL/pare-feu ou routage/VLAN. Diagnostic : alimentation/lien, ipconfig, ping loopback/passerelle, ping serveur par IP, tracert, DNS/nslookup, règles pare-feu. DNS résout noms ; DHCP attribue paramètres IP.

### Niveau 3 — explication pédagogique
La plage Wi-Fi /25, services /26 et administration /27 ne se chevauchent pas ; conserver une réserve d’adresses pour l’extension.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR
- Reconnaître une panne DHCP avec DORA
- Diagnostiquer une perte de connectivité

## Java — question 1 — Spécialité · mercredi · dossier 4

### Énoncé / tâche associée
Chambre avec attributs privés : explique classe/objet/attribut/méthode/constructeur ; écris Chambre encapsulée, constructeur, getters/setters, estDisponible(), calculerPrixSejour(nuits) ; Reservation avec chambre/dates/statut et calcul des nuits ; main avec deux chambres ; Suite extends Chambre avec capacité ; explique héritage, redéfinition et polymorphisme.

### Niveau 1 — réponse minimale
class Chambre { private String numero,type,etat; private double prixNuit; public Chambre(String n,String t,double p,String e){numero=n;type=t;prixNuit=p;etat=e;} public boolean estDisponible(){return "Disponible".equals(etat);} public double calculerPrixSejour(int nuits){if(nuits<0) throw new IllegalArgumentException(); return prixNuit*nuits;} public double getPrixNuit(){return prixNuit;} public String getEtat(){return etat;} public void setEtat(String e){etat=e;} } class Reservation { private String reference,statut; private Chambre chambre; private LocalDate arrivee,depart; public long nombreNuits(){return ChronoUnit.DAYS.between(arrivee,depart);} } class Suite extends Chambre { private int capacite; ..

### Niveau 2 — réponse complète / solution type
```java
class Chambre { private String numero,type,etat; private double prixNuit; public Chambre(String n,String t,double p,String e){numero=n;type=t;prixNuit=p;etat=e;} public boolean estDisponible(){return "Disponible".equals(etat);} public double calculerPrixSejour(int nuits){if(nuits<0) throw new IllegalArgumentException(); return prixNuit*nuits;} public double getPrixNuit(){return prixNuit;} public String getEtat(){return etat;} public void setEtat(String e){etat=e;} } class Reservation { private String reference,statut; private Chambre chambre; private LocalDate arrivee,depart; public long nombreNuits(){return ChronoUnit.DAYS.between(arrivee,depart);} } class Suite extends Chambre { private int capacite; ... } Créer deux chambres dans main puis afficher et calculer. Héritage : Suite réutilise Chambre ; redéfinition : @Override remplace un comportement ; polymorphisme : Chambre c=new Suite(...), appel dynamique de la méthode redéfinie.
```

### Niveau 3 — explication pédagogique
Utiliser LocalDate et ChronoUnit.DAYS ; une réservation valide doit avoir départ après arrivée.

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
- Comparer des chaînes Java
