# Modélisation d'un potager par une matrice
if __name__ == "__main__":
    from genere_potager import genere_potager
    from conflits import conflits
    from correction import correction_globale
    plantes = [("Concombres", 5,), ("Haricot", 3), ("Choux", 2)]
    n = 5
    terrain = genere_potager(plantes)
    print(terrain)
    print(conflits(terrain))
    # terrain = correction_locale(terrain=terrain, locA=(1,0))
    terrain = correction_globale(terrain=terrain)
    print(terrain)
    print(conflits(terrain))
