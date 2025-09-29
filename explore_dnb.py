
# -----------------------------------------------------------------------------------------------------
# listes de fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

def taux_reussite(resultat):
    """calcule le pourcentage de réussite correspondant au résultat

    Args:
        resultat (tuple): le résultat d'un collège pour une session (année)
        
    Returns:
        float:  le pourcentage de réussite (nb. admis / nb. présents ā la session)
    """
    pass


def meilleur(resultat1, resultat2):
    """vérifie si resultat1 est meilleur que resultat2 au sens des taux de réussites

    Args:
        resultat1 (tuple): un résultat d'un collège pour une session (année)
        resultat2 (tuple): un autre résultat d'un collège pour une session (année)

    Returns:
        bool:   True si le taux de réussite de resultat1 est supérieur ā celui de resultat2
    """    
    pass


def meilleur_taux_reussite(liste_resultats):
    """recherche le meilleur taux de réussite dans une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le meilleur taux de rēussite
    """
    pass


def pire_taux_reussite(liste_resultats):
    """recherche le pire taux de réussite parmi une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le pire taux de rēussite
    """
    pass


def total_admis_presents(liste_resultats):
    """calcule le nombre total de candidats admis et de candidats présents aux épreuves du DNB parmi les résultats de la liste passée en paramètre

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple : un couple d'entiers contenant le nombre total de candidats admis et prēsents
    """
    pass


def filtre_session(liste_resultats, session):
    """génère la sous-liste de liste_resultats, restreinte aux résultats de la session demandée

    Args:
        liste_resultats (list): une liste de résultats
        session (int): une session (année)

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats de la session demandēe
    """
    pass


def filtre_departement(liste_resultats, departement):
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département demandé

    Args:
        liste_resultats (list): une liste de résultats
        departement (int): un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du dēpartement demandé
    """
    pass


def filtre_college(liste_resultats, nom, departement):
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département donné et dont le nom du collège contient le nom passé en paramètre (en minuscule ou majuscule)

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (éventuellement incomplet)
        departement (int) : un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du collège et du département recherchēs
    """
    pass


def taux_reussite_global(liste_resultats, session):
    """calcule le taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)
        
    Returns:
        float: taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnēes
    """
    pass


def moyenne_taux_reussite_college(liste_resultats, nom, departement):
    """calcule la moyenne des taux de réussite d'un collège sur l'ensemble des sessions

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (exact)
        departement (int) : un numéro de département
        
    Returns:
        float: moyenne des taux de rēussite d'un collège sur l'ensemble des sessions
    """
    pass


def meilleur_college(liste_resultats, session):
    """recherche le collège ayant obtenu le meilleur taux de réussite pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)
        
    Returns:
        tuple: couple contenant le nom du collège et le dēpartement
    """
    pass


def liste_sessions(liste_resultats):
    """retourne la liste des sessions (années) dont au moins un résultat est reporté dans la liste de résultats.
    ATTENTION : la liste renvoyée doit être sans doublons et triée par ordre chronologique des sessions 

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        list: une liste de session (int) triēe et sans doublons
    """    
    pass


def plus_longe_periode_amelioration(liste_resultats):
    """recherche la plus longue periode d'amélioration du taux de réussite global au DNB

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple: un couple contenant la session (année) de début de la période et la session de fin de la pēriode
    """    
    pass

def est_bien_triee(liste_resultats):
    """vérifie qu'une liste de résultats est bien triée dans l'ordre chronologique des sessions puis dans l'ordre croissant des départements puis dans l'ordre alphabétique des noms de collèges
    
    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        bool: True si la liste est bien triēe et False sinon
    """
    pass


def fusionner_resultats(liste_resultats1, liste_resultats2):
    """Fusionne deux listes de résultats triées sans doublons en une liste triée sans doublon
    sachant qu'un même résultat peut être présent dans les deux listes

    Args:
        liste_resultat1 (list): la première liste de résultats
        liste_resultat2 (list): la seconde liste de résultats

    Returns:
        list: la liste triée sans doublon comportant tous les rēsultats de liste_resultats1 et liste_resultats2
    """
    pass


def charger_resultats(nom_fichier):
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des rēsultats contenus dans le fichier
    """
    pass
