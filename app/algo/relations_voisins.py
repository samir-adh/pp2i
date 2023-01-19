import numpy as np
from Plante import mul


def relations_voisins(terrain: np.ndarray, i: int, j: int) -> np.ndarray:
    """Fonction servant à obtenir des informations sur les relations entre la plante en position (i,j) et ses voisines"""
    voisins = np.zeros((3, 3))
    dl = [-1, 0, 1]
    # On s'interresse à chacun des voisines directes de la plante et on regarde ses relations avec celles-ci
    for di in dl:
        for dj in dl:
            if (i + di) in range(0, terrain.shape[0]) and (j + dj) in range(0, terrain.shape[1]):
                voisins[di + 1, dj +
                        1] = mul(terrain[i, j], terrain[i + di, j + dj])
            else:
                voisins[di + 1, dj + 1] = None
    return voisins
