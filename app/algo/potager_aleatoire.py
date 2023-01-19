import numpy as np
from Plante import Plante


def potager_aleatoire(n: int) -> np.ndarray:
    """Fonction qui renvoie une configuration aléatoire d'un potager de taille (n,n), utile pour les test des fonctions de correction"""
    noms_plante = ["Tomates", "Salade",
                   "Epinard", "Carotte", "Poireau", "Oignon"]
    terrain = np.ndarray(shape=(n, n), dtype=Plante)
    for i in range(n):
        for j in range(n):
            terrain[i, j] = Plante(
                nom=noms_plante[np.random.randint(len(noms_plante))])
    return terrain