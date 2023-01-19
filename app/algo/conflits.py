from Plante import mul
import numpy as np


def conflits(terrain: np.ndarray) -> list:
    """Fonction identifiant les conflit dans le potager en renvoyant une liste les paires de positions des plantes qui ne s'associent pas entre elles"""
    n, m = terrain.shape
    # La fonction 'in_range' nous permettra d'éviter de regarder des indices hors de portée
    def in_range(i, j):
        return (i + di) in range(0, n) and (j + dj) in range(0, m)
    dl = [-1, 0, 1]
    liste_conflits = []
    for i in range(n):
        for j in range(m):
            # les di représentent les déplacements verticaux sur le potager
            for di in dl:
                # les dj représentent les déplacements horizontaux sur le potager
                for dj in dl:
                    # Pour chaque plante on regarde si elle est en conflit avec l'une de ses voisines 
                    if in_range(i + di, j + dj) and (di, dj) != (0, 0) and mul(terrain[i, j], terrain[i + di, j + dj]) == -1:
                        # Le cas échéant on ajoute celle-ci et sa voisine problématique à la liste
                        liste_conflits.append(((i, j), (i + di, j + dj)))
    return liste_conflits