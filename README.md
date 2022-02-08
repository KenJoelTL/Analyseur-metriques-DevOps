# Analyseur de métriques

Cette application à pour but d'obtenir des métriques utiles à l'application de la méthodologie DevOps d'un projet utilisant GitHub.

## ⚡ Outils nécéssaires
- python 3.9

## 🛠️ Installation des composantes
```sh
pip install request
```

## ⚙ Configurations
Avant de démarrer le programme, veuillez configurer les variables du fichier config
```py
baseUrl = 'https://api.github.com/' ## GitHub API
repo_base_url = # repo's url
headers= # {"authorization": "token [YOUR TOKEN]"}
```

## 💻 Démarrage de l'application
```sh
# programme principal
python application.py

# script de remplissage régulier du fichier de données
python task-logger.py
```

## 📚 En savoir plus
[Lien vers le wiki](./wiki/index.md)