""" Script permettant d'accéder à l'API Isogeo en lecture
 """

# ############################################################################
# ########## Libraries #############
# ##################################

#Standard library
import json 

#Package
from isogeo_pysdk import Isogeo, IsogeoUtils, __version__
utils = IsogeoUtils()

# ############################################################################
# ########## FUNCTIONS #############
# ##################################

# API authentification with json file
def API_auth(jsonFile):
     api_credentials = utils.credentials_loader(jsonFile)
     isogeo = Isogeo(client_id=api_credentials.get("client_id"), client_secret=api_credentials.get("client_secret"))
     token = isogeo.connect()

     return isogeo, token

# Make request to the API
def API_request_Maker(auth, filter_query = "", request_all = 1):
     if request_all == 1:
          search = auth[0].search(auth[1], whole_share = 0, page_size = 0, augment=0)
     else :
          search = auth[0].search(auth[1], whole_share = 0, page_size = 0, augment=0, query = filter_query)

     return search

# Write the result of the request in a json file
def json_request_Writer(search, title):
     with open("{}.json".format(title), "w") as json_basic:
          json.dump(search,
                         json_basic,
                         sort_keys=True,
                         indent=4,
                         )

# Extract filters' values from an API request
def get_Filters_Values(search):
     dict_Filters_Values = {"keyword":{}, "owner":{}, "type":{}, "format":{}, "provider":{}}
     if search.get("total") > 0:
          all_tags = search.get("tags")
          for tag in all_tags:
               if tag.split(":")[0] in dict_Filters_Values:
                    dict_Filters_Values[tag.split(":")[0]][tag]=all_tags[tag]

     return dict_Filters_Values

# ############################################################################
# ########## SCRIPT #############
# ##################################

trad_Filtres = {"Mot-clef":"keyword",
                    "Groupe de travail":"owner",
                    "Type":"type",
                    "Format":"format",
                    "Fournisseur":"provider"}

# CONNEXION A L'API 
auth = API_auth("client_secrets.json")


# TEST RECUPERATION DES VALEURS INITIALES
# requete initiale
search_all = API_request_Maker(auth = auth, request_all = 1)

# écriture du résultat dans un fichier json
#json_request_Writer(search_all, "api_searchAll")

# récupération des valeurs
dico_Filtres = get_Filters_Values(search_all)

# affichage des valeurs
""" for filtre in dico_Filtres:
     print(filtre, " ===> ", dico_Filtres[filtre]) """


# TEST RECUPERATION DES VALEURS D'ACTUALISATION
# requete secondaire:
filter_type_str = "type:vector-dataset format:shp"
search_type = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_type_str)
json_request_Writer(search_type, "api_searchtype")

dico_Filtres_test = get_Filters_Values(search_type)

print(len(dico_Filtres_test))
for filtre in dico_Filtres_test:
     print(filtre, " ===> ", dico_Filtres_test[filtre])



""" filter_kw_str = "keyword:isogeo:thematique-urbanisme keyword:isogeo:thematique-transports"
search_kw = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_kw_str)
json_request_Writer(search_kw, "api_searchkw")

# requete lourde
filter_kwtypeformat_str = "type:vector-dataset format:shp keyword:isogeo:thematique-transports"
search_kwtypeformat = API_request_Maker(auth = auth, request_all = 0, filter_query = filter_kwtypeformat_str)
json_request_Writer(search_kwtypeformat, "api_searchkwtypeformat") """