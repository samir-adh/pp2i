import sqlite3

conn = sqlite3.connect('app/flask/pp2i.db')
cursor = conn.cursor()
cursor.execute("""
DELETE FROM utilisateur;
""")
cursor.execute("""
DELETE FROM plan;
""")
cursor.execute("""
INSERT INTO utilisateur (idUser,motDePasse)
VALUES
    ("Romain Samba","columbia");
""")
cursor.execute("""
INSERT INTO plan (nom,fichier,creePar)
VALUES
    ("potager 1", "potager_1.png", "Romain Samba"),
    ("potager 2", "potager_2.png", "Romain Samba"),
    ("potager 3", "potager_3.png", "Romain Samba");
""")
conn.commit()
conn.close()