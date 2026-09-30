# Corrigé type — Application 3 — Adressage IPv4 /29

- Identifiant : EP-014
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Réseaux — question 1 — APPLICATION3 · /29

### Énoncé / tâche associée
À quel préfixe correspond le masque 255.255.255.248 ?

### Niveau 1 — réponse minimale
C. /29

### Niveau 3 — explication pédagogique
248 vaut 11111000 en binaire : cinq bits réseau dans le dernier octet, soit /29.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — APPLICATION3 · /29

### Énoncé / tâche associée
Combien de bits sont réservés aux hôtes avec /29 ?

### Niveau 1 — réponse minimale
B. 3

### Niveau 3 — explication pédagogique
IPv4 comporte 32 bits ; 32 − 29 = 3 bits hôte.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — APPLICATION3 · /29

### Énoncé / tâche associée
Combien d’adresses totales contient un /29 ?

### Niveau 1 — réponse minimale
B. 8

### Niveau 3 — explication pédagogique
3 bits hôte donnent 2³ = 8 adresses.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 4 — APPLICATION3 · /29

### Énoncé / tâche associée
Quel est le réseau /29 contenant 192.168.1.228 ?

### Niveau 1 — réponse minimale
B. 192.168.1.224

### Niveau 3 — explication pédagogique
Les blocs /29 ont une taille de 8 ; .228 appartient au bloc .224–.231.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 5 — APPLICATION3 · /29

### Énoncé / tâche associée
Quelle est l’adresse de broadcast du réseau ?

### Niveau 1 — réponse minimale
C. 192.168.1.231

### Niveau 3 — explication pédagogique
Le bloc .224–.231 se termine à .231.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 6 — APPLICATION3 · /29

### Énoncé / tâche associée
Quelle est la plage d’hôtes utilisables ?

### Niveau 1 — réponse minimale
B. .225 à .230

### Niveau 3 — explication pédagogique
Exclure le réseau .224 et le broadcast .231 donne .225–.230.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 7 — APPLICATION3 · /29

### Énoncé / tâche associée
Combien d’hôtes utilisables y a-t-il dans un /29 ?

### Niveau 1 — réponse minimale
C. 6

### Niveau 3 — explication pédagogique
8 adresses totales moins réseau et broadcast donnent 6.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 8 — APPLICATION3 · /29

### Énoncé / tâche associée
192.168.1.228 est-elle une adresse hôte utilisable dans ce /29 ?

### Niveau 1 — réponse minimale
B. Oui

### Niveau 3 — explication pédagogique
.228 est dans la plage d’hôtes .225–.230.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 9 — APPLICATION3 · /29

### Énoncé / tâche associée
Combien de sous-réseaux /29 peut-on créer à partir d’un /24 ?

### Niveau 1 — réponse minimale
C. 32

### Niveau 3 — explication pédagogique
Un /24 découpé en /29 emprunte 5 bits : 2⁵ = 32 sous-réseaux.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 10 — APPLICATION3 · /29

### Énoncé / tâche associée
192.168.1.228/29 et 192.168.1.233/29 sont-elles sur le même sous-réseau ?

### Niveau 1 — réponse minimale
B. Non, réseaux différents

### Niveau 3 — explication pédagogique
.228 est dans le bloc .224–.231 ; .233 est dans le bloc .232–.239.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.
