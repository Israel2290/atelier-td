# Épreuve de spécialité SIL — Mercredi

## Informations générales

- ID : EP-003
- Année : Non précisée dans le document original.
- Session : Mercredi
- Matière : Spécialité SIL
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Barème par question/sous-question présent dans la source et conservé dans la transcription ; total global non précisé.
- Source : `Epreuve_Specialite_SIL_MERCREDI.docx` (DOCX)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

# Cours

## 1. Comprendre la matière

L’épreuve porte sur un système hôtelier. Elle demande de relier des clients, chambres, réservations et paiements en SQL/UML, de segmenter un réseau d’hôtel et d’écrire des classes Java.

## 2. Notions essentielles

### Base de données d’un hôtel
`CLIENT`, `CHAMBRE`, `RESERVATION` et `PAIEMENT` ont chacune une clé primaire. Une réservation porte les clés étrangères du client et de la chambre ; un paiement référence une réservation. `INNER JOIN` ne garde que les correspondances, `LEFT JOIN` conserve aussi les chambres sans réservation.

### UML
Un client réserve une chambre ; une réservation possède des dates, un statut et peut recevoir plusieurs paiements. Les cardinalités traduisent ces règles. Un scénario nominal décrit les étapes normales d’une réservation.

### Réseau d’hôtel
Séparer Administration, Services et Wi-Fi Clients en VLAN ou sous-réseaux. Le pare-feu contrôle les flux ; le Wi-Fi invité ne doit pas accéder aux serveurs internes. Le VLSM attribue `/25` à 80 postes, `/26` à 40 et `/27` à 20.

### Java
Une classe `Chambre` encapsule numéro, type, prix et état. `estDisponible()` teste l’état ; `calculerPrixSejour()` multiplie prix et nombre de nuits. `Suite extends Chambre` illustre l’héritage ; une référence `Chambre` contenant une `Suite` illustre le polymorphisme.

## 3. Méthodes pour résoudre les exercices

### Requêtes SQL
Suivre les chemins FK : client → réservation → chambre et réservation → paiement. Pour les chambres sans réservation, partir de `CHAMBRE` et utiliser `LEFT JOIN`. Pour un total, utiliser `SUM` et `GROUP BY`.

### VLSM et calcul CIDR
Trier les besoins par taille, calculer les blocs et noter réseau/hôtes/broadcast. Pour `192.168.60.34/27`, le pas est 32 : trouver le bloc qui contient 34.

### Java de réservation
Valider que le nombre de nuits est positif, utiliser `LocalDate` et calculer `ChronoUnit.DAYS.between(arrivee, depart)`. Écrire les méthodes d’accès seulement pour les attributs nécessaires.

## 4. Astuces et pièges à éviter

- `COUNT(IdReservation)` est préférable à `COUNT(*)` avec un `LEFT JOIN`.
- Le numéro de chambre n’est pas forcément un identifiant technique stable.
- Une VLAN invitée doit être filtrée par routage/pare-feu, pas seulement nommée.
- `Suite` doit appeler `super(...)` dans son constructeur.

## 5. Ce qu’il faut retenir

Les mêmes règles se répondent : PK/FK en SQL, associations en UML, VLAN/subnets en réseau et objets encapsulés en Java. Toujours justifier le choix avec la contrainte du sujet.
---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

# ÉPREUVE DE SPÉCIALITÉ – SIL

Licence – Systèmes Informatiques et Logiciels (SIL)

## CONSIGNES GÉNÉRALES

Lire attentivement chaque dossier avant de répondre.

Justifier les réponses lorsque cela est demandé.

Les schémas UML et réseau doivent être propres, lisibles et correctement légendés.

Les requêtes SQL doivent respecter une syntaxe correcte.

Les programmes Java doivent respecter les principes fondamentaux de la programmation orientée objet.

Toute réponse doit être présentée de manière claire et méthodique.

# DOSSIER 1 – BASES DE DONNÉES ET REQUÊTES SQL (5 POINTS)

Un hôtel souhaite informatiser la gestion de ses clients, de ses chambres, de ses réservations et des paiements.

Le système utilise les relations suivantes :

CLIENT (IdClient, Nom, Prenom, Telephone, Email)

CHAMBRE (IdChambre, Numero, TypeChambre, PrixNuit, Etat)

RESERVATION (IdReservation, DateArrivee, DateDepart, Statut, IdClient, IdChambre)

PAIEMENT (IdPaiement, DatePaiement, Montant, ModePaiement, IdReservation)

1. Identifier la clé primaire de chacune des quatre relations.

2. Identifier les clés étrangères et préciser les relations qu’elles permettent d’établir.

3. Expliquer pourquoi le numéro de chambre ne doit pas nécessairement être utilisé comme clé primaire de la table CHAMBRE.

4. Écrire une requête SQL permettant d’afficher la liste des chambres actuellement disponibles (Etat = 'Disponible').

5. Écrire une requête permettant d’afficher le nom, le prénom, le numéro de chambre, la date d’arrivée et la date de départ des clients ayant effectué une réservation.

6. Écrire une requête permettant d’afficher les chambres dont le prix par nuit est compris entre 30 000 et 75 000 FCFA.

7. Écrire une requête permettant de calculer le montant estimé d’une réservation à partir du nombre de nuits et du prix de la chambre. Indiquer l’expression SQL utilisée pour calculer le nombre de nuits.

8. Écrire une requête permettant de connaître le nombre de réservations enregistrées pour chaque chambre.

9. Écrire une requête permettant d’afficher les clients ayant effectué au moins deux réservations.

10. Écrire une requête permettant d’afficher le montant total des paiements enregistrés pour chaque réservation.

11. Expliquer la différence entre INNER JOIN et LEFT JOIN et indiquer dans quel cas chacun pourrait être utilisé dans ce système.

# DOSSIER 2 – MODÉLISATION UML (5 POINTS)

La direction de l’hôtel souhaite disposer d’une application permettant aux clients de consulter les chambres, effectuer une réservation et consulter leur historique. La réception peut enregistrer les clients, confirmer ou annuler les réservations, enregistrer les paiements et signaler l’état des chambres. Le responsable de l’hôtel peut consulter des statistiques.

1. Identifier les acteurs principaux du système et préciser brièvement le rôle de chacun.

2. Donner au moins huit cas d’utilisation correspondant au fonctionnement de l’application.

3. Identifier les cas d’utilisation qui pourraient être inclus dans « Effectuer une réservation ».

4. Construire le diagramme de cas d’utilisation UML du système hôtelier.

5. Identifier au moins sept classes pertinentes pour la modélisation.

6. Pour les classes Client, Chambre, Reservation et Paiement, proposer au minimum quatre attributs pertinents.

7. Déterminer les associations entre Client, Chambre, Reservation et Paiement.

8. Proposer les cardinalités correspondant aux associations identifiées.

9. Réaliser un diagramme de classes UML cohérent du système.

10. Décrire textuellement le scénario nominal d’une réservation effectuée par un client.

# DOSSIER 3 – TÉLÉINFORMATIQUE ET RÉSEAUX (5 POINTS)

L’hôtel dispose d’une réception, d’un service administratif, d’un restaurant, de bureaux de gestion et d’un réseau Wi-Fi destiné aux clients. L’ensemble doit accéder à Internet, mais le Wi-Fi des clients doit être isolé du réseau interne de l’hôtel.

1. Proposer une architecture réseau adaptée à l’hôtel en faisant apparaître au minimum : Internet, routeur, pare-feu, switch, serveurs et points d’accès Wi-Fi.

2. Expliquer le rôle du pare-feu dans cette infrastructure.

3. Expliquer pourquoi il est nécessaire de séparer le réseau Wi-Fi des clients du réseau interne de l’hôtel.

4. Proposer une organisation logique en trois réseaux : réseau Administration, réseau Services de l’hôtel et réseau Wi-Fi Clients. Indiquer le principe de séparation utilisé.

5. Le réseau interne de l’hôtel est 192.168.60.0/24. Proposer trois sous-réseaux adaptés aux besoins suivants : Administration (20 postes), Services (40 postes), Wi-Fi Clients (80 postes). Pour chaque sous-réseau, donner l’adresse réseau, le masque, la première adresse utilisable, la dernière adresse utilisable et le broadcast.

6. Un ordinateur de la réception possède l’adresse 192.168.60.34/27. Déterminer son adresse réseau et son adresse de broadcast.

7. Expliquer le rôle de DHCP dans l’attribution des paramètres réseau aux postes et aux appareils Wi-Fi.

8. Le serveur de réservation est accessible depuis le réseau interne mais pas depuis le réseau Wi-Fi des clients. Donner deux raisons techniques possibles expliquant cette situation.

9. Un terminal de la réception n’accède plus au serveur de l’hôtel. Proposer une procédure de diagnostic allant de la vérification physique jusqu’aux tests réseau.

10. Expliquer la différence entre DNS et DHCP et donner un exemple d’utilisation de chacun dans l’hôtel.

# DOSSIER 4 – PROGRAMMATION JAVA / POO (5 POINTS)

On souhaite développer une application Java pour gérer les chambres et les réservations d’un hôtel.

Une chambre possède un numéro, un type, un prix par nuit et un état. Une réservation possède une référence, une date d’arrivée, une date de départ et un statut.

1. Expliquer les notions suivantes : classe, objet, attribut, méthode et constructeur.

2. Déclarer une classe Chambre avec les attributs appropriés. Utiliser l’encapsulation.

3. Écrire un constructeur permettant d’initialiser une chambre.

4. Écrire les méthodes d’accès (getters/setters) nécessaires.

5. Écrire une méthode estDisponible() retournant true si l’état de la chambre est « Disponible » et false dans le cas contraire.

6. Écrire une méthode calculerPrixSejour(int nombreNuits) permettant de calculer le coût d’un séjour.

7. Déclarer une classe Reservation contenant au minimum une référence, une Chambre, une date d’arrivée, une date de départ et un statut.

8. Écrire une méthode permettant de calculer le nombre de nuits à partir des dates d’arrivée et de départ.

9. Écrire un programme principal permettant de créer deux chambres, d’afficher leurs informations et de calculer le prix d’un séjour pour chacune.

10. Créer une classe Suite qui hérite de Chambre et ajouter un attribut spécifique permettant de préciser le nombre de personnes pouvant être accueillies.

11. Expliquer et illustrer, dans ce contexte, les notions d’héritage et de redéfinition de méthode.

12. Indiquer un exemple de polymorphisme pouvant être utilisé entre Chambre et Suite.
