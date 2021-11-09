# coding=utf-8

import json 
from datetime import date

#========================================#
#  ***                           ****    #
#      CREATE-READ-UPDATE-DELETE         #
#  ***                           ****    #
#========================================#

class Models :
    """
    C'est une classe pour gérer la base de données.
    """

    def __init__ (self):
        self.file = "data.json"

    def nextId(self):
        """
        Une methode pour récuperer le prochain ID pour  la base de données.
        """
        data = self.read()
        ids = []
        for items in data["task"]:
            ids.append(items["id"])
        return max(ids) + 1

    def create (self, nom, responsable, statut , description = "", date = date.today().strftime("%d/%m/%Y")) :
        """
        Une methode pour insérer dans la base de données.
        """
        new = {
            "id": self.nextId(),
            "nom": nom,
            "responsable": responsable,
            "description": description,
            "date": date,
            "statut":statut
        }
        data = self.read()
        data["task"].append(new)
        with open(self.file, "w",encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile,ensure_ascii=False ,indent=2)
        jsonFile.close()

    def read(self) :
        """
        Une methode pour récuperer la liste de toutes les tâches.
        """
        jsonFile = open(self.file, "r",encoding='utf-8')
        data =  json.load(jsonFile)
        jsonFile.close()
        return data

    def update (self,id,  nom, responsable, statut = "En cours" , description = "", date = date.today().strftime("%d/%m/%Y")) :
        """
        Une methode pour modifier dans la base de données.
        """
        new = {
            "id": int(id),
            "nom": nom,
            "responsable": responsable,
            "description": description,
            "date": date,
            "statut":statut
        }

        data = self.read()
        for task in data["task"]:
            if task["id"] == id :
                task["nom"] = new["nom"]
                task["responsable"] = new["responsable"]
                task["description"] = new["description"]
                task["date"] = new["date"]
                task["statut"] = new["statut"]
        with open(self.file, "w",encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile,ensure_ascii=False ,indent=2)
        jsonFile.close()

    def delete(self ,id) :
        """
        Une methode pour éffacer une tâches dans la base de données.
        """
        data = self.read()
        for task in data["task"]:
            if task["id"] == id :
                data["task"].remove(task)
                break
        with open(self.file, "w",encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile,ensure_ascii=False ,indent=2)
        jsonFile.close()

    def search(self,query):
        """
        Une methode pour faire une recherche dans la base de données
        """
        data =  self.read()
        result = []

        for task in data["task"]:
            if query.lower() in task["nom"].lower() :
                result.append(task)
        return result


if __name__ == "__main__":
    print("")