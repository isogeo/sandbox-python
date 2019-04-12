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

api_credentials = utils.credentials_loader("client_secrets.json")

isogeo = Isogeo(client_id=api_credentials.get("client_id"), client_secret=api_credentials.get("client_secret"))

token = isogeo.connect()

search_all = isogeo.search(token, 
                            page_size=0,  
                            whole_share=0,    
                            augment=0
                       )

""" with open("api_search_ALL.json", "w") as json_basic:
    json.dump(search_all,
                json_basic,
                sort_keys=True,
                indent=4,
                ) """

nb_MD_tot = search_all.get("total")
print("Nombre total de métadonnées accessibles : {}".format(nb_MD_tot))

all_tags = search_all.get("tags")
dico_Filtres = {"keyword":{},
                "owner":{},
                "type":{},
                "format":{},
                "provider":{}}

print("dico_Filtres avant :", dico_Filtres)

liste_Filtres = ["keyword", "owner", "type", "format", "provider"]

for tag in all_tags:
    #print(tag, "___", all_tags[tag])
    if tag.split(":")[0] in liste_Filtres:
        #print(tag)
        dico_Filtres[tag.split(":")[0]][tag]=all_tags[tag]

for filtre in dico_Filtres:
    print("dico_Filtres {} après : {}".format(filtre, dico_Filtres[filtre]))

trad_Filtres = {"Mot-clef":"keyword",
                    "Groupe de travail":"owner",
                    "Type":"type",
                    "Format":"format",
                    "Fournisseur":"provider"}