import random


# def interclasser(liste1: list[int | float], liste2: list[int | float]):
#     if liste1 == []:
#         return liste2
#     elif liste2 == []:
#         return liste1
#     else:
#         if liste1[0] <= liste2[0]:
#             return [liste1[0]] + interclasser(liste1[1::], liste2)
#         else:
#             return [liste2[0]] + interclasser(liste1, liste2[1::])


# def tri_fusion(liste: list[int | float]):
#     if len(liste) <= 1:
#         return liste
#     else:
#         return interclasser(
#             tri_fusion(liste[0 : len(liste) // 2]),
#             tri_fusion(liste[len(liste) // 2 : len(liste)]),
#         )


def tri_fusion(liste: list[int]):
    longueur = len(liste) - 1
    taille = 1
    while taille < longueur:
        i = 0
        while i < longueur:
            gauche1 = i
            droite1 = i + taille - 1
            gauche2 = i + taille
            droite2 = i + 2 * taille - 1

            if gauche2 >= longueur:
                break

            if droite2 >= longueur:
                droite2 = longueur - 1

            temp = merge(liste, gauche1, droite1, gauche2, droite2)

            for j in range(droite2 - (gauche1 + 1)):
                liste[i + j] = temp[j]

            i += 2 * taille
        taille *= 2
    return liste


def merge(liste, gauche1, droite1, gauche2, droite2):
    temp = []
    index = 0
    while gauche1 <= droite1 and gauche2 <= droite2:
        if liste[gauche1] <= liste[gauche2]:
            temp[index] = liste[gauche1]
            index += 1
            gauche1 += 1
        else:
            temp[index] = liste[gauche2]
            index += 1
            gauche2 += 1

    while gauche1 <= droite1:
        temp[index] = liste[gauche1]
        index += 1
        gauche1 += 1

    while gauche2 <= droite2:
        temp[index] = liste[gauche2]
        index += 1
        gauche2 += 1

    return temp


if __name__ == "__main__":
    # a: list[int] = [random.randrange(-100, 100) for _ in range(10000)]
    a: list[int] = [random.randrange(0, 10) for _ in range(10)]
    print(a)
    print(tri_fusion(a))
    print(a)
