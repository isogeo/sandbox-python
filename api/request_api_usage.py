# -*- coding: UTF-8 -*-
#! python3

""" Script présentant des exemples d'utilisation du module de requête via l'API isogeo
 """

# ############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import json 

# Package
from isogeo_pysdk import Isogeo, IsogeoUtils
utils = IsogeoUtils()

# Modules
from request_api_module import *

# ############################################################################
# ########## SCRIPT #############
# ##################################

# création d'une instance de la classe isogeo_API permettant d'accéder à l'API en lecture
isogeo = isogeo_API(file_name = "client_secrets.json")

# RÉCUPERATION DES VALEURS INITIALES
# requete initiale
search_all = isogeo.request_Maker(filter_request=0)

# récupération du nombre total de métadonnées accessibles dans l'application:
nb_md = search_all[1]
print("{} fiches de métadonnées accessibles au total.".format(nb_md))

# récupération d'un méta dictionnaire contenant notamment les valeurs des champs de filtres
filter_values = search_all[0]
print("Les différents formats de données accessibles : ", filter_values["formats"])

# REQUETES DE RECUPERATION DES VALEURS D'ACTUALISATION DES CHAMPS DE FILTRE OU d'INVENTAIRE
# requete à un seul filtre : exemple du champ 'type'
filter_type_str = "type:vector-dataset" # chaîne de caractère correspondant à la valeur du paramètre 'query' pour les filtres sémantiques
search_type = isogeo.request_Maker(filter_request=1, filter_query=filter_type_str)
print("{} métadonnées accessibles après avoir filtré par '{}'".format(search_type[1], filter_type_str))

# requete à 2 filtres : exemple des champs 'type' et 'format'
filter_typeformat_str = "type:vector-dataset format:shp" # chaîne de caractère correspondant à la valeur du paramètre 'query' pour les filtres sémantiques
search_typeformat = isogeo.request_Maker(filter_request=1, filter_query=filter_typeformat_str)

# requete à 1 filtre appelé 2 fois : exemple du champ 'mot-clef'
filter_kw_str = "keyword:isogeo:thematique-urbanisme keyword:isogeo:thematique-transports" # chaîne de caractère correspondant à la valeur du paramètre 'query' pour les filtres sémantiques
search_kw = isogeo.request_Maker(filter_request=1, filter_query=filter_kw_str)
print("Il reste '{}' valeurs possibles du champ 'mot-clef' après avoir appliqué le filtre '{}'".format(len(search_kw[0]["keywords"]), filter_kw_str))

# requete à 3 filtres dont l'un est appelé deux fois : champs 'mot-clef' (x2), format et type 
filter_kwtypeformat_str = "type:vector-dataset format:shp keyword:isogeo:test keyword:inspire-theme:addresses"
search_kwtypeformat = isogeo.request_Maker(filter_request=1, filter_query=filter_kwtypeformat_str)