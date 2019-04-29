# sandbox-python

Formation, montée en puissance et métaformation.

## Utilité

Sandbox-python est un **environnement de formation** permettant notamment de fixer des objectifs et des délais d'accomplissement afin d'encadrer le déroulement de la formation, d'**accompagner la montée en puissance**.

## Objectifs

* **GitHub** : L'objectif premier de la formation et de **découvrir et d'acquérir certaines pratiques de développeurs** en évoluant dans cette environnement.

* **Python** : L'objectif secondaire constitue la finalité de la formation : la **montée en puissance sur python** dans deux domaines particuliers (interface utilisateur et API isogéo).

## Finalité

Acquérir des compétences et connaissances nécessaires au **développement du plugin isogeo pour QGIS3**.

## Projet

Dans le but d'atteindre les objectifs de formation, un **moteur de recherche** faisant appel à l'**API isogeo** en lecture a été déveoppé dans ce dépôt.

## Quickstart

* Installation du package isogeo-pysdk :

```powershell
pip install isogeo-pysdk
```

* Importer les dossiers `api` et `ui` ainsi que le fichier `main_search_engine.py` et les stocker dans le **même répertoire**.

* Ajouter le **fichier `.json` d'authentification** Isogeo dans le dossier `api` (au même niveau que le fichier `api_client.py`).

* **Exécuter le script** suivant dans un interpréteur Python.

```python
# Import du module permettant de connecter l'interface utilisateur et l'API Isogeo
# (donne également accès aux modules api_client, ui_objs et tkinter)
from main_search_engine import *

# Générer le moteur de recherche connecté à l'API via le fichier json d'authentification
# (Création d'une instance de la classe "isogeo_searchEngine" du module main_search_engine)
search_engine = isogeo_searchEngine(auth_file_name = "client_secrets.json")

# Liaison de la console à l'interface graphique
search_engine.mainloop()
```
