""" Script contenant les fonctions permettant de se connecter à l'API isogeo en lecture
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

# Extract filters' values from an API request in a meta dictionnary
def get_Filters_Values(search):
     dict_Filters_Values = {"keyword":{}, "owner":{}, "type":{}, "format":{}, "provider":{}}
     if search.get("total") > 0:
          all_tags = search.get("tags")
          for tag in all_tags:
               if tag.split(":")[0] in dict_Filters_Values:
                    dict_Filters_Values[tag.split(":")[0]][tag]=all_tags[tag]

     return dict_Filters_Values