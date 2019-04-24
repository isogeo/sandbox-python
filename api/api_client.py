# -*- coding: UTF-8 -*-
#! python3

""" Classe permettant de se connecter à l'API isogeo en lecture
via un fichier json d'authentification.
 """

# ############################################################################
# ########## Libraries #############
# ##################################

#Standard library
import json 

#Package
from isogeo_pysdk import Isogeo, IsogeoUtils
utils = IsogeoUtils()

# ############################################################################
# ########## Class #############
# ##################################
class isogeo_API(Isogeo): #Une classe qui hérite de la classe Isogeo
     def __init__(self, file_name):
          # création du chemin vers le fichier d'authentification
          self.json_file = "{}/{}".format("/".join(__file__.split("\\")[:-1]), file_name)
          # récupérétion des informations d'authentification contenues dans le fichier
          self.client_id = utils.credentials_loader(self.json_file).get("client_id")
          self.client_secret = utils.credentials_loader(self.json_file).get("client_secret")
          # connexion à l'API et récupération du token 
          self.isogeo = Isogeo(client_id = self.client_id, client_secret = self.client_secret)
          self.token = self.isogeo.connect()
     
     # Méthode permettant d'effectuer les différents types de requête à l'API
     def request_Maker(self, filter_request = 0, filter_query = ""):
          if filter_request == 1:
               search = self.isogeo.search(whole_share = 0, page_size = 0, augment = 0, tags_as_dicts = 1, query = filter_query)
          else :
               search = self.isogeo.search(whole_share = 0, page_size = 0, augment = 0, tags_as_dicts = 1)
          # retourne les valeurs des champs ainsi que le nombre de métadonnées filtrées
          return search.get("tags"), search.get("total") 