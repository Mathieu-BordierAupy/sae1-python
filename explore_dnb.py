# -----------------------------------------------------------------------------------------------------
# listes de fonctions à implémenter
# -----------------------------------------------------------------------------------------------------


# Type custom pour les tuple de resultat
Resultat = tuple[int, str, int, int, int]


def taux_reussite(resultat: Resultat) -> float | None:
    """calcule le pourcentage de réussite correspondant au résultat

    Args:
        resultat (tuple): le résultat d'un collège pour une session (année)

    Returns:
        float:  le pourcentage de réussite (nb. admis / nb. présents à la session)
    """
    nb_presents: int = resultat[3]

    if nb_presents <= 0:
        return None

    nb_admis: int = resultat[4]

    return (nb_admis / nb_presents) * 100


def meilleur(resultat1: Resultat, resultat2: Resultat) -> bool | None:
    """vérifie si resultat1 est meilleur que resultat2 au sens des taux de réussites

    Args:
        resultat1 (tuple): un résultat d'un collège pour une session (année)
        resultat2 (tuple): un autre résultat d'un collège pour une session (année)

    Returns:
        bool:   True si le taux de réussite de resultat1 est supérieur ā celui de resultat2
    """

    res1: float | None = taux_reussite(resultat1)
    res2: float | None = taux_reussite(resultat2)

    if res1 is None and res2 is not None:
        return False
    elif res2 is None and res1 is not None:
        return True
    elif res1 is None and res2 is None:
        return None

    return res1 > res2  # pyright: ignore[reportOperatorIssue]


def meilleur_taux_reussite(liste_resultats: list[Resultat]) -> float | None:
    """recherche le meilleur taux de réussite dans une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le meilleur taux de rēussite
    """
    if liste_resultats == []:
        return None

    meilleur_res: float | None = taux_reussite(liste_resultats[0])

    # Pour chaque tour de boucle
    #   i prend l'entier suivant du range à partir de 1
    #   liste_resultats[i] est le i-ème résultat de la liste
    #   taux est le taux de réussite du i-ème resultat
    #   meilleur_res est le meilleur taux de réussite trouvé ou None si les taux ne sont pas calculable
    for i in range(1, len(liste_resultats)):
        taux = taux_reussite(liste_resultats[i])
        if meilleur_res is None or (taux is not None and meilleur_res < taux):
            meilleur_res = taux

    return meilleur_res


def pire_taux_reussite(liste_resultats: list[Resultat]) -> float | None:
    """recherche le pire taux de réussite parmi une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le pire taux de rēussite
    """
    if liste_resultats == []:
        return None

    pire_res: float | None = taux_reussite(liste_resultats[0])

    # Pour chaque tour de boucle
    #   i prend l'entier suivant du range à partir de 1
    #   liste_resultats[i] est le i-ème résultat de la liste
    #   taux est le taux de réussite du i-ème resultat
    #   pire_res est le pire taux de réussite trouvé ou None si les taux ne sont pas calculable
    for i in range(1, len(liste_resultats)):
        taux = taux_reussite(liste_resultats[i])
        if pire_res is None or (taux is not None and pire_res > taux):
            pire_res = taux

    return pire_res


def total_admis_presents(liste_resultats: list[Resultat]) -> tuple[int, int] | None:
    """calcule le nombre total de candidats admis et de candidats présents aux épreuves du DNB parmi les résultats de la liste passée en paramètre

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple : un couple d'entiers contenant le nombre total de candidats admis et prēsents
    """
    if liste_resultats == []:
        return None

    total_admis: int = 0
    total_present: int = 0

    # Pour chaque tour de boucle
    #   resultat est l'élément suivant de liste_resultats
    #   total_admis est le total du nombre d'admis trouvé jusqu'à maintenant
    #   total_present est le total du nombre de present trouvé jusqu'à maintenant
    for resultat in liste_resultats:
        total_admis += resultat[4]
        total_present += resultat[3]

    return (total_admis, total_present)


def filtre_session(liste_resultats: list[Resultat], session: int) -> list[Resultat]:
    """génère la sous-liste de liste_resultats, restreinte aux résultats de la session demandée

    Args:
        liste_resultats (list): une liste de résultats
        session (int): une session (année)

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats de la session demandēe
    """
    liste_resultats_triee: list[Resultat] = []

    # Pour chaque tour de boucle
    #   resultats est le tuple resultat suivant de liste_resultats
    #   resultats[0] est le numéro de session (année) du resulat actuel
    #   liste_resultats_triee contient tout les resultats qui sont de la bonne session déjà trouvé
    for resultats in liste_resultats:
        if resultats[0] == session:
            liste_resultats_triee.append(resultats)

    return liste_resultats_triee


def filtre_departement(
    liste_resultats: list[Resultat], departement: int
) -> list[Resultat]:
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département demandé

    Args:
        liste_resultats (list): une liste de résultats
        departement (int): un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du dēpartement demandé
    """
    liste_resultats_triee: list[Resultat] = []

    # Pour chaque tour de boucle
    #   resultats est le tuple resultat suivant de liste_resultats
    #   resultats[2] est le numéro de departement du resulat actuel
    #   liste_resultats_triee contient tout les resultats qui sont du bon departement déjà trouvé
    for resultats in liste_resultats:
        if resultats[2] == departement:
            liste_resultats_triee.append(resultats)

    return liste_resultats_triee


def string_contient(source: str, contient: str) -> bool:
    """Cherche une chaine de caractère dans une autre, ne respecte pas la case

    Args:
        source (str): La chaine de caractère où chercher
        contient (str): La chaine à retrouver dans la source

    Returns:
        bool: True si la chaine à été correctement trouvé, sinon False
    """
    if len(contient) == 0:
        return False

    # Pour chaque tour de boucle
    #   i est l'indice actuelle du parcours de la chaine de comparaison (contient)
    #   j est l'indice actuelle du parcours de la chaine source (range)
    #   lettre est le j-ème caractère de la chaine source, en lower
    i: int = 0
    for j in range(len(source)):
        lettre = source[j].lower()

        # Compare si la lettre actuelle est la lettre dans contient à l'indice j
        if lettre == contient[i].lower():
            # Si la lettre est la bonne, on avance le curseur i de 1
            i += 1
        else:
            # On remet i à 0 pour reprendre la comparaison à 0
            i = 0
        # Si i est la taille de contient, c'est qu'il à été parcouru en entier et donc que le mot à été trouvé
        if i == len(contient):
            return True

    return False


def filtre_college(
    liste_resultats: list[Resultat], nom: str, departement: int
) -> list[Resultat]:
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département donné et dont le nom du collège contient le nom passé en paramètre (en minuscule ou majuscule)

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (éventuellement incomplet)
        departement (int) : un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du collège et du département recherchēs
    """
    liste_resultats_triee: list[Resultat] = []

    # Pour chaque tour de boucle
    #   resultats est le tuple resultat suivant de liste_resultats
    #   resultats[1] est le nom du college du resulat actuel
    #   resultats[2] est le numéro de departement du resulat actuel
    #   liste_resultats_triee contient tout les resultats qui sont du bon departement et commencant par le nom déjà trouvé
    for resultat in liste_resultats:
        # TODO: Maybe I can't use __contains__
        if (
            resultat[2] == departement and nom.lower() in resultat[1].lower()
        ):  # string_contient(resultat[1], nom):
            liste_resultats_triee.append(resultat)

    return liste_resultats_triee


def taux_reussite_global(liste_resultats: list[Resultat], session: int) -> float | None:
    """calcule le taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)

    Returns:
        float: taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnēes
    """
    liste_resultats_session: list[Resultat] = filtre_session(liste_resultats, session)

    total_ad_pr = total_admis_presents(liste_resultats_session)
    # Verify that the function ran correctly
    if total_ad_pr is None:
        return None
    nb_admis, nb_present = total_ad_pr

    if nb_admis <= 0:
        return None

    return nb_admis / nb_present * 100


def moyenne_taux_reussite_college(
    liste_resultats: list[Resultat], nom: str, departement: int
) -> float | None:
    """calcule la moyenne des taux de réussite d'un collège sur l'ensemble des sessions

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (exact)
        departement (int) : un numéro de département

    Returns:
        float: moyenne des taux de rēussite d'un collège sur l'ensemble des sessions
    """
    if liste_resultats == []:
        return None
    total_taux: float = 0
    nb_taux: int = 0

    # Pour chaque tour de boucle
    #   resultats est le tuple resultat suivant de liste_resultats
    #   resultats[1] est le nom du college du resulat actuel
    #   resultats[2] est le numéro de departement du resulat actuel
    #   liste_resultats_triee contient tout les resultats qui sont du bon departement et avec le bon nom déjà trouvé
    for resultat in liste_resultats:
        if resultat[2] == departement and resultat[1] == nom:
            taux: float | None = taux_reussite(resultat)
            if taux is not None:
                total_taux += taux
                nb_taux += 1

    if nb_taux <= 0:
        return None

    return total_taux / nb_taux


def meilleur_college(
    liste_resultats: list[Resultat], session: int
) -> tuple[str, int] | None:
    """recherche le collège ayant obtenu le meilleur taux de réussite pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)

    Returns:
        tuple: couple contenant le nom du collège et le dēpartement
    """
    resultats = filtre_session(liste_resultats, session)

    if resultats == []:
        return None

    meilleur_trouve: int = 0
    meilleur_taux = taux_reussite(resultats[0])

    # Pour chaque tour de boucle
    #   i est l'entier suivant du range à partir de 1
    #   resultats[i] est le i-ème resultat
    #   taux est le taux de reussite du i-ème resultat ou None si non calculable
    #   meilleur_trouve est l'indice du meilleur resultat
    #   meilleur_taux est le taux du meilleur resultat pour ne pas à avoir à le recalculer
    for i in range(1, len(resultats)):
        taux = taux_reussite(resultats[i])
        if taux is not None and (meilleur_taux is None or taux > meilleur_taux):
            meilleur_trouve = i
            meilleur_taux = taux
    # Aucun taux n'a pu être calculé, on renvoie donc None
    if meilleur_taux is None:
        return None
    return resultats[meilleur_trouve][1], resultats[meilleur_trouve][2]


def fusion_liste(liste1: list[int], liste2: list[int]) -> list[int]:
    if not liste1:
        return liste2
    if not liste2:
        return liste1

    if liste1[0] <= liste2[0]:
        return [liste1[0]] + fusion_liste(liste1[1:], liste2)
    else:
        return [liste2[0]] + fusion_liste(liste1, liste2[1:])


def tri_fusion(liste: list[int]) -> list[int]:
    if len(liste) <= 1:
        return liste

    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])
    return fusion_liste(gauche, droite)


def liste_sessions(liste_resultats: list[Resultat]) -> list[int]:
    """retourne la liste des sessions (années) dont au moins un résultat est reporté dans la liste de résultats.
    ATTENTION : la liste renvoyée doit être sans doublons et triée par ordre chronologique des sessions

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        list[int]: une liste de session (int) triēe et sans doublons
    """
    nouvelle_session: list[int] = []

    for resultat in liste_resultats:
        if resultat[0] not in nouvelle_session:
            nouvelle_session.append(resultat[0])

    tri_fusion(nouvelle_session)

    return nouvelle_session


def plus_longue_periode_amelioration(
    liste_resultats: list[Resultat],
) -> tuple[int, int] | None:
    """recherche la plus longue periode d'amélioration du taux de réussite global au DNB

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple: un couple contenant la session (année) de début de la période et la session de fin de la pēriode
    """

    if liste_resultats == []:
        return None

    # Fait une liste de toute les années de la liste
    annees = []
    for r in liste_resultats:
        if r[0] not in annees:
            annees.append(r[0])

    # Calcule les moyennes pour chaque années
    moyennes = []
    for annee in annees:
        sous_liste = filtre_session(liste_resultats, annee)
        total = total_admis_presents(sous_liste)
        if total is not None:
            admis, presents = total
            if presents > 0:
                moyennes.append((annee, admis / presents * 100))

    if not moyennes:
        return None

    meilleur_debut = meilleur_fin = moyennes[0][0]
    debut = moyennes[0][0]
    fin = debut
    plus_grand_temps = 1
    temps_actuelle = 1

    # Cherche la plus longue periode d'amélioration permis les moyennes calculé
    for i in range(1, len(moyennes)):
        if moyennes[i][1] > moyennes[i - 1][1]:
            fin = moyennes[i][0]
            temps_actuelle += 1
        else:
            if temps_actuelle > plus_grand_temps:
                plus_grand_temps = temps_actuelle
                meilleur_debut, meilleur_fin = debut, fin
            debut = moyennes[i][0]
            fin = debut
            temps_actuelle = 1

    if temps_actuelle > plus_grand_temps:
        meilleur_debut, meilleur_fin = debut, fin

    return (meilleur_debut, meilleur_fin)


def est_bien_triee(liste_resultats: list[Resultat]) -> bool:
    """vérifie qu'une liste de résultats est bien triée dans l'ordre chronologique des sessions puis dans l'ordre croissant des départements puis dans l'ordre alphabétique des noms de collèges

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        bool: True si la liste est bien triēe et False sinon
    """

    if not liste_resultats:
        return True

    for i in range(1, len(liste_resultats)):
        prev = liste_resultats[i - 1]
        cur = liste_resultats[i]

        # Comparer par année d'abord
        if prev[0] > cur[0]:
            return False

        # Si même année, comparer par département
        if prev[0] == cur[0]:
            if prev[2] > cur[2]:
                return False

            # Si même année ET même département, comparer par nom (alphabétique)
            if prev[2] == cur[2]:
                # On compare les noms tels quels ; tests utilisent des majuscules,
                # donc l'ordre lexicographique standard est OK.
                if prev[1] > cur[1]:
                    return False

    return True


def fusionner_resultats(
    liste_resultats1: list[Resultat], liste_resultats2: list[Resultat]
) -> list[Resultat]:
    """Fusionne deux listes de résultats triées sans doublons en une liste triée sans doublon
    sachant qu'un même résultat peut être présent dans les deux listes

    Args:
        liste_resultat1 (list): la première liste de résultats
        liste_resultat2 (list): la seconde liste de résultats

    Returns:
        list: la liste triée sans doublon comportant tous les rēsultats de liste_resultats1 et liste_resultats2
    """
    # Indice pour la parcours asyncrone des deux liste
    i, j = 0, 0
    resultat = []

    while i < len(liste_resultats1) and j < len(liste_resultats2):
        resultat1, resultat2 = liste_resultats1[i], liste_resultats2[j]

        # Comparaison hiérarchique : année, département, nom
        if resultat1[0] < resultat2[0] or (
            resultat1[0] == resultat2[0]
            and (
                resultat1[2] < resultat2[2]
                or (resultat1[2] == resultat2[2] and resultat1[1] < resultat2[1])
            )
        ):
            if not resultat or resultat[-1] != resultat1:
                resultat.append(resultat1)
            i += 1
        elif (
            resultat1[0] == resultat2[0]
            and resultat1[1] == resultat2[1]
            and resultat1[2] == resultat2[2]
        ):
            # Les deux résultats sont identiques (même année, nom, département)
            if not resultat or resultat[-1] != resultat1:
                resultat.append(resultat1)
            i += 1
            j += 1
        else:
            if not resultat or resultat[-1] != resultat2:
                resultat.append(resultat2)
            j += 1

    # Ajouter les restes (s’ils ne sont pas déjà présents)
    while i < len(liste_resultats1):
        if not resultat or resultat[-1] != liste_resultats1[i]:
            resultat.append(liste_resultats1[i])
        i += 1

    while j < len(liste_resultats2):
        if not resultat or resultat[-1] != liste_resultats2[j]:
            resultat.append(liste_resultats2[j])
        j += 1

    return resultat


def charger_resultats(nom_fichier: str) -> list[Resultat] | None:
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des rēsultats contenus dans le fichier
    """
    try:
        with open(nom_fichier, "r", errors="replace") as file:
            line = file.readline()  # Skip la 1er ligne
            liste_resultats: list[Resultat] = []
            line_compte = 1

            while line != "":
                try:
                    line = file.readline()
                    line_compte += 1
                    raw = line.split(",")  # Decoupe la ligne
                    #       annee       nom     departement     presents    admis
                    data = int(raw[0]), raw[1], int(raw[2]), int(raw[3]), int(raw[4])
                    liste_resultats.append(data)
                except (IndexError, ValueError, UnicodeDecodeError) as err:
                    # Gestion des erreurs
                    print(f"Line invalide '{err}' ({line_compte}:{file.tell()})")
            return liste_resultats
    except OSError as err:
        # Gestion des erreurs d'ouverture et d'accès au fichier
        print(f"Impossible de lire '{nom_fichier}'! {err.strerror}")
        return None
