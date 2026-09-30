# QCM de sous-réseautage IPv4

## Informations générales

- ID : EP-015
- Année : Non précisée dans le document original.
- Session : Non précisée
- Matière : Réseaux
- Durée : Non précisée dans le document original.
- Coefficient : Non précisé dans le document original.
- Barème : Non précisé dans le document original.
- Source : `QCM_Subnetting_EXERCICE .pdf` (2 pages PDF)
- Statut de transcription : ⚠️ PARTIEL — extraction Markdown générée ; relecture fidèle intégrale par rapport à la source à effectuer.

---

## Transcription fidèle

> Le texte, les données, choix de réponses et sous-questions sont extraits de la source. Les tableaux DOCX sont restitués en tableaux Markdown ; les pages PDF conservent leur découpage. Une relecture intégrale mot à mot reste nécessaire avant de marquer cette transcription VALIDÉE.

## Page 1

                       Analyse de sous-réseau
                                   192.10.11.150/29 — Sous-réseautage IPv4


QCM
1. Quel est le masque de sous-réseau correspondant à /29 ?
    A. 255.255.255.240
    B. 255.255.255.248
    C. 255.255.255.252
    D. 255.255.255.224

2. Combien d'adresses contient un bloc /29 ?
    A. 4
    B. 8
    C. 16
    D. 32

3. Combien d'hôtes utilisables dans un /29 ?
    A. 8
    B. 7
    C. 6
    D. 4

4. Quelle est l'adresse réseau contenant 192.10.11.150/29 ?
    A. 192.10.11.128
    B. 192.10.11.144
    C. 192.10.11.152
    D. 192.10.11.136

5. Quelle est l'adresse de broadcast du réseau contenant 192.10.11.150/29 ?
    A. 192.10.11.151
    B. 192.10.11.159
    C. 192.10.11.150
    D. 192.10.11.152

6. Quelle est la première adresse hôte utilisable dans 192.10.11.144/29 ?
    A. 192.10.11.144
    B. 192.10.11.145
    C. 192.10.11.146
    D. 192.10.11.150

7. Quelle est la dernière adresse hôte utilisable dans 192.10.11.144/29 ?
    A. 192.10.11.150
    B. 192.10.11.151
    C. 192.10.11.149
    D. 192.10.11.152

8. 192.10.11.150 peut-il être attribué à une machine du réseau ?
    A. Non, c'est l'adresse réseau
    B. Non, c'est le broadcast
    C. Oui, c'est une adresse hôte valide
    D. Non, hors de la plage

9. Combien de bits sont réservés à la partie hôte dans un /29 ?
    A. 2
    B. 3
    C. 4
    D. 5

10. Quel est le préfixe CIDR équivalent à 255.255.255.248 ?
    A. /27
    B. /28


---

## Page 2

    C. /29
    D. /30

11. Quelle est la taille de bloc (pas entre réseaux) pour un masque /29 ?
    A. 2
    B. 4
    C. 8
    D. 16

12. Quel réseau suit immédiatement 192.10.11.144/29 ?
    A. 192.10.11.148/29
    B. 192.10.11.152/29
    C. 192.10.11.160/29
    D. 192.10.11.151/29

13. 192.10.11.144 peut-il être attribué à un hôte ?
    A. Oui
    B. Non, c'est l'adresse réseau
    C. Non, c'est le broadcast
    D. Seulement en IPv6

14. Dans quelle classe d'adresse IP se situe 192.10.11.150 (classes historiques) ?
    A. Classe A
    B. Classe B
    C. Classe C
    D. Classe D

15. Combien de sous-réseaux /29 peut-on créer à partir d'un bloc /24 ?
    A. 8
    B. 16
    C. 32
    D. 64

16. Quelle formule donne le nombre d'hôtes utilisables pour un masque /n ?
    A. 2^n - 2
    B. 2^(32-n) - 2
    C. 2^(32-n)
    D. 32 - n

17. Un hôte configuré avec 192.10.11.150/29 peut-il communiquer directement avec 192.10.11.153/29 sans
routeur ?
    A. Oui, même sous-réseau
    B. Non, sous-réseaux différents
    C. Cela dépend du VLAN
    D. Toujours, en IP publique

18. Quel est le masque en notation décimale pointée pour /30 ?
    A. 255.255.255.252
    B. 255.255.255.248
    C. 255.255.255.254
    D. 255.255.255.240

19. Pourquoi ne peut-on pas attribuer l'adresse de broadcast à un hôte ?
    A. Elle est réservée au routeur par défaut
    B. Elle sert à envoyer des données à tous les hôtes du sous-réseau
    C. Elle est réservée au DNS
    D. Elle n'existe qu'en IPv6

20. Si une entreprise a besoin de 6 hôtes exactement par sous-réseau, quel masque minimal utiliser ?
    A. /30
    B. /29
    C. /28
    D. /27
