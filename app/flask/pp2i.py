import sys
import os
sys.path.append(os.getcwd() + '/app/algo')
from genere_potager import genere_potager
from correction import correction_globale
from flask import *
import sqlite3
import numpy as np
from pota_to_img import pota_to_img


app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def accueil():
    return render_template("accueil.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        mdp = request.form.get("mdp")
        conn = sqlite3.connect('app/flask/pp2i.db')
        conn.commit()
        c = conn.cursor()
        c.execute("SELECT * FROM utilisateur")
        base = c.fetchall()
        c.close()
        for i in base:
            # on verifie si l'utlisateur est dans la base si oui on le ramene vers sa page avec ses plans deja fais
            if i[0] == user and i[1] == mdp:
                return redirect(f"/pageuser/{i[0]}")
        else:
            # ou créer un template avec ce message et un lien pour revenir vers le login ou aller vers nouveau compte
            return "Mot de passe ou nom d'utilisateur incorrect"
    else:
        return render_template("login.html")


@app.route("/nouveaucompte", methods=['POST', 'GET'])
def nouvcompte():
    if request.method == "GET":
        return render_template("nouveaucompte.html")
    else:
        conn = sqlite3.connect(database='app/flask/pp2i.db')
        c = conn.cursor()
        nom = request.form.get("nom")
        mdp = request.form.get("mdp")
        c.execute("INSERT INTO utilisateur VALUES(?,?)", (nom, mdp))
        conn.commit()
        conn.close()
        return redirect('/login')


@app.route("/nb/<string:user>", methods=["GET", "POST"])
def nb(user):
    if request.method == "GET":
        return render_template('nombre.html')
    else:
        nombre = request.form.get("nbfruleg")
        return redirect(f"/nouveaupotager/{user}/{nombre}")

@app.route("/nouveaupotager/<string:user>/<int:nombre>", methods=["GET","POST"])
def nouveaupota(user,nombre):
    L=[]
    if request.method=="GET":
        conn= sqlite3.connect('app/bd/legumes.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT legume1 FROM LEGUMES")
        base= c.fetchall()
        conn.commit()
        conn.close()
        return render_template("nouvpotager.html",base=base,nb=nombre)

    elif request.method== "POST":
        nom=request.form.get('nompota')
        for i in range(nombre):
            L.append([request.form.get(f"fruitslegumes{i}"),int(request.form.get(f'nbfruitlegu{i}'))])
        potager=correction_globale(genere_potager(L))
        n,m = potager.shape
        res = np.full(shape=(n,m),fill_value="                                                 ")
        for i in range(n):
            for j in range(m):
                if potager[i,j]== None:
                    res[i,j] = 'vide'
                else:
                    res[i,j]=potager[i,j].nom
                resul=res.tolist()
        resultat=pota_to_img(resul,nom)
        conn=sqlite3.connect('app/flask/pp2i.db')
        c=conn.cursor()
        c.execute("INSERT INTO plan(nom,fichier,creePar) VALUES(?,?,?)",(nom,str(resultat),user))
        conn.commit()
        conn.close()
        return render_template('resultat.html',resultat='pota/'+resultat, user=user)                                                                  # donnée qui sera utlisé ensuite pour l'algo 


@app.route("/pageuser/<string:user>")
def pageuser(user):
    conn = sqlite3.connect('app/flask/pp2i.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM plan WHERE creePar='{user}'")
    b = c.fetchall()
    conn.commit()
    conn.close()
    return render_template("pageuser.html", user=user,base=b)