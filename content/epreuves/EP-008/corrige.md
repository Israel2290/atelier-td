# Corrigé type — Épreuve de tronc commun — Mardi

- Identifiant : EP-008
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Web — question 1 — Tronc commun · mardi

### Énoncé / tâche associée
Différencie Internet et Web. Cite un service Internet qui n’est pas le Web.

### Niveau 1 — réponse minimale
Internet est le réseau mondial interconnecté

### Niveau 2 — réponse complète / solution type
Internet est le réseau mondial interconnecté. Le Web est un service sur Internet utilisant HTTP/HTTPS et des pages liées. Le courrier électronique (SMTP/IMAP) est un autre service.

### Niveau 3 — explication pédagogique
Le Web est une application d’Internet, pas un synonyme du réseau Internet.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 2 — Tronc commun · mardi

### Énoncé / tâche associée
Quel est le rôle du DNS ? Décris les principales étapes de résolution d’un nom.

### Niveau 1 — réponse minimale
DNS associe un nom de domaine à une adresse IP

### Niveau 2 — réponse complète / solution type
DNS associe un nom de domaine à une adresse IP. Le résolveur consulte son cache puis interroge les serveurs DNS nécessaires (racine, domaine de premier niveau, autoritaire), récupère l’adresse et la met en cache.

### Niveau 3 — explication pédagogique
Le cache accélère les résolutions suivantes tant que la durée TTL n’est pas expirée.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 3 — Tronc commun · mardi

### Énoncé / tâche associée
Compare GET et POST avec un usage de chacun. Que signifient 404 et 500 ?

### Niveau 1 — réponse minimale
GET demande/consulte une ressource et ses paramètres apparaissent souvent dans l’URL ; POST envoie des données dans le corps, par exemple pour créer un compte

### Niveau 2 — réponse complète / solution type
GET demande/consulte une ressource et ses paramètres apparaissent souvent dans l’URL ; POST envoie des données dans le corps, par exemple pour créer un compte. 404 : ressource introuvable. 500 : erreur interne du serveur.

### Niveau 3 — explication pédagogique
Les données POST ne sont pas automatiquement chiffrées : HTTPS est toujours requis pour les protéger.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Lire GET ou POST en PHP

## Web — question 4 — Tronc commun · mardi

### Énoncé / tâche associée
Pourquoi HTTP est-il dit « sans état » ? Comment cookies et sessions résolvent-ils cela ?

### Niveau 1 — réponse minimale
Chaque requête HTTP est traitée indépendamment ; le protocole ne mémorise pas seul l’utilisateur

### Niveau 2 — réponse complète / solution type
Chaque requête HTTP est traitée indépendamment ; le protocole ne mémorise pas seul l’utilisateur. Un cookie conserve un identifiant côté navigateur ; le serveur l’associe à une session contenant l’état (connexion, panier, etc.).

### Niveau 3 — explication pédagogique
Le cookie transporte souvent un identifiant, pas nécessairement toutes les données de session.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Web — question 5 — Tronc commun · mardi

### Énoncé / tâche associée
Décris l’injection SQL et XSS et donne une protection pour chacune.

### Niveau 1 — réponse minimale
L’injection SQL introduit une entrée qui modifie une commande SQL ; utiliser des requêtes préparées

### Niveau 2 — réponse complète / solution type
L’injection SQL introduit une entrée qui modifie une commande SQL ; utiliser des requêtes préparées. XSS injecte un script exécuté dans le navigateur d’une victime ; encoder/échapper les données affichées et appliquer une politique CSP.

### Niveau 3 — explication pédagogique
Valider les entrées aide, mais ne remplace ni les paramètres SQL ni l’encodage de sortie.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 1 — Tronc commun · mardi

### Énoncé / tâche associée
Décris le cycle d’exécution d’une instruction par le processeur.

### Niveau 1 — réponse minimale
Le processeur récupère l’instruction en mémoire (fetch), la décode, exécute l’opération, puis écrit le résultat si nécessaire

### Niveau 2 — réponse complète / solution type
Le processeur récupère l’instruction en mémoire (fetch), la décode, exécute l’opération, puis écrit le résultat si nécessaire. Le cycle se répète ; le compteur ordinal indique l’instruction suivante.

### Niveau 3 — explication pédagogique
Les détails varient selon l’architecture, mais récupération, décodage et exécution en sont les étapes centrales.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 2 — Tronc commun · mardi

### Énoncé / tâche associée
Présente la hiérarchie registres, cache, RAM, stockage et explique son intérêt.

### Niveau 1 — réponse minimale
Du plus rapide et petit au plus lent et grand : registres → cache → RAM → SSD/HDD

### Niveau 2 — réponse complète / solution type
Du plus rapide et petit au plus lent et grand : registres → cache → RAM → SSD/HDD. Cette hiérarchie équilibre vitesse, capacité et coût ; les données fréquemment utilisées restent près du processeur.

### Niveau 3 — explication pédagogique
La localité temporelle et spatiale permet aux caches de réduire l’attente mémoire.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 3 — Tronc commun · mardi

### Énoncé / tâche associée
Compare SSD et HDD selon trois critères.

### Niveau 1 — réponse minimale
SSD : mémoire flash sans pièces mobiles, accès rapide et silencieux, mais prix par Go souvent supérieur

### Niveau 2 — réponse complète / solution type
SSD : mémoire flash sans pièces mobiles, accès rapide et silencieux, mais prix par Go souvent supérieur. HDD : plateaux mécaniques, plus lent et plus sensible aux chocs, mais généralement économique pour de grandes capacités.

### Niveau 3 — explication pédagogique
Les critères pertinents incluent vitesse, prix/capacité, bruit, consommation et résistance.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 4 — Tronc commun · mardi

### Énoncé / tâche associée
Définis périphérique d’entrée, de sortie et mixte, avec deux exemples de chaque.

### Niveau 1 — réponse minimale
Entrée : envoie des données à l’ordinateur (clavier, souris)

### Niveau 2 — réponse complète / solution type
Entrée : envoie des données à l’ordinateur (clavier, souris). Sortie : restitue les résultats (écran, imprimante). Mixte : entrée et sortie (écran tactile, clé USB ou carte réseau).

### Niveau 3 — explication pédagogique
Le classement dépend du sens des échanges avec l’ordinateur.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Architecture — question 5 — Tronc commun · mardi

### Énoncé / tâche associée
Convertis 77 en binaire et 3F₁₆ en décimal. Pourquoi utilise-t-on l’hexadécimal ?

### Niveau 1 — réponse minimale
77₁₀ = 1001101₂

### Niveau 2 — réponse complète / solution type
77₁₀ = 1001101₂. 3F₁₆ = 3×16 + 15 = 63₁₀. L’hexadécimal représente les groupes de quatre bits de façon compacte et lisible.

### Niveau 3 — explication pédagogique
Chaque chiffre hexadécimal correspond exactement à quatre bits.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 1 — Tronc commun · mardi

### Énoncé / tâche associée
Compare les topologies bus, étoile et anneau. Donne un avantage et un inconvénient de l’étoile.

### Niveau 1 — réponse minimale
Bus : câble partagé, économique mais une panne du câble perturbe tout

### Niveau 2 — réponse complète / solution type
Bus : câble partagé, économique mais une panne du câble perturbe tout. Étoile : liens vers un équipement central, facile à dépanner mais dépend du centre et demande plus de câbles. Anneau : nœuds en boucle, circulation ordonnée mais une rupture peut interrompre l’anneau.

### Niveau 3 — explication pédagogique
En étoile, un lien terminal peut tomber sans couper les autres, mais une panne du switch central est critique.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — Tronc commun · mardi

### Énoncé / tâche associée
Différencie TCP et UDP et donne un exemple d’usage de chacun.

### Niveau 1 — réponse minimale
TCP établit une connexion et assure ordre, retransmission et contrôle de flux : transfert de fichiers ou Web

### Niveau 2 — réponse complète / solution type
TCP établit une connexion et assure ordre, retransmission et contrôle de flux : transfert de fichiers ou Web. UDP n’établit pas de connexion et n’assure pas la livraison : voix/vidéo temps réel ou DNS.

### Niveau 3 — explication pédagogique
TCP privilégie la fiabilité ; UDP réduit les délais et les échanges de contrôle.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — Tronc commun · mardi

### Énoncé / tâche associée
Pour 172.16.5.130/26, donne le masque, réseau, broadcast et nombre d’hôtes utilisables.

### Niveau 1 — réponse minimale
Masque 255.255.255.192

### Niveau 2 — réponse complète / solution type
Masque 255.255.255.192. Pas de blocs de 64 : .130 est dans .128–.191. Réseau 172.16.5.128 ; broadcast 172.16.5.191 ; plage hôte .129–.190 ; 62 hôtes.

### Niveau 3 — explication pédagogique
Six bits hôte donnent 64 adresses totales, moins réseau et broadcast.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 4 — Tronc commun · mardi

### Énoncé / tâche associée
Différencie paire torsadée et fibre optique. Quand utiliser un câble droit ou croisé ?

### Niveau 1 — réponse minimale
La paire torsadée transmet des signaux électriques, est peu coûteuse et adaptée aux réseaux locaux

### Niveau 2 — réponse complète / solution type
La paire torsadée transmet des signaux électriques, est peu coûteuse et adaptée aux réseaux locaux. La fibre transporte la lumière, offre grande portée/débit et résiste aux interférences. Câble droit entre équipements de types différents ; croisé entre équipements similaires sans auto-MDI/MDIX.

### Niveau 3 — explication pédagogique
Les équipements modernes corrigent souvent automatiquement le câblage croisé.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 5 — Tronc commun · mardi

### Énoncé / tâche associée
Cite les quatre couches TCP/IP et associe un protocole à chacune.

### Niveau 1 — réponse minimale
Accès réseau (Ethernet/Wi-Fi), Internet (IP), Transport (TCP/UDP), Application (HTTP, DNS, SMTP).

### Niveau 2 — réponse complète / solution type
Accès réseau (Ethernet/Wi-Fi), Internet (IP), Transport (TCP/UDP), Application (HTTP, DNS, SMTP).

### Niveau 3 — explication pédagogique
Le modèle TCP/IP regroupe les fonctions du modèle OSI en quatre couches.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Reconnaître une panne DHCP avec DORA

## Excel — question 1 — Tronc commun · mardi

### Énoncé / tâche associée
Distingue NB, NBVAL et NB.SI et donne un exemple.

### Niveau 1 — réponse minimale
NB compte les cellules numériques : =NB(A1:A10)

### Niveau 2 — réponse complète / solution type
NB compte les cellules numériques : =NB(A1:A10). NBVAL compte les cellules non vides : =NBVAL(A1:A10). NB.SI compte selon un critère : =NB.SI(A1:A10;">=10").

### Niveau 3 — explication pédagogique
NB.SI prend la plage puis le critère ; NBVAL inclut texte et nombres.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 2 — Tronc commun · mardi

### Énoncé / tâche associée
Écris la formule de somme des ventes C2:C50 pour la région « Nord » en A2:A50 et explique-la.

### Niveau 1 — réponse minimale
=SOMME.SI(A2:A50;"Nord";C2:C50)

### Niveau 2 — réponse complète / solution type
=SOMME.SI(A2:A50;"Nord";C2:C50). La fonction teste le critère sur A2:A50 puis additionne les cellules correspondantes de C2:C50.

### Niveau 3 — explication pédagogique
La plage de critères et la plage de somme ont la même taille et correspondent ligne à ligne.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 3 — Tronc commun · mardi

### Énoncé / tâche associée
Qu’est-ce que la mise en forme conditionnelle ? Donne un exemple et les étapes.

### Niveau 1 — réponse minimale
Elle modifie automatiquement l’apparence d’une cellule selon une règle

### Niveau 2 — réponse complète / solution type
Elle modifie automatiquement l’apparence d’une cellule selon une règle. Exemple : colorer en rouge les notes < 10. Sélectionner la plage, choisir Accueil → Mise en forme conditionnelle, définir la règle et le format.

### Niveau 3 — explication pédagogique
La mise en forme change l’affichage sans modifier la valeur de la cellule.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 4 — Tronc commun · mardi

### Énoncé / tâche associée
Écris une formule : « Très bien » si B2 ≥ 16, « Bien » si B2 ≥ 14, « Passable » sinon.

### Niveau 1 — réponse minimale
=SI(B2>=16;"Très bien";SI(B2>=14;"Bien";"Passable"))

### Niveau 2 — réponse complète / solution type
=SI(B2>=16;"Très bien";SI(B2>=14;"Bien";"Passable"))

### Niveau 3 — explication pédagogique
Tester le seuil le plus élevé en premier évite qu’une note de 16 soit classée seulement « Bien ».

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Excel — question 5 — Tronc commun · mardi

### Énoncé / tâche associée
Cite trois types de graphiques Excel et leur usage, puis décris comment en créer un.

### Niveau 1 — réponse minimale
Colonnes/barres : comparer des catégories

### Niveau 2 — réponse complète / solution type
Colonnes/barres : comparer des catégories. Courbe : évolution dans le temps. Secteurs : proportions d’un total (peu de catégories). Sélectionner les données, choisir Insertion → Graphique adapté, puis ajouter titre et légende.

### Niveau 3 — explication pédagogique
Choisir le graphique selon le message à communiquer et éviter les secteurs avec trop de catégories.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.
