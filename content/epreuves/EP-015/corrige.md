# Corrigé type — QCM de sous-réseautage IPv4

- Identifiant : EP-015
- Statut de vérification : ⚠️ PARTIEL — corrigé type relié aux questions ; relecture pédagogique et vérification réelle du code/SQL question par question restent à effectuer.

> Le sujet d’origine est intégralement transcrit dans `epreuve.md`. Les réponses ci-dessous sont des réponses types ; si le sujet autorise d’autres formulations ou solutions, elles peuvent également convenir.

## Réseaux — question 1 — QCM subnetting · /29

### Énoncé / tâche associée
Quel masque correspond à /29 ?

### Niveau 1 — réponse minimale
B. 255.255.255.248

### Niveau 3 — explication pédagogique
Un /29 a 29 bits à 1 : 255.255.255.248.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 2 — QCM subnetting · /29

### Énoncé / tâche associée
Combien d’adresses contient un bloc /29 ?

### Niveau 1 — réponse minimale
B. 8

### Niveau 3 — explication pédagogique
Il reste 3 bits hôte : 2³ = 8 adresses totales.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 3 — QCM subnetting · /29

### Énoncé / tâche associée
Combien d’hôtes sont utilisables dans un /29 classique ?

### Niveau 1 — réponse minimale
C. 6

### Niveau 3 — explication pédagogique
8 adresses moins réseau et broadcast donnent 6 hôtes.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 4 — QCM subnetting · /29

### Énoncé / tâche associée
Quel est le réseau contenant 192.10.11.150/29 ?

### Niveau 1 — réponse minimale
B. 192.10.11.144

### Niveau 3 — explication pédagogique
Les blocs de 8 couvrent .144–.151 ; le réseau est .144.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

### Templates associés
- Calculer un sous-réseau CIDR

## Réseaux — question 5 — QCM subnetting · /29

### Énoncé / tâche associée
Quel est le broadcast de 192.10.11.150/29 ?

### Niveau 1 — réponse minimale
A. 192.10.11.151

### Niveau 3 — explication pédagogique
Le bloc .144–.151 se termine par le broadcast .151.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 6 — QCM subnetting · /29

### Énoncé / tâche associée
Quelle est la première adresse hôte de 192.10.11.144/29 ?

### Niveau 1 — réponse minimale
B. 192.10.11.145

### Niveau 3 — explication pédagogique
La première adresse après le réseau .144 est .145.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 7 — QCM subnetting · /29

### Énoncé / tâche associée
Quelle est la dernière adresse hôte de 192.10.11.144/29 ?

### Niveau 1 — réponse minimale
A. 192.10.11.150

### Niveau 3 — explication pédagogique
Le broadcast est .151 ; la dernière adresse hôte est .150.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 8 — QCM subnetting · /29

### Énoncé / tâche associée
192.10.11.150 peut-elle être attribuée à une machine ?

### Niveau 1 — réponse minimale
C. Oui, adresse hôte valide

### Niveau 3 — explication pédagogique
.150 se situe entre .145 et .150, plage hôte du réseau .144/29.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 9 — QCM subnetting · /29

### Énoncé / tâche associée
Combien de bits sont réservés à la partie hôte dans un /29 ?

### Niveau 1 — réponse minimale
B. 3

### Niveau 3 — explication pédagogique
32 − 29 = 3 bits hôte.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 10 — QCM subnetting · /29

### Énoncé / tâche associée
Quel est le préfixe CIDR équivalent à 255.255.255.248 ?

### Niveau 1 — réponse minimale
C. /29

### Niveau 3 — explication pédagogique
Le dernier octet 248 contient cinq bits à 1 ; 24 + 5 = /29.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 11 — QCM subnetting · /29

### Énoncé / tâche associée
Quelle est la taille de bloc d’un masque /29 ?

### Niveau 1 — réponse minimale
C. 8

### Niveau 3 — explication pédagogique
256 − 248 = 8 adresses par bloc.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 12 — QCM subnetting · /29

### Énoncé / tâche associée
Quel réseau suit 192.10.11.144/29 ?

### Niveau 1 — réponse minimale
B. 192.10.11.152/29

### Niveau 3 — explication pédagogique
Les réseaux avancent de 8 : après .144 vient .152.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 13 — QCM subnetting · /29

### Énoncé / tâche associée
192.10.11.144 peut-elle être attribuée à un hôte ?

### Niveau 1 — réponse minimale
B. Non, adresse réseau

### Niveau 3 — explication pédagogique
.144 est la première adresse du bloc : c’est l’adresse réseau.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 14 — QCM subnetting · /29

### Énoncé / tâche associée
Dans quelle classe historique se trouve 192.10.11.150 ?

### Niveau 1 — réponse minimale
C. C

### Niveau 3 — explication pédagogique
Dans le classful historique, les adresses commençant par 192 à 223 sont de classe C.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 15 — QCM subnetting · /29

### Énoncé / tâche associée
Combien de sous-réseaux /29 peut-on créer à partir d’un /24 ?

### Niveau 1 — réponse minimale
C. 32

### Niveau 3 — explication pédagogique
Un /24 vers /29 emprunte 5 bits, soit 2⁵ = 32 sous-réseaux.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 16 — QCM subnetting · /29

### Énoncé / tâche associée
Quelle formule calcule le nombre d’hôtes utilisables d’un masque /n ?

### Niveau 1 — réponse minimale
B. 2^(32−n) − 2

### Niveau 3 — explication pédagogique
Il reste 32−n bits hôte ; dans un sous-réseau classique on retire réseau et broadcast.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 17 — QCM subnetting · /29

### Énoncé / tâche associée
192.10.11.150/29 peut-elle communiquer directement avec 192.10.11.153/29 sans routeur ?

### Niveau 1 — réponse minimale
B. Non, sous-réseaux différents

### Niveau 3 — explication pédagogique
.150 est dans .144/29 et .153 dans .152/29 : il faut router entre les deux réseaux.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 18 — QCM subnetting · /29

### Énoncé / tâche associée
Quel est le masque décimal de /30 ?

### Niveau 1 — réponse minimale
A. 255.255.255.252

### Niveau 3 — explication pédagogique
Un /30 laisse deux bits hôte ; les 30 bits réseau donnent 255.255.255.252.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 19 — QCM subnetting · /29

### Énoncé / tâche associée
Pourquoi ne peut-on pas attribuer l’adresse de broadcast à un hôte ?

### Niveau 1 — réponse minimale
B. Elle envoie vers tous les hôtes du sous-réseau

### Niveau 3 — explication pédagogique
Le broadcast désigne tous les hôtes du sous-réseau et ne peut pas identifier un hôte individuel.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.

## Réseaux — question 20 — QCM subnetting · /29

### Énoncé / tâche associée
Pour exactement 6 hôtes utilisables par sous-réseau, quel masque minimal choisir ?

### Niveau 1 — réponse minimale
B. /29

### Niveau 3 — explication pédagogique
/29 donne 8 adresses totales et 6 utilisables ; /30 n’en donne que 2.

### Méthode
Repérer chaque élément demandé, répondre dans le même ordre et vérifier que toutes les conditions et données du sujet ont été traitées.

### Points à retenir
Respecter les noms, valeurs, clés et contraintes de l’énoncé ; ne pas ajouter d’hypothèse non indiquée.
