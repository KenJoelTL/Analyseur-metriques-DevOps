import time
import os
import json
import requests
from datetime import datetime
testUrl = "https://api.github.com/microsoft/PowerToys/projects"
baseUrl_ = 'https://api.github.com/users/pascal1796/'
baseUrl = 'https://api.github.com/'
repo_base_url = 'https://api.github.com/repos/KenJoelTL/LOG680-tp01-eq08/'
api_base = 'https://api.github.com/user/repos'
headers = {"authorization": "token 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"}
project_id = 14032098


def getKanbanTaskList():
    r = requests.get(url=baseUrl+"projects/" +
                     str(project_id)+"/columns", headers=headers)
    if r.status_code == 200:
        data = r.json()
        tasks = {}
        for columns in data:
            col_title = columns["name"]
            tasks[col_title] = []
            r = requests.get(url=columns["url"]+"/cards", headers=headers)
            if r.status_code == 200:
                res = r.json()
                for cards in res:
                    r = requests.get(url=cards["content_url"], headers=headers)
                    if r.status_code == 200:
                        card = r.json()
                        card_to_save = {}
                        card_to_save["card_title"] = card["title"]
                        card_to_save["created_at"] = card["created_at"]
                        tasks[col_title].append(card_to_save)

        # chargement de fichier
        database = {}
        f = open('database.json')
        database = json.load(f)
        f.close()

        # Ajout dans l'objet de base de données
        database[datetime.now().strftime('%Y-%m-%d %H:%M')] = tasks

        # Enregistrement dans le fichier
        with open('database.json', 'w') as f:
            json.dump(database, f)


def main():
    while True:
        print("Fetching data...")
        getKanbanTaskList()
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        print("Database updated - " + now)
        time.sleep(1*60)


if __name__ == "__main__":
    main()
