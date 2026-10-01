import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = {
'EP-001': '''# Cours

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

La copie doit suivre l’ordre de la question : identifier, relier, calculer, puis justifier. Les quatre réflexes centraux sont PK/FK en SQL, cardinalités en UML, réseau/broadcast en IP et encapsulation en Java.''',
'EP-002': '''# Cours

## 1. Comprendre la matière

Cette épreuve travaille la conception d’une plateforme de formation : requêtes SQL, modèle UML, interconnexion de sites et programmation Java avec des étudiants.

## 2. Notions essentielles

### SQL
`SELECT` lit des colonnes, `WHERE` filtre, `JOIN` relie les tables et `GROUP BY` prépare un comptage par formation. Une table d’inscription contient les clés étrangères de l’étudiant et de la formation.

### UML de formation en ligne
Un étudiant peut suivre plusieurs cours et un cours plusieurs étudiants : il faut une association `Inscription`. Une évaluation appartient à un cours ; une note est liée à un étudiant et à une évaluation.

### Réseaux inter-sites
Un LAN couvre un site ; un WAN relie le siège aux agences. Le switch connecte localement, le routeur achemine entre sous-réseaux et DHCP distribue les paramètres. En VLSM, on réserve d’abord les blocs les plus grands.

### Java objet
Utiliser une classe `Etudiant` avec des attributs privés, un constructeur, une méthode d’affichage et `admis()`. L’encapsulation protège l’état ; l’héritage spécialise une classe ; le polymorphisme permet plusieurs implémentations derrière un type commun.

## 3. Méthodes pour résoudre les exercices

### Requête avec jointure
Commencer par la table contenant l’information demandée, écrire la clé de jointure, puis filtrer. Pour compter par formation, utiliser `COUNT(...)` et `GROUP BY`.

### VLSM
Calculer le nombre d’hôtes nécessaire, choisir `/26`, `/27`, `/28`, etc., puis attribuer les réseaux sans chevauchement. Pour chaque bloc, donner réseau, première IP, dernière IP et broadcast.

### Programme Java
Écrire les champs, initialiser dans le constructeur, afficher avec une méthode et retourner un booléen pour une condition. Dans `main`, tester au moins un étudiant admis et un étudiant ajourné.

## 4. Astuces et pièges à éviter

- Une association plusieurs-à-plusieurs nécessite une classe/table intermédiaire.
- Ne pas utiliser une passerelle pour masquer un mauvais masque.
- Une référence de classe fille doit respecter le constructeur parent.
- `moyenne >= 10` inclut exactement 10.

## 5. Ce qu’il faut retenir

Le chemin de résolution est : schéma relationnel → relations UML → adressage réseau → classe Java testable. Chaque réponse doit rester liée au vocabulaire de l’énoncé.''',
'EP-003': '''# Cours

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

Les mêmes règles se répondent : PK/FK en SQL, associations en UML, VLAN/subnets en réseau et objets encapsulés en Java. Toujours justifier le choix avec la contrainte du sujet.''',
'EP-004': '''# Cours

## 1. Comprendre la matière

Cette épreuve SIL mélange SQL clinique, UML d’une application de commandes, réseaux d’entreprise avec VLSM et Java appliqué à un compte bancaire.

## 2. Notions essentielles

### SQL et agrégats
Une FK pointe vers la PK d’une table mère. `SELECT` lit, `WHERE` filtre avant regroupement, `GROUP BY` forme les groupes, `HAVING` filtre les groupes et `SUM`/`COUNT` calculent des totaux. `LEFT JOIN ... IS NULL` trouve les lignes sans correspondance.

### UML de commande
Une commande appartient à un client et contient au moins un plat. La relation plusieurs-à-plusieurs Commande/Plat devient `LigneCommande`, qui porte notamment la quantité. Un acteur peut être un rôle ou un système externe.

### Réseaux et VLSM
Switch = couche 2, routeur = couche 3, TCP = couche 4, HTTP = couche 7, câble = couche 1. Encapsulation : données → segment → paquet → trame → bits. Pour 60, 28, 20 et 10 postes, choisir les blocs `/26`, `/27`, `/27`, `/28`.

### Java bancaire
Une classe bancaire encapsule numéro, titulaire et solde. Un dépôt valide le montant ; un retrait vérifie le solde. `7 / 2` vaut 3 en Java car les deux opérandes sont des entiers.

## 3. Méthodes pour résoudre les exercices

### SQL
Identifier le côté parent/enfant, puis construire la requête du plus simple au plus précis. Une question « plus de 5 consultations » demande `GROUP BY` puis `HAVING COUNT(...) > 5`.

### VLSM
Allouer le plus grand bloc d’abord. Déduire la taille par `2^bits_hôte`, puis inscrire chaque plage sans chevauchement. Une adresse `169.254.x.x` conduit à vérifier le DHCP.

### Java
Écrire la classe et ses invariants, puis les méthodes métier `deposer` et `retirer`. Analyser une boucle en notant la valeur de la variable à chaque tour.

## 4. Astuces et pièges à éviter

- `COUNT(*)` et `COUNT(colonne)` ne réagissent pas pareil aux NULL.
- `==` ne compare pas le contenu des `String`.
- Un tableau Java a une taille fixe après sa création.
- Ne pas confondre `this` et `super`.
- Un routeur, pas un switch, relie des réseaux IP différents.

## 5. Ce qu’il faut retenir

La copie attend des correspondances précises : clause SQL → étape de regroupement, élément UML → multiplicité, besoin réseau → préfixe, règle métier → méthode Java.''',
'EP-005': '''# Cours

## 1. Comprendre la matière

Cette épreuve utilise une bibliothèque, une plateforme de covoiturage, un établissement réseau et une boutique Java. Elle évalue les bases de données, UML, IPv4/DHCP et la POO.

## 2. Notions essentielles

### Bibliothèque et intégrité
Une table enfant porte une FK vers sa table mère. `ON DELETE RESTRICT` empêche de supprimer une ligne encore référencée. Une PK ne peut pas être NULL. L’ordre d’insertion suit les dépendances : parents puis enfants.

### UML
`include` signifie qu’un comportement est obligatoire dans le cas de base. Composition : la partie dépend du cycle de vie du tout. `-` signifie privé. Diagramme de classes = structure ; diagramme d’activités = flux ; séquence = messages dans le temps.

### Réseau scolaire
Routeur = liaison entre réseaux. `/26`, `/27` et `/28` se choisissent avec `2^h - 2`. DHCP suit Discover, Offer, Request, Acknowledge. Les ports usuels et les commandes `ping`, `tracert`, `ipconfig` servent au diagnostic.

### Java
`new` crée un objet, `private` protège un attribut, `extends` exprime l’héritage. Un constructeur porte le nom de la classe. Les types primitifs comme `int` et `double` ne sont pas des classes.

## 3. Méthodes pour résoudre les exercices

### SQL
Lire les relations, répondre aux QCM d’intégrité référentielle, puis écrire les requêtes avec `JOIN`, `GROUP BY`, `COUNT` et `IS NULL`. Pour les lignes jamais empruntées, utiliser une jointure gauche suivie d’un test NULL.

### UML
Traduire chaque phrase de l’énoncé en acteur, cas, classe ou multiplicité. Mettre la donnée propre à une relation dans la classe d’association.

### Réseau
DORA se mémorise dans l’ordre ; une IP APIPA est un symptôme DHCP. Pour une panne, partir du câble, de la configuration locale, de la passerelle, de l’IP distante puis du DNS.

### Java
Pour une analyse de code, simuler les variables ligne par ligne. Pour une classe, produire attributs privés, constructeur, getters/setters, méthodes métier puis `main`.

## 4. Astuces et pièges à éviter

- Une classe abstraite ne s’instancie pas directement.
- Une composition est plus forte qu’une simple association.
- `extends` n’est pas `implements`.
- Une adresse privée n’est pas routable directement sur Internet.

## 5. Ce qu’il faut retenir

Toujours distinguer structure, comportement et lien : table/clés en SQL, classes/cardinalités en UML, couches/ports en réseau et objets/méthodes en Java.''',
'EP-006': '''# Cours

## 1. Comprendre la matière

Le tronc commun du lundi couvre Web, architecture matérielle, réseaux et Excel. Les questions sont surtout rédactionnelles et demandent des définitions accompagnées d’un exemple.

## 2. Notions essentielles

### Web
Le client (navigateur) envoie une requête au serveur. Une URL contient protocole, hôte, port, chemin, paramètres et fragment. DNS traduit le nom en IP ; HTTPS ajoute le chiffrement TLS. HTML structure, CSS met en forme et JavaScript rend la page interactive.

### Architecture
Le processeur exécute les instructions ; la RAM est volatile ; ROM et stockage sont persistants. La carte mère relie les composants. Le démarrage passe par BIOS/UEFI, POST, chargeur puis noyau.

### Réseau
LAN/MAN/WAN décrivent la portée. Hub diffuse, switch commute des MAC, routeur achemine des IP. `/24` laisse 8 bits hôte ; réseau et broadcast sont réservés. DHCP attribue une configuration, DNS résout un nom.

### Excel
Classeur, feuille, cellule et plage sont les niveaux de base. Une référence relative se déplace ; `$A$1` est absolue. `SI`, `SOMME`, `MOYENNE`, `MAX`, `RECHERCHEV` et les tableaux croisés sont essentiels.

## 3. Méthodes pour résoudre les exercices

### Question théorique
Donner d’abord une définition courte, puis le rôle et un exemple concret. Pour une URL ou un démarrage, suivre l’ordre chronologique.

### Calcul réseau
Appliquer masque, réseau, broadcast et `2^(32-prefixe)-2` dans cet ordre.

### Formule Excel
Écrire le nom de fonction, les arguments et les guillemets autour des textes. Vérifier quelles références doivent rester fixes lors d’une recopie.

## 4. Astuces et pièges à éviter

- Internet n’est pas synonyme du Web.
- POST n’est pas un chiffrement : HTTPS reste nécessaire.
- RAM et stockage n’ont pas la même persistance.
- Un switch ne remplace pas un routeur entre réseaux.
- `SI` utilise des textes entre guillemets.

## 5. Ce qu’il faut retenir

Une bonne réponse de tronc commun suit le triplet définition → fonctionnement → exemple. Les formules et calculs doivent être écrits avec leurs bornes et unités.''',
'EP-007': '''# Cours

## 1. Comprendre la matière

Cette version b reprend les notions principales du tronc commun du lundi : Web, architecture, réseaux et Excel. Utiliser le contenu du sujet affiché et vérifier les différences de numérotation avec la version lundi.

## 2. Notions essentielles

Revoir client/serveur, URL, HTTP/HTTPS, HTML/CSS/JavaScript ; processeur, RAM, ROM, carte mère et démarrage ; LAN/MAN/WAN, OSI, DHCP/DNS et subnetting ; cellules Excel, références et fonctions `SI`, `SOMME`, `MOYENNE`, `MAX`, `RECHERCHEV`.

## 3. Méthodes pour résoudre les exercices

Pour une définition, écrire le sens puis un exemple. Pour un calcul IP, trouver masque, réseau, broadcast et plage. Pour Excel, vérifier les références absolues/relatives et les guillemets des textes. Comparer les notions par critères plutôt que par une phrase vague.

## 4. Astuces et pièges à éviter

- Cette version est proche du lundi mais doit être vérifiée séparément.
- Ne pas confondre HTTP avec HTTPS ni RAM avec stockage.
- `WHERE`/`HAVING` et réseau/broadcast sont des couples souvent confondus.

## 5. Ce qu’il faut retenir

Répondre avec une définition, une méthode courte et un exemple adapté aux données exactes de la version b.''',
'EP-008': '''# Cours

## 1. Comprendre la matière

Le mardi approfondit Web, architecture, réseaux et Excel avec DNS, sécurité Web, mémoire, protocoles, conversions, fonctions et graphiques.

## 2. Notions essentielles

DNS résout un nom en IP ; GET consulte et POST transmet des données ; cookies/sessions conservent un état. SQL injection et XSS sont des failles distinctes : requêtes préparées côté serveur, échappement de sortie côté affichage.

Le cycle processeur est fetch, decode, execute. La hiérarchie registres/cache/RAM/stockage équilibre vitesse et capacité. TCP garantit la livraison ; UDP privilégie la faible latence. Les quatre couches TCP/IP sont accès réseau, Internet, transport, application.

Excel : `NB`, `NBVAL`, `NB.SI`, `SOMME.SI`, `SI` imbriqué, mise en forme conditionnelle et graphiques. Une courbe montre une évolution ; un secteur montre des parts.

## 3. Méthodes pour résoudre les exercices

Comparer deux technologies avec critères, avantage et exemple. Pour les conversions, décomposer en puissances de 2 ou de 16. Pour une formule Excel, identifier plage, critère, valeur vraie et valeur fausse.

## 4. Astuces et pièges à éviter

- HTTPS protège le transport mais ne garantit pas l’honnêteté du site.
- TCP/UDP ne se différencient pas seulement par la vitesse : la fiabilité est le critère central.
- Une référence absolue utilise `$` devant ligne et colonne.
- Échapper les sorties n’est pas la même chose que valider les entrées.

## 5. Ce qu’il faut retenir

Pour chaque comparaison : définition, fonctionnement, cas d’usage et limite. Pour chaque formule : arguments, plage et résultat attendu.''',
'EP-009': '''# Cours

## 1. Comprendre la matière

Cette épreuve objective les bases Web, matérielles, réseau et Excel avec QCM, vrai/faux, associations, classements et réponses rédigées.

## 2. Notions essentielles

HTML utilise `<a>` pour un lien ; DNS résout les noms ; HTTPS utilise 443. Apache est un serveur Web, MySQL un SGBD, Chrome un navigateur et PHP un langage serveur. Les couches réseau sont Physique, Liaison, Réseau, Transport, Session, Présentation, Application.

Les registres sont plus rapides que la RAM, le BIOS est non volatile et le bus d’adresses ne transporte pas les données. IPv6 utilise 128 bits ; IPv4 privée n’est pas publique. Excel distingue `MAX`, `NB.SI`, `CONCATENER`, `ARRONDI` et `AUJOURDHUI`.

## 3. Méthodes pour résoudre les exercices

Pour une association, identifier le rôle de chaque élément avant d’associer. Pour un classement, partir du niveau bas vers haut ou du déclencheur vers le résultat. Pour 50 machines, ajouter réseau et broadcast avant de choisir le CIDR.

## 4. Astuces et pièges à éviter

- `<br>` est un saut de ligne, pas un paragraphe.
- Le bus d’adresses indique une position ; le bus de données transporte une valeur.
- SMTP envoie le courrier ; IMAP/POP le récupèrent.
- Un `/26` fournit 62 hôtes utilisables.

## 5. Ce qu’il faut retenir

Les questions à choix testent souvent une différence de rôle. Lire chaque proposition jusqu’au bout et justifier les faux avec le concept précis.''',
'EP-010': '''# Cours

## 1. Comprendre la matière

Le jeudi utilise quatre dossiers de technologie Web, architecture, réseaux et Excel avec QCM, associations, classements, erreurs et cas pratiques.

## 2. Notions essentielles

Outils navigateur, DNS, codes HTTP, responsive design, HTML/CSS/JavaScript/JSON et mise en ligne structurent le Web. En matériel : fréquence en hertz, cache, SSD, BIOS/UEFI, POST, pilotes, partitions et unités binaires. En réseau : pare-feu, DHCP, DNS, NAT, VPN, OSI, APIPA et sous-réseaux. En Excel : `SI`, références absolues, `RECHERCHEV`, agrégats, formats et erreurs.

## 3. Méthodes pour résoudre les exercices

Pour « trouver l’erreur », repérer le concept violé puis réécrire toute la version correcte. Pour un classement, reconstruire la chaîne logique. Pour un cas pratique, répondre dans les sous-parties (a), (b), (c) et donner un exemple concret. Pour le réseau, isoler couche physique, IP, route, DNS.

## 4. Astuces et pièges à éviter

- `ERR_NAME_NOT_RESOLVED` désigne d’abord une résolution DNS échouée.
- `#NOM?` vient souvent d’un texte sans guillemets dans une formule.
- `#REF!` indique une référence supprimée.
- La source s’arrête avant le taux de remise : ne pas l’inventer.

## 5. Ce qu’il faut retenir

Une correction complète traite chaque sous-partie et distingue le symptôme, la cause puis la solution. Signaler explicitement une donnée absente du sujet.''',
'EP-011': '''# Cours

## 1. Comprendre la matière

Le vendredi combine Web/API, architecture système, diagnostic réseau et Excel sous forme de QCM, vrai/faux, associations, classements et cas pratiques.

## 2. Notions essentielles

REST expose des ressources par URL, souvent en JSON ; HTTP 201 indique une création. Front-end, back-end et base de données ont des rôles distincts. Un bus relie les composants, un SSD stocke en flash et un pilote fait l’interface avec le matériel.

Réseau : `ping`, `ipconfig`, `tracert`, `nslookup`, ARP, VLAN, DHCP et TCP handshake. Un `/26` donne 62 hôtes ; IPv4 fait 32 bits, une MAC 48 bits. Excel utilise validation, filtres, `$`, `SOMME.SI.ENS`, `ARRONDI` et des codes d’erreur.

## 3. Méthodes pour résoudre les exercices

Pour un handshake, mémoriser SYN → SYN-ACK → ACK. Pour un diagnostic, tester d’abord le lien puis IP locale, passerelle, IP externe et nom DNS. Pour Excel, suivre la chaîne sélectionner → fonction → plage → critère → résultat.

## 4. Astuces et pièges à éviter

- HTTPS ne garantit pas qu’un site est fiable.
- Une IP `169.254.x.x` pointe souvent vers DHCP.
- Un VLAN sépare logiquement ; il faut encore un routage/pare-feu correct.
- `NBVAL` compte les cellules non vides, pas seulement les nombres.

## 5. Ce qu’il faut retenir

Dans un cas pratique, répondre avec une configuration ou une commande concrète. Dans un QCM, distinguer le rôle exact du protocole ou de l’outil.''',
'EP-012': '''# Cours

## 1. Comprendre la matière

Cette application est un entraînement d’adressage IPv4 en `/24`. Il faut séparer partie réseau et partie hôte, puis trouver les limites du sous-réseau.

## 2. Notions essentielles

`/24` signifie 24 bits réseau et 8 bits hôte. Masque : `255.255.255.0`. Réseau : partie hôte à zéro ; broadcast : partie hôte à un ; hôtes : entre les deux. Un octet se convertit en binaire avec les valeurs 128, 64, 32, 16, 8, 4, 2, 1.

## 3. Méthodes pour résoudre les exercices

1. Lire le préfixe.
2. Écrire le masque décimal.
3. Mettre les bits hôte à zéro pour le réseau.
4. Mettre les bits hôte à un pour le broadcast.
5. Exclure ces deux adresses pour la plage utilisable.
6. Pour deux IP, comparer leurs adresses réseau.

## 4. Astuces et pièges à éviter

- Une adresse hôte valide n’est ni réseau ni broadcast.
- `/24` contient 256 adresses au total mais 254 hôtes utilisables.
- Ne pas confondre le dernier octet d’hôte avec l’adresse complète.

## 5. Ce qu’il faut retenir

Pour `192.168.1.0/24`, réseau `.0`, hôtes `.1` à `.254`, broadcast `.255`. La méthode réseau/host/broadcast résout tout le QCM.''',
'EP-013': '''# Cours

## 1. Comprendre la matière

Cette application porte sur le découpage d’un `/24` en sous-réseaux `/27`.

## 2. Notions essentielles

`/27` laisse 5 bits hôte : `2^5 = 32` adresses par bloc et `32 - 2 = 30` hôtes utilisables. Le masque est `255.255.255.224` et le pas est `256 - 224 = 32`.

Les réseaux successifs sont `.0`, `.32`, `.64`, `.96`, etc. Dans un bloc, réseau = première adresse, broadcast = dernière, hôtes = adresses intermédiaires.

## 3. Méthodes pour résoudre les exercices

Trouver le multiple de 32 inférieur ou égal au dernier octet. Ajouter 31 pour le broadcast. Comparer ensuite l’IP à la plage du bloc. Pour compter les sous-réseaux depuis `/24`, emprunter 3 bits : `2^3 = 8`.

## 4. Astuces et pièges à éviter

- `.28` appartient au bloc `.0–.31`, pas à un réseau `.24`.
- `.31` est broadcast ; `.32` commence le bloc suivant.
- Une IP peut être valide dans un bloc mais appartenir à un autre avec un autre masque.

## 5. Ce qu’il faut retenir

`/27` = masque `.224`, pas 32 hôtes mais 30 utilisables, blocs de 32 et 8 sous-réseaux issus d’un `/24`.''',
'EP-014': '''# Cours

## 1. Comprendre la matière

Cette application porte sur le découpage en blocs `/29`, utiles pour de petits réseaux.

## 2. Notions essentielles

`/29` laisse 3 bits hôte : 8 adresses totales et 6 hôtes utilisables. Le masque est `255.255.255.248` et le pas est `256 - 248 = 8`.

Les blocs finissent par `.0`, `.8`, `.16`, `.24`, `.32`, etc. La première adresse est le réseau ; la dernière est le broadcast.

## 3. Méthodes pour résoudre les exercices

Repérer le multiple de 8 qui précède le dernier octet. Ajouter 7 pour trouver le broadcast ; les six valeurs internes sont utilisables. Pour savoir si deux hôtes communiquent directement, comparer leurs blocs `/29`.

## 4. Astuces et pièges à éviter

- `.228` appartient au bloc `.224–.231`.
- `.224` est réseau et `.231` broadcast.
- Depuis un `/24`, passer à `/29` emprunte 5 bits : 32 sous-réseaux.

## 5. Ce qu’il faut retenir

`/29` = `.248`, blocs de 8, 6 hôtes utilisables. Toujours calculer les limites avant de juger une IP.''',
'EP-015': '''# Cours

## 1. Comprendre la matière

Ce QCM rassemble les règles générales de sous-réseautage IPv4 : masques, tailles de blocs, classes historiques, hôtes et communication entre réseaux.

## 2. Notions essentielles

Pour un préfixe `/n`, bits hôte = `32 - n`, adresses totales = `2^(32-n)` et hôtes classiques = `2^(32-n)-2`. La taille du bloc dans le dernier octet est `256 - valeur_du_masque`.

Un `/29` a 8 adresses, 6 hôtes et un pas de 8. Un `/30` a le masque `255.255.255.252`. Une adresse de broadcast sert à joindre tous les hôtes et ne s’attribue pas à une machine.

## 3. Méthodes pour résoudre les exercices

1. Convertir le masque ou le préfixe.
2. Calculer les bits hôte et la taille de bloc.
3. Trouver le début et la fin du bloc contenant l’IP.
4. Déterminer la plage d’hôtes.
5. Comparer les réseaux avant de conclure sur une communication directe.
6. Pour un besoin de 6 hôtes, choisir le plus petit bloc fournissant au moins 6 adresses utilisables.

## 4. Astuces et pièges à éviter

- Le broadcast n’est pas la passerelle par défaut.
- Deux adresses privées peuvent être dans des réseaux différents.
- Les classes A/B/C sont historiques ; le CIDR est la méthode actuelle.
- Une taille totale de 8 n’est pas une capacité de 8 hôtes.

## 5. Ce qu’il faut retenir

Mémoriser les couples `/29 = .248 = 8 adresses = 6 hôtes` et `/30 = .252`. La taille de bloc permet de résoudre rapidement les QCM.''',
}

for exam_id, course in COURSES.items():
    path = ROOT / 'content' / 'epreuves' / exam_id / 'epreuve.md'
    original = path.read_text(encoding='utf-8')
    marker = '\n---\n\n## Transcription fidèle\n'
    if marker not in original:
        raise SystemExit(f'Marker absent: {path}')
    before, after = original.split(marker, 1)
    if '\n# Cours\n' in before:
        before = before.split('\n# Cours\n', 1)[0].rstrip()
    path.write_text(before.rstrip() + '\n\n' + course.strip() + marker + after, encoding='utf-8')

course_data = {exam_id: course.strip() for exam_id, course in COURSES.items()}
(ROOT / 'epreuves-courses.js').write_text(
    'window.ATELIER_EXAM_COURSES = ' + json.dumps(course_data, ensure_ascii=False) + ';\n',
    encoding='utf-8'
)
