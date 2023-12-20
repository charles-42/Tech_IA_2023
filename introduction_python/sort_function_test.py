import pytest

def trier_liste(liste):

    # Vérifie que la liste ne contient que des nombres, des chaînes de caractères ou des booléens
    types_valides = (int, float, str, bool)
    for element in liste:
        if type(element) not in types_valides:
            raise ValueError("La liste ne doit contenir que des nombres, des chaînes de caractères ou des booléens")

    # Tri la liste en utilisant la fonction `sorted()`
    try:
        return sorted(liste)
    except TypeError:
        raise ValueError("La liste ne doit pas contenir des éléments de types différents")

def test_liste_vide():
    # Vérifie que la fonction renvoie une liste vide si la liste d'entrée est vide
    liste = []
    sortie_attendue = []
    assert trier_liste(liste) == sortie_attendue

def test_liste_triee():
    # Vérifie que la fonction ne modifie pas la liste d'entrée si la liste d'entrée est déjà triée
    liste = [1, 2, 3]
    sortie_attendue = liste
    trier_liste(liste)
    assert liste == sortie_attendue

def test_liste_non_triee():
    # Vérifie que la fonction trie la liste d'entrée dans l'ordre croissant
    liste = [3, 2, 1]
    sortie_attendue = [1, 2, 3]
    assert trier_liste(liste) == sortie_attendue

def test_liste_avec_elements_de_types_differents():
    # Vérifie que la fonction renvoie une erreur si la liste d'entrée contient des éléments de types différents
    liste = [1, 2, "a", "b", True, False]
    with pytest.raises(ValueError):
        trier_liste(liste)
