import string
import random
from flask import Flask, request, render_template, flash, redirect
import sqlite3

def BDDConnect():
    bdd = sqlite3.connect('data/pp2i-s5.db')
    cursor = bdd.cursor()
    return bdd, cursor

conn=sqlite3.connect('pp2i.db')
c=conn.cursor()

c.execute("DROP TABLE IF EXISTS plan")
c.execute("DROP TABLE IF EXISTS associations")
c.execute("DROP TABLE IF EXISTS utilisateur")
c.execute("DROP TABLE IF EXISTS legumes")
c.execute("DROP TABLE IF EXISTS terrain")

c.execute("CREATE TABLE utilisateur(idUser PRIMARY KEY, motDePasse VARCHAR)")
						
c.execute("""CREATE TABLE terrain(idTerrain PRIMARY KEY,
					forme INT NOT NULL,
					orientation NOT NULL,
					dimension1 REAL NOT NULL CHECK (dimension1 > 0),
					dimension2 REAL CHECK (dimension2 >= 0 OR dimension2 ISNULL),
					dimension3 REAL CHECK (dimension3 >= 0 OR dimension3 ISNULL)); """)
		
					
c.execute("""CREATE TABLE legumes(idLegume PRIMARY KEY,
					icone TEXT NOT NULL CHECK (icone LIKE '%.jpg' OR icone LIKE '%.png'),
					hauteur REAL CHECK (hauteur > 0),
					longueur REAL CHECK (longueur > 0),
					largeur REAL CHECK (largeur > 0),
					soleil NOT NULL);""")

c.execute("""CREATE TABLE plan(idPlan PRIMARY KEY,
				 nom VARCHAR,
				 fichier VARCHAR,
				 creePar VARCHAR,
				 idTerrain,
				 legume1,
				 legume2,
				 legume3,
				 legume4,
				 legume5,
				 legume6,
				 legume7,
				 legume8,
				 legume9,
				 legume10,
				 legume11,
				 legume12,
				 legume13,
				 legume14,
				 legume15,
				 legume16,
				 legume17,
				 legume18,
				 legume19,
				 legume20,
				 CONSTRAINT creePar_idUser_fk
				  FOREIGN KEY (creePar)
				  REFERENCES utilisateur(idUser),
				 CONSTRAINT idTerrain_fk
				  FOREIGN KEY (idTerrain)
				  REFERENCES terrain(idTerrain),
				 CONSTRAINT legume1_fk
				  FOREIGN KEY (legume1)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume2_fk
				  FOREIGN KEY (legume2)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume3_fk
				  FOREIGN KEY (legume3)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume4_fk
				  FOREIGN KEY (legume4)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume5_fk
				  FOREIGN KEY (legume5)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume6_fk
				  FOREIGN KEY (legume6)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume7_fk
				  FOREIGN KEY (legume7)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume8_fk
				  FOREIGN KEY (legume8)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume9_fk
				  FOREIGN KEY (legume9)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume10_fk
				  FOREIGN KEY (legume10)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume11_fk
				  FOREIGN KEY (legume11)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume12_fk
				  FOREIGN KEY (legume12)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume13_fk
				  FOREIGN KEY (legume13)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume14_fk
				  FOREIGN KEY (legume14)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume15_fk
				  FOREIGN KEY (legume15)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume16_fk
				  FOREIGN KEY (legume16)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume17_fk
				  FOREIGN KEY (legume17)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume18_fk
				  FOREIGN KEY (legume18)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume19_fk
				  FOREIGN KEY (legume19)
				  REFERENCES legumes(idLegume),
				 CONSTRAINT legume20_fk
				  FOREIGN KEY (legume20)
				  REFERENCES legumes(idLegume));""")
				  
c.execute("""CREATE TABLE associations(legume1,
						  legume2,
						  posOuNeg INT CHECK (posOuNeg == 0 OR posOuNeg == 1 OR posOuNeg == -1),
						  CONSTRAINT assoc_pk 
						   PRIMARY KEY (legume1,legume2),
						  CONSTRAINT legume1_fk
						   FOREIGN KEY (legume1)
						   REFERENCES legumes(idLegume),
						  CONSTRAINT legume2_fk
						   FOREIGN KEY (legume2)
						   REFERENCES legumes(idLegume)
						   ); """)

conn.commit()
conn.close()

