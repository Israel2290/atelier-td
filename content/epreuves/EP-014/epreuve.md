# Application 3 — Adressage IPv4 /29

## Informations générales

- ID : EP-014
- Année : Non précisée dans le document original.
- Session : Non précisée
- Matière : Réseaux
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Non précisé dans le document original.
- Source : `APPLICATION3.pdf` (2 pages PDF)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

# Cours

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

`/29` = `.248`, blocs de 8, 6 hôtes utilisables. Toujours calculer les limites avant de juger une IP.
---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

## Page 1

                              QUIZ RÉSEAUX
                  Adresse 192.168.1.228 avec masque 255.255.255.248

1. À quel préfixe CIDR (/xx) correspond le masque 255.255.255.248 ?
    A. /27
    B. /28
    C. /29
    D. /30

2. Combien de bits sont réservés à la partie hôte avec ce masque ?
    A. 2 bits
    B. 3 bits
    C. 4 bits
    D. 5 bits

3. Combien d'adresses IP contient chaque sous-réseau /29 (total, réseau et broadcast inclus)
?
    A. 4
    B. 8
    C. 16
    D. 32

4. Quelle est l'adresse réseau du sous-réseau /29 contenant 192.168.1.228 ?
    A. 192.168.1.220
    B. 192.168.1.224
    C. 192.168.1.228
    D. 192.168.1.192

5. Quelle est l'adresse de broadcast de ce sous-réseau /29 ?
    A. 192.168.1.230
    B. 192.168.1.255
    C. 192.168.1.231
    D. 192.168.1.239

6. Quelle est la plage d'adresses hôtes utilisables dans ce sous-réseau /29 ?
    A. 192.168.1.224 à 192.168.1.231
    B. 192.168.1.225 à 192.168.1.230
    C. 192.168.1.225 à 192.168.1.231
    D. 192.168.1.228 à 192.168.1.230

7. Combien d'hôtes utilisables y a-t-il dans un sous-réseau /29 ?


---

## Page 2

    A. 8
    B. 7
    C. 6
    D. 4

8. 192.168.1.228 est-elle une adresse hôte utilisable dans ce sous-réseau /29 ?
    A. Non, c'est l'adresse réseau
    B. Oui, c'est une adresse hôte valide
    C. Non, c'est l'adresse de broadcast
    D. Impossible à dire

9. Combien de sous-réseaux /29 peut-on créer à partir d'un réseau /24 comme
192.168.1.0/24 ?
    A. 8
    B. 16
    C. 32
    D. 64

10. Une machine A a l'IP 192.168.1.228/29 et une machine B a l'IP 192.168.1.233/29. Sont-
elles sur le même sous-réseau ?
    A. Oui, même sous-réseau /29
    B. Non, sous-réseaux /29 différents
    C. Impossible à déterminer
    D. Cela dépend de la passerelle
