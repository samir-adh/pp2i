from relations_voisins import relations_voisins
from conflits import conflits
import numpy as np
import time


def correction_locale(terrain: np.ndarray, locA: tuple) -> np.ndarray:
    """Fonction qui renvoie un potager dans lequel on a changé la place d'une plante dans une copie du potager initial pour qu'elle ne soit plus en conflit avec ses voisines"""

    # On prend connaissance de la plante ploblématique
    planteA = terrain[locA]
    n, m = terrain.shape
    # Définition d'un booléen qui nous permettra de savoir si on a réglé le problème
    corrected = False
    i = 0
    # On va échanger la plante A avec chacune des autres plantes du potager afin de toruver une configuration dans laquelle la plante A ne pose plus de conflits
    while i < n and not corrected:
        j = 0
        while j < m and not corrected:
            # On défini la plante B comme celle en position (i,j)
            planteB = terrain[i, j]
            # Il est inutile d'échanger deux plantes de la même espèce
            if planteB != None and planteB.nom == planteA.nom:
                pass
            else:
                active_config = terrain.copy()
                # Ici on échange la plante A avec la plante B
                swap(active_config, locA, (i, j))
                # On verifie que la nouvelle configuration ne génère pas de nouveaux conflits...
                if (-1 not in relations_voisins(active_config, i, j)) and (-1 not in relations_voisins(active_config, locA[0], locA[1])):
                    # Si ce n'est pas le cas on a bien une configuration viable: on a résolu le problème
                    corrected = True
            j += 1
        i += 1
    # Pour des raisons obscures, le paramètre 'terrain' ne change pas lorsque l'on fait 'terrain = terrainB', on se contente donc de renvoyer le terrain corrigé
    return active_config


def correction_globale(terrain: np.ndarray) -> np.ndarray:
    """Fonction visant à renvoyer un potager dans lequel il n'y a plus de conflits dans le positionnement des plantes"""
    active_config = terrain.copy()
    start = time.time()
    dt = 0
    configs = [(active_config,len(conflits(active_config)))]
    # On a deux conditions d'arret : plus de conflit ou l'aglorithme tourne depuis plus de 12s (dans le cas où il n'existe pas de configuration sans conflit)
    while conflits(active_config) and dt < 12:
        active_config = terrain.copy()
        liste_conflits = conflits(active_config)
        # On fait en sorte de garder des conflits uniques pour ne pas avoir à resoudre conflits déja résolus
        for conflitA in liste_conflits:
            for conflitB in liste_conflits:
                if (conflitA[1], conflitA[0]) == (conflitB[0], conflitA[1]):
                    liste_conflits.remove(active_config)
        # On resoud chaque conflit repéré à l'aide de la correction locale
        for conflit in liste_conflits:
            if active_config[conflit[0]] != None:
                active_config = correction_locale(terrain=active_config, locA=conflit[0])
        configs.append((active_config,len(conflits(active_config))))
        dt = time.time() - start
    configs.sort(key=lambda a:a[1])
    return configs[0][0]


def swap(terrain: np.ndarray, locA: tuple, locB: tuple) -> None:
    """Fonction qui échange la position de deux plantes sur le terrain """
    terrain[locA], terrain[locB] = terrain[locB], terrain[locA]


if __name__ == "__main__":
    from genere_potager import genere_potager
    from conflits import conflits
    plantes = [("Salade", 5,), ("Tomates", 3), ("Fenouil", 2)]
    n = 5
    terrain = genere_potager(plantes)
    print(terrain)
    print(conflits(terrain))
    # terrain = correction_locale(terrain=terrain, locA=(1,0))
    terrain = correction_globale(terrain=terrain)
    print(terrain)
    print(conflits(terrain))
