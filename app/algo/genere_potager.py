import numpy as np
from Plante import Plante


def genere_potager(plantes: list) -> np.ndarray:
    """
    Fonction qui génère un potager en placant chaque espèce sur un ligne.
    Un exemple d'usage de cette fonction est :
        'genere_potager(plantes=[("Concombres", 5,), ("Radis", 3), ("Choux", 2)]'
    """
    n = int(np.sqrt(sum([plante[1] for plante in plantes]))) + 1
    terrain = np.ndarray(shape=(n, n), dtype=Plante)
    plts = []
    for plante in plantes:
        for i in range(plante[1]):
            plts.append(Plante(plante[0]))

    def ligne_indice(k):
        return k // n, k % n

    for i in range(len(plts)):
        terrain[ligne_indice(i)] = plts[i]
    return terrain
