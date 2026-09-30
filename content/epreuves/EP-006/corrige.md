# Corrigé type — Épreuve de tronc commun — Lundi

- Identifiant : EP-006
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Web — question 1 — Tronc commun · lundi

### Énoncé / tâche associée
Explique le modèle client-serveur et précise le rôle du navigateur et du serveur web.

### Niveau 1 — réponse minimale
Le navigateur (client) envoie une requête HTTP au serveur

### Niveau 2 — réponse complète / solution type
Le navigateur (client) envoie une requête HTTP au serveur. Le serveur traite la requête, accède si besoin aux données et renvoie une réponse que le navigateur affiche.

### Niveau 3 — explication pédagogique
Le client demande une ressource ; le serveur la fournit ou la génère.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 2 — Tronc commun · lundi

### Énoncé / tâche associée
Décompose l’URL https://www.exemple.bj:8080/produits/liste.php?categorie=3#haut.

### Niveau 1 — réponse minimale
https : protocole ; www.exemple.bj : nom d’hôte ; 8080 : port ; /produits/liste.php : chemin ; ?categorie=3 : paramètre de requête ; #haut : fragment/point d’ancrage.

### Niveau 2 — réponse complète / solution type
https : protocole ; www.exemple.bj : nom d’hôte ; 8080 : port ; /produits/liste.php : chemin ; ?categorie=3 : paramètre de requête ; #haut : fragment/point d’ancrage.

### Niveau 3 — explication pédagogique
Le fragment est traité dans le navigateur et n’est généralement pas envoyé au serveur.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 3 — Tronc commun · lundi

### Énoncé / tâche associée
Décris les étapes entre la saisie d’une adresse dans le navigateur et l’affichage de la page.

### Niveau 1 — réponse minimale
Le navigateur analyse l’URL, résout le domaine par DNS, établit une connexion au serveur (TLS si HTTPS), envoie une requête HTTP, reçoit la réponse et interprète HTML, CSS, JavaScript et ressources pour afficher la page.

### Niveau 2 — réponse complète / solution type
Le navigateur analyse l’URL, résout le domaine par DNS, établit une connexion au serveur (TLS si HTTPS), envoie une requête HTTP, reçoit la réponse et interprète HTML, CSS, JavaScript et ressources pour afficher la page.

### Niveau 3 — explication pédagogique
La résolution DNS précède l’envoi de la requête HTTP à l’adresse IP trouvée.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 4 — Tronc commun · lundi

### Énoncé / tâche associée
Compare HTTP et HTTPS. Pourquoi HTTPS est-il indispensable pour un paiement en ligne ?

### Niveau 1 — réponse minimale
HTTPS est HTTP protégé par TLS

### Niveau 2 — réponse complète / solution type
HTTPS est HTTP protégé par TLS. Il chiffre les échanges, authentifie le serveur avec son certificat et protège l’intégrité des données ; HTTP transmet sans cette protection.

### Niveau 3 — explication pédagogique
Le cadenas indique une connexion chiffrée, pas que le site est honnête ou exempt de fraude.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 5 — Tronc commun · lundi

### Énoncé / tâche associée
Distingue une page statique d’une page dynamique et donne le rôle de HTML, CSS et JavaScript.

### Niveau 1 — réponse minimale
Une page statique est servie telle qu’elle est stockée ; une page dynamique varie selon les données, l’utilisateur ou les requêtes

### Niveau 2 — réponse complète / solution type
Une page statique est servie telle qu’elle est stockée ; une page dynamique varie selon les données, l’utilisateur ou les requêtes. HTML structure le contenu, CSS définit son apparence et JavaScript ajoute des interactions.

### Niveau 3 — explication pédagogique
Une page dynamique peut être générée côté serveur, modifiée côté navigateur, ou les deux.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 1 — Tronc commun · lundi

### Énoncé / tâche associée
Décris le rôle du processeur et de ses principaux éléments. Cite deux caractéristiques de performance.

### Niveau 1 — réponse minimale
Le processeur exécute les instructions

### Niveau 2 — réponse complète / solution type
Le processeur exécute les instructions. L’unité de commande orchestre leur exécution, l’UAL réalise les opérations et les registres stockent temporairement les valeurs. Fréquence et nombre de cœurs sont deux caractéristiques, avec l’architecture et le cache.

### Niveau 3 — explication pédagogique
Une fréquence ou un nombre de cœurs plus élevé ne garantit pas seul de meilleures performances.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 2 — Tronc commun · lundi

### Énoncé / tâche associée
Compare la RAM, la ROM et la mémoire de masse (HDD/SSD), notamment leur volatilité.

### Niveau 1 — réponse minimale
La RAM est rapide et volatile

### Niveau 2 — réponse complète / solution type
La RAM est rapide et volatile. La ROM conserve des instructions même hors tension. Le HDD/SSD stocke durablement les fichiers et n’est pas volatile ; il est plus lent que la RAM.

### Niveau 3 — explication pédagogique
Volatile signifie que le contenu est perdu lorsque l’alimentation est coupée.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 3 — Tronc commun · lundi

### Énoncé / tâche associée
Quel est le rôle de la carte mère ? Cite cinq composants qui s’y connectent.

### Niveau 1 — réponse minimale
Elle relie et permet la communication entre composants

### Niveau 2 — réponse complète / solution type
Elle relie et permet la communication entre composants. Exemples : processeur, RAM, SSD/HDD, carte graphique, alimentation, carte réseau, périphériques USB.

### Niveau 3 — explication pédagogique
Les composants compatibles se connectent directement ou via des connecteurs et bus de la carte mère.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 4 — Tronc commun · lundi

### Énoncé / tâche associée
Décris les grandes étapes du démarrage d’un ordinateur.

### Niveau 1 — réponse minimale
À la mise sous tension, le firmware BIOS/UEFI lance le POST, vérifie le matériel, choisit un périphérique de démarrage et lance le chargeur d’amorçage, qui charge le noyau du système d’exploitation.

### Niveau 2 — réponse complète / solution type
À la mise sous tension, le firmware BIOS/UEFI lance le POST, vérifie le matériel, choisit un périphérique de démarrage et lance le chargeur d’amorçage, qui charge le noyau du système d’exploitation.

### Niveau 3 — explication pédagogique
Le firmware initialise le matériel avant le chargement du système.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 5 — Tronc commun · lundi

### Énoncé / tâche associée
Convertis 45 en binaire et 11010₂ en décimal. Combien de bits dans 3 octets ?

### Niveau 1 — réponse minimale
45₁₀ = 101101₂

### Niveau 2 — réponse complète / solution type
45₁₀ = 101101₂. 11010₂ = 16 + 8 + 2 = 26₁₀. 3 octets = 24 bits.

### Niveau 3 — explication pédagogique
Chaque position binaire vaut une puissance de 2 ; un octet contient 8 bits.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 1 — Tronc commun · lundi

### Énoncé / tâche associée
Définis LAN, MAN et WAN et donne un exemple de chacun.

### Niveau 1 — réponse minimale
LAN : réseau local d’un logement, bureau ou campus

### Niveau 2 — réponse complète / solution type
LAN : réseau local d’un logement, bureau ou campus. MAN : réseau à l’échelle d’une ville. WAN : réseau étendu reliant régions ou pays ; Internet en est un exemple.

### Niveau 3 — explication pédagogique
La différence principale est l’étendue géographique, pas une technologie unique.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — Tronc commun · lundi

### Énoncé / tâche associée
Différencie un hub, un switch et un routeur.

### Niveau 1 — réponse minimale
Le hub répète les signaux vers tous ses ports

### Niveau 2 — réponse complète / solution type
Le hub répète les signaux vers tous ses ports. Le switch transmet une trame au port associé à l’adresse MAC destinataire. Le routeur achemine les paquets IP entre réseaux.

### Niveau 3 — explication pédagogique
Hub : couche physique ; switch : liaison ; routeur : réseau.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — Tronc commun · lundi

### Énoncé / tâche associée
Cite les sept couches OSI et associe un protocole ou équipement à deux couches.

### Niveau 1 — réponse minimale
Physique, Liaison de données, Réseau, Transport, Session, Présentation, Application

### Niveau 2 — réponse complète / solution type
Physique, Liaison de données, Réseau, Transport, Session, Présentation, Application. Exemples : Ethernet/switch à Liaison ; IP/routeur à Réseau ; TCP à Transport ; HTTP à Application.

### Niveau 3 — explication pédagogique
Les couches s’ordonnent du support physique vers les services applicatifs.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 4 — Tronc commun · lundi

### Énoncé / tâche associée
Pour 192.168.10.25/24, donne la classe IPv4, le masque, le réseau, le broadcast et les hôtes utilisables.

### Niveau 1 — réponse minimale
Classe C selon l’adressage classful historique ; masque 255.255.255.0 ; réseau 192.168.10.0 ; broadcast 192.168.10.255 ; hôtes 192.168.10.1 à .254, soit 254.

### Niveau 2 — réponse complète / solution type
Classe C selon l’adressage classful historique ; masque 255.255.255.0 ; réseau 192.168.10.0 ; broadcast 192.168.10.255 ; hôtes 192.168.10.1 à .254, soit 254.

### Niveau 3 — explication pédagogique
Le préfixe /24 laisse 8 bits hôte : 2⁸ − 2 = 254 adresses utilisables.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 5 — Tronc commun · lundi

### Énoncé / tâche associée
Explique DHCP et DNS, puis décris les quatre étapes DORA.

### Niveau 1 — réponse minimale
DHCP attribue automatiquement la configuration IP ; DNS traduit les noms en adresses IP

### Niveau 2 — réponse complète / solution type
DHCP attribue automatiquement la configuration IP ; DNS traduit les noms en adresses IP. DORA : Discover (découverte), Offer (offre), Request (demande), Acknowledge (confirmation).

### Niveau 3 — explication pédagogique
Un client DHCP diffuse d’abord une découverte, puis accepte une offre et reçoit la confirmation du bail.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 1 — Tronc commun · lundi

### Énoncé / tâche associée
Distingue classeur, feuille, cellule et plage de cellules.

### Niveau 1 — réponse minimale
Le classeur est le fichier Excel

### Niveau 2 — réponse complète / solution type
Le classeur est le fichier Excel. Une feuille est un onglet du classeur. Une cellule est l’intersection d’une ligne et d’une colonne. Une plage est un ensemble de cellules, par exemple A1:B4.

### Niveau 3 — explication pédagogique
Un classeur peut contenir plusieurs feuilles ; chaque feuille contient des cellules.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 2 — Tronc commun · lundi

### Énoncé / tâche associée
Distingue référence relative, absolue et mixte. Que devient =A2*$B$1 de C2 à C3 ?

### Niveau 1 — réponse minimale
A2 est relative et devient A3

### Niveau 2 — réponse complète / solution type
A2 est relative et devient A3. $B$1 est absolue et ne change pas. La formule devient =A3*$B$1. Une référence mixte fixe soit la colonne ($A2), soit la ligne (A$2).

### Niveau 3 — explication pédagogique
Le signe $ fige la colonne ou la ligne qui le suit lors d’une recopie.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 3 — Tronc commun · lundi

### Énoncé / tâche associée
Écris la formule « Admis » si B2 ≥ 10, sinon « Ajourné », puis les formules somme, moyenne et maximum de B2:B20.

### Niveau 1 — réponse minimale
=SI(B2>=10;"Admis";"Ajourné") ; =SOMME(B2:B20) ; =MOYENNE(B2:B20) ; =MAX(B2:B20).

### Niveau 2 — réponse complète / solution type
=SI(B2>=10;"Admis";"Ajourné") ; =SOMME(B2:B20) ; =MOYENNE(B2:B20) ; =MAX(B2:B20).

### Niveau 3 — explication pédagogique
SI teste une condition ; SOMME, MOYENNE et MAX agrègent une plage.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 4 — Tronc commun · lundi

### Énoncé / tâche associée
Explique RECHERCHEV et ses arguments.

### Niveau 1 — réponse minimale
RECHERCHEV(valeur_cherchée; table_matrice; no_index_col; [valeur_proche])

### Niveau 2 — réponse complète / solution type
RECHERCHEV(valeur_cherchée; table_matrice; no_index_col; [valeur_proche]). Elle cherche dans la première colonne de la plage et renvoie la valeur de la colonne indiquée sur la même ligne. FAUX demande une correspondance exacte.

### Niveau 3 — explication pédagogique
En correspondance approximative, la première colonne doit généralement être triée.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 5 — Tronc commun · lundi

### Énoncé / tâche associée
Qu’est-ce qu’un tableau croisé dynamique ? À quoi sert-il et comment le créer ?

### Niveau 1 — réponse minimale
C’est un outil qui résume et analyse des données par catégories avec des agrégations

### Niveau 2 — réponse complète / solution type
C’est un outil qui résume et analyse des données par catégories avec des agrégations. Sélectionner une table avec en-têtes, choisir Insertion → Tableau croisé dynamique, puis placer les champs en Lignes, Colonnes, Valeurs et Filtres.

### Niveau 3 — explication pédagogique
La source doit être tabulaire et comporter des en-têtes distincts.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.
