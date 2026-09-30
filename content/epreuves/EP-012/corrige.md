# Corrigé type — Application 1 — Adressage IPv4 /24

- Identifiant : EP-012
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Réseaux — question 1 — APPLICATION1 · /24

### Énoncé / tâche associée
Dans 192.168.1.28/24, quelle partie de l’adresse identifie l’hôte ?

### Niveau 1 — réponse minimale
B. 28

### Niveau 3 — explication pédagogique
Avec /24, les 24 premiers bits désignent le réseau ; le dernier octet (28) identifie l’hôte.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — APPLICATION1 · /24

### Énoncé / tâche associée
Quelle est l’adresse réseau de 192.168.1.28/24 ?

### Niveau 1 — réponse minimale
A. 192.168.1.0

### Niveau 3 — explication pédagogique
Le masque /24 conserve les trois premiers octets et met la partie hôte à zéro.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 3 — APPLICATION1 · /24

### Énoncé / tâche associée
Quelle est l’adresse de broadcast du réseau contenant 192.168.1.28/24 ?

### Niveau 1 — réponse minimale
D. 192.168.1.255

### Niveau 3 — explication pédagogique
Le broadcast met tous les bits hôte à 1 ; pour un /24, le dernier octet vaut 255.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 4 — APPLICATION1 · /24

### Énoncé / tâche associée
À quel masque décimal correspond /24 ?

### Niveau 1 — réponse minimale
C. 255.255.255.0

### Niveau 3 — explication pédagogique
Les 24 bits réseau correspondent à trois octets à 255.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 5 — APPLICATION1 · /24

### Énoncé / tâche associée
192.168.1.28 est-elle une adresse utilisable pour un hôte ?

### Niveau 1 — réponse minimale
B. Oui, adresse hôte valide

### Niveau 3 — explication pédagogique
Dans 192.168.1.0/24, les hôtes vont de .1 à .254 ; .28 est utilisable.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 6 — APPLICATION1 · /24

### Énoncé / tâche associée
Quelle est la plage complète d’adresses hôtes utilisables dans ce réseau /24 ?

### Niveau 1 — réponse minimale
B. .1 à .254

### Niveau 3 — explication pédagogique
On exclut l’adresse réseau .0 et le broadcast .255.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 7 — APPLICATION1 · /24

### Énoncé / tâche associée
Quelle est la représentation binaire de l’octet 28 ?

### Niveau 1 — réponse minimale
A. 00011100

### Niveau 3 — explication pédagogique
28 = 16 + 8 + 4, soit 00011100₂ sur huit bits.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 8 — APPLICATION1 · /24

### Énoncé / tâche associée
Dans quel sous-réseau /25 se trouve 192.168.1.28 ?

### Niveau 1 — réponse minimale
A. 192.168.1.0/25

### Niveau 3 — explication pédagogique
Le premier /25 couvre .0 à .127 ; .28 en fait partie.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 9 — APPLICATION1 · /24

### Énoncé / tâche associée
Combien d’adresses au total contient un sous-réseau /24 ?

### Niveau 1 — réponse minimale
B. 256

### Niveau 3 — explication pédagogique
Il reste 8 bits hôte : 2⁸ = 256 adresses, dont 254 hôtes utilisables.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 10 — APPLICATION1 · /24

### Énoncé / tâche associée
192.168.1.28/24 et 192.168.1.200/24 sont-elles sur le même réseau ?

### Niveau 1 — réponse minimale
B. Oui

### Niveau 3 — explication pédagogique
Les deux adresses appartiennent à 192.168.1.0/24.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.
