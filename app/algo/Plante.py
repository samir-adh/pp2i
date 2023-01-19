from donnees import getRelation


class Plante():
    """Classe qui définit l'objet 'Plante' afin d'effectuer plus facilement des opération spécifiques"""
    def __init__(self, nom: str) -> None:
        # Une plante a pour unique attribut son nom
        self.nom = nom

    def __repr__(self) -> str:
        return self.nom

    
def mul(planteA, planteB):
    """Cette fonction renvoie la relation entre les deux plantes passées en argument à partir des données stockées dans la base de données"""
    if (type(planteA) == Plante) and (type(planteB) == Plante):
        return getRelation(planteA=planteA.nom, planteB=planteB.nom)
    else:
        return 0