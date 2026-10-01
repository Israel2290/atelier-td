# Application 1 — Adressage IPv4 /24

## Informations générales

- ID : EP-012
- Année : Non précisée dans le document original.
- Session : Non précisée
- Matière : Réseaux
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Non précisé dans le document original.
- Source : `APPLICATION1.pdf` (2 pages PDF)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

# Cours

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

Pour `192.168.1.0/24`, réseau `.0`, hôtes `.1` à `.254`, broadcast `.255`. La méthode réseau/host/broadcast résout tout le QCM.
---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

## Page 1

    QUIZ RÉSEAUX — 192.168.1.28/24
1. Dans 192.168.1.28/24, quelle partie de l'adresse identifie l'hôte ?
    A. 192.168.1
    B. 28
    C. 192.168.1.28
    D. 1.28

2. Quelle est l'adresse réseau de 192.168.1.28/24 ?
    A. 192.168.1.0
    B. 192.168.1.28
    C. 192.168.0.0
    D. 192.168.1.1

3. Quelle est l'adresse de broadcast du réseau contenant 192.168.1.28/24 ?
    A. 192.168.1.28
    B. 192.168.1.0
    C. 192.168.1.254
    D. 192.168.1.255

4. À quel masque décimal correspond /24 ?
    A. 255.255.0.0
    B. 255.255.255.128
    C. 255.255.255.0
    D. 255.0.0.0

5. 192.168.1.28 est-elle une adresse utilisable pour un hôte (PC, imprimante, etc.) ?
    A. Non, c'est l'adresse réseau
    B. Oui, c'est une adresse hôte valide
    C. Non, c'est l'adresse de broadcast
    D. Impossible à dire sans passerelle

6. Quelle est la plage complète des adresses hôtes utilisables dans ce réseau /24 ?
    A. 192.168.1.0 à 192.168.1.255
    B. 192.168.1.1 à 192.168.1.254
    C. 192.168.1.28 à 192.168.1.254
    D. 192.168.1.1 à 192.168.1.255

7. Quelle est la représentation binaire du dernier octet (28) de l'adresse 192.168.1.28 ?
    A. 00011100


---

## Page 2

    B. 00011010
    C. 00101100
    D. 00011110

8. Si on divise 192.168.1.0/24 en deux sous-réseaux /25, dans lequel se trouve 192.168.1.28 ?
    A. 192.168.1.0/25 (hôtes 1 à 126)
    B. 192.168.1.128/25 (hôtes 129 à 254)
    C. 192.168.1.0/26
    D. Aucun des deux

9. Combien d'adresses IP au total (hôtes + réseau + broadcast) contient le sous-réseau de
192.168.1.28/24 ?
    A. 128
    B. 256
    C. 254
    D. 512

10. Une machine A a l'IP 192.168.1.28/24 et une machine B a l'IP 192.168.1.200/24. Sont-
elles sur le même réseau ?
    A. Non, elles sont sur des réseaux différents
    B. Oui, elles sont sur le même réseau
    C. Cela dépend du fournisseur d'accès
    D. Impossible sans connaître la passerelle
