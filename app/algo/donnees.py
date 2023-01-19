# Ce fichier definit les fonction nécessaires pour manipuler les données de la base de données
import time
import sqlite3
import pathlib

def getRelation(planteA, planteB):
    val=[]
    """Renvoie la valeur de l'association entre la planteA et la planteB"""
    path = pathlib.Path().resolve().parent.absolute()
    path = str(path)
    conn = sqlite3.connect(database='app/flask/pp2i.db')
    cursor = conn.execute(
        f'''
        SELECT posOuNeg
        FROM associations
        WHERE legume1 = '{planteA}'
            AND legume2 = '{planteB}'
        '''
    )
    for row in cursor:
        val = row[0]
    conn.close()
    return val

if __name__ == '__main__':
    planteA = 'Poireau'
    planteB = 'Concombres'
    start = time.time()
    a = getRelation(planteA,planteB)
    dt = time.time()-start
    print(a)
