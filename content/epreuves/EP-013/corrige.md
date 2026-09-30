# Corrigé type — Application 2 — Adressage IPv4 /27

- Identifiant : EP-013
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Réseaux — question 1 — APPLICATION 2 · /27

### Énoncé / tâche associée
Quel masque décimal correspond à /27 ?

### Niveau 1 — réponse minimale
B. 255.255.255.224

### Niveau 3 — explication pédagogique
Les 27 premiers bits à 1 donnent 255.255.255.224.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — APPLICATION 2 · /27

### Énoncé / tâche associée
Combien d’adresses totales contient un sous-réseau /27 ?

### Niveau 1 — réponse minimale
C. 32

### Niveau 3 — explication pédagogique
Il reste 5 bits hôte : 2⁵ = 32 adresses.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — APPLICATION 2 · /27

### Énoncé / tâche associée
Quel est le réseau /27 contenant 192.168.1.28 ?

### Niveau 1 — réponse minimale
C. 192.168.1.0

### Niveau 3 — explication pédagogique
Les blocs /27 avancent par 32 ; .28 appartient au bloc .0–.31.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 4 — APPLICATION 2 · /27

### Énoncé / tâche associée
Quelle est l’adresse de broadcast de ce sous-réseau /27 ?

### Niveau 1 — réponse minimale
D. 192.168.1.31

### Niveau 3 — explication pédagogique
Le bloc .0–.31 se termine par le broadcast .31.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 5 — APPLICATION 2 · /27

### Énoncé / tâche associée
Quelle est la plage d’hôtes utilisables du sous-réseau ?

### Niveau 1 — réponse minimale
B. .1 à .30

### Niveau 3 — explication pédagogique
Les adresses réseau .0 et broadcast .31 sont réservées.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 6 — APPLICATION 2 · /27

### Énoncé / tâche associée
Combien d’hôtes utilisables contient un /27 ?

### Niveau 1 — réponse minimale
C. 30

### Niveau 3 — explication pédagogique
32 adresses totales moins réseau et broadcast donnent 30 hôtes.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 7 — APPLICATION 2 · /27

### Énoncé / tâche associée
192.168.1.28 est-elle utilisable comme adresse hôte dans ce /27 ?

### Niveau 1 — réponse minimale
B. Oui

### Niveau 3 — explication pédagogique
.28 est comprise entre .1 et .30 dans le réseau .0/27.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 8 — APPLICATION 2 · /27

### Énoncé / tâche associée
Combien de sous-réseaux /27 peut-on créer depuis 192.168.1.0/24 ?

### Niveau 1 — réponse minimale
A. 8

### Niveau 3 — explication pédagogique
On emprunte 3 bits au /24 : 2³ = 8 sous-réseaux.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 9 — APPLICATION 2 · /27

### Énoncé / tâche associée
192.168.1.28/27 et 192.168.1.35/27 sont-elles sur le même sous-réseau ?

### Niveau 1 — réponse minimale
B. Non, sous-réseaux différents

### Niveau 3 — explication pédagogique
.28 est dans .0–.31 ; .35 est dans .32–.63.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 10 — APPLICATION 2 · /27

### Énoncé / tâche associée
En numérotant les sous-réseaux /27 de 192.168.1.0/24 à partir de 1, lequel contient 192.168.1.28 ?

### Niveau 1 — réponse minimale
C. 1er : .0/27

### Niveau 3 — explication pédagogique
Le premier bloc /27 est .0–.31, qui contient .28.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.
