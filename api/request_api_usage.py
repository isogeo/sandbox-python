""" Script présentant des exemples d'utilisation du module de requête via l'API isogeo
 """

# ############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import json 

# Package
from isogeo_pysdk import Isogeo, IsogeoUtils, __version__
utils = IsogeoUtils()

# Modules
from request_api_module import API_auth, API_request_Maker, get_Filters_Values 

# ############################################################################
# ########## SCRIPT #############
# ##################################
dir_file = "/".join(__file__.split("/")[:-1])

# Un dictionnaire pour la transition entre les termes retournés par la requetes et ceux utilisés dans l'interface
trad_Filtres = {"Mot-clef":"keyword",
                    "Groupe de travail":"owner",
                    "Type":"type",
                    "Format":"format",
                    "Fournisseur":"provider"}

# CONNEXION A L'API 
auth = API_auth("{}/client_secrets.json".format(dir_file))

# RÉCUPERATION DES VALEURS INITIALES
# requete initiale
search_all = API_request_Maker(auth = auth, request_all = 1)

# récupération des valeurs dans un méta dictionnaire
dico_Filtres = get_Filters_Values(search_all)

# récupération du nombre total de métadonnées accessibles dans l'application:
nb_MD_tot = search_all.get("total")


# RECUPERATION DES VALEURS D'ACTUALISATION DES CHAMPS DE FILTRE OU d'INVENTAIRE
# requete à un seul filtre : exemple du champ 'type'
filter_type_str = "type:vector-dataset" # chaîne de caractère correspondant à la valeur du paramètre 'query' pour les filtres sémantiques

search_type = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_type_str)

dico_Filtres_type = get_Filters_Values(search_type)

search_type.get("total") # récupération du nombre de métadonnées retournées

# requete à 2 filtres : exemple des champs 'type' et 'format'
filter_typeformat_str = "type:vector-dataset format:shp" # chaîne de caractère correspondant à la valeur du paramètre 'query' pour les filtres sémantiques

search_typeformat = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_typeformat_str)

dico_Filtres_typeformat = get_Filters_Values(search_typeformat)

search_typeformat.get("total") # récupération du nombre de métadonnées retournées

# requete à 1 filtre appelé 2 fois : exemple du champ 'mot-clef'
filter_kw_str = "keyword:isogeo:thematique-urbanisme keyword:isogeo:thematique-transports" # chaîne de caractère correspondant à la valeur du paramètre 'query' pour les filtres sémantiques

search_kw = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_kw_str)

dico_Filtres_kw = get_Filters_Values(search_kw)

search_kw.get("total") # récupération du nombre de métadonnées retournées

# requete à 3 filtres dont l'un est appelé deux fois : champs 'mot-clef' (x2), format et type 
filter_kwtypeformat_str = "type:vector-dataset format:shp keyword:isogeo:test keyword:inspire-theme:addresses"

search_kwtypeformat = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_kwtypeformat_str)

dico_Filtres_kwtypeformat = get_Filters_Values(search_kwtypeformat)

search_kwtypeformat.get("total") # récupération du nombre de métadonnées retournées