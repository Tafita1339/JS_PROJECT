# coding=utf-8

import os
from flask import Flask , request, jsonify
from models import Models
from datetime import date as d

from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

db = Models()

# Route pour la page homme
@app.route('/',methods=['GET','POST'])
def home():
	return "Bienvenu sur l'API" ,200


# La route pour voir liste des tâches
@app.route("/api/liste", methods=['GET', 'POST'])
def liste():
    try :
        all = db.read()
        return jsonify(all), 200
    except Exception as e:
        print(e)
        return jsonify({
            'status': "Il y a eu une érreur lors de la récuperation.",
        }), 502



@app.route("/api/read", methods=['GET', 'POST'])
def read():
    data = request.get_json()
    id = data.get("id")
    result = {}
    try :
        all = db.read()
        for i in all["task"]:
            if i["id"] == id:
                result = i
                break
        return result
    except Exception as e:
        print(e)
        return jsonify({
            'status': "Il y a eu une érreur lors de la récuperation.",
        }), 502


# La route pour créer des tâches
@app.route("/api/create", methods=['POST'])
def create():
    data = request.get_json() 

    nom = data.get("nom")
    responsable = data.get("responsable")
    description = data.get("description")
    date = data.get("date")
    statut = data.get("statut")
    if date == None :
        date = d.today().strftime("%d/%m/%Y")

    try :
        db.create(nom,responsable,statut,description,date)
        return jsonify({'status': "La tâche a bien été crée",}), 200
    except Exception as e:
        print(e)
        return jsonify({
                'status': "Il y a eu une érreur lors de la création.",
            }), 502


# La route pour mettre à jour les tâches
@app.route("/api/update", methods=['POST'])
def update():
    data = request.get_json()

    id = data.get("id")
    statut = data.get("statut")
    nom = data.get("nom")
    responsable = data.get("responsable")
    description = data.get("description")
    date = data.get("date")

    if date == None :
        date = d.today().strftime("%d/%m/%Y")

    if id != None and str(id).isnumeric() :
        try :
            db.update(int(id),nom,responsable,statut,description,date) 
            return jsonify({'status': "La tâche a bien été mis à jour",}), 200
        except Exception as e:
            print(e)
            return jsonify({
                'status': "Il y a eu une érreur lors de la mis à jour.",
                }), 502
    else :
        return jsonify({'status': "Il y a eu une érreur lors du mis à jours.",}), 502


# La route pour supprimer les tâches
@app.route("/api/delete", methods=['POST','DELETE'])
def delete():
    data = request.get_json()

    id = data.get("id")
    print(id)
    if id != None and str(id).isnumeric() :
        try :
            db.delete(int(id))
            return jsonify({'status': "La tâche a bien été supprimer",}), 200
        except Exception as e:
            print(e)
            return jsonify({
                'status': "Il y a eu une érreur lors de la suppréssion.",
                }), 502
    else :
        return jsonify({'status': "Il y a eu une érreur lors de la suppréssion.",}), 502 



# Pour faires des recherches ans la base de données
@app.route("/api/search", methods=['POST'])
def search():
    data = request.get_json()
    query = data.get("query")
    try :
        result = db.search(query)
        if len(result)==0 :
            return "Pas de reponse"
        else:
            res = {
                "resultat" : result
                }
            return jsonify(res), 200

    except Exception as e:
        print(e)
        return jsonify({
            'status': "Il y a eu une érreur lors de la recherche.",
            }), 502

#=========================#
#  LANCEMENT DU SERVEUR   #     
#=========================#  

if __name__=="__main__":
	app.run(host='0.0.0.0' ,port=4444,debug=True)