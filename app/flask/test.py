import sys
import numpy as np
import sqlite3
sys.path.append('/home/eleve/pvcc-grp_24/app/algo')
import conflits,correction,donnees,genere_potager,Plante,potager_aleatoire,relations_voisins
from relations_voisins import *
from potager_aleatoire import *
from Plante import *
from genere_potager import *
from donnees import *
from correction import *
from conflits import *

potager = potager_aleatoire(5)
n,m = potager.shape
res = np.full(shape=(n,m),fill_value="                                                    ")
for i in range(n):
    for j in range(m):
        res[i,j] = potager[i,j].nom


conn=sqlite3.connect('pp2i.db')
c=conn.cursor()
c.execute('INSERT INTO plan(fichier) VALUES("test")')
c.execute('SELECT * FROM plan')
print (c.fetchall())





