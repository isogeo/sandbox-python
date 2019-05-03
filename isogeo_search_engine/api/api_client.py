# -*- coding: UTF-8 -*-
#! python3

""" A module to connect and request Isogeo's API.
"""

# ############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import json
import os

# Package
from isogeo_pysdk import Isogeo, IsogeoUtils

utils = IsogeoUtils()

# ############################################################################
# ########## Class #############
# ##################################


class IsogeoAPI:  # Une classe qui hérite de la classe Isogeo
    """ Make easier connecting and requesting to Isogeo's API using isogeo-pysdk package.
    Online resources:
    * Full isogeo-pysdk doc at : https://isogeo-api-pysdk.readthedocs.io/en/latest/index.html
    * Full Isogeo's API doc at : http://help.isogeo.com/api

    :param str file_name: name of the credential file
    """

    def __init__(self, file_name: str = "client_secrets.json") -> object:
        # création du chemin vers le fichier d'authentification
        self.dir_path = os.path.dirname(__file__)
        self.auth_file_name = file_name
        self.auth_file_path = os.path.join(self.dir_path, self.auth_file_name)

        # récupérétion des informations d'authentification contenues dans le fichier
        self.client_id = utils.credentials_loader(self.auth_file_path).get("client_id")
        self.client_secret = utils.credentials_loader(self.auth_file_path).get(
            "client_secret"
        )
        # connexion à l'API et récupération du token
        self.isogeo = Isogeo(client_id=self.client_id, client_secret=self.client_secret)
        self.token = self.isogeo.connect()

    # Méthode permettant d'effectuer les différents types de requête à l'API
    def request_maker(
        self, filter_request: bool = False, filter_query: str = None
    ) -> tuple:
        """Request API about the resources shared with the application wich credential file allow access.
        Using a method of isogeo_pysdk's Isogeo class to return the number and the tags of searched resources.

        :param bool filter_request: 0 [DEFAULT] to search all the resources shared in the application / 1 to filter the request
        :param str filter_query: with filter_request = True, character string for 'query' parameter of * isogeo_pysdk.Isogeo.search() * method
        """

        if not isinstance(filter_request, bool):
            raise TypeError("'filter_request' parameter must be boolean")

        if filter_request:
            if not isinstance(filter_query, str):
                raise TypeError("'filter_query' parameter must be a string")
            search = self.isogeo.search(
                whole_share=0,
                page_size=0,
                augment=0,
                tags_as_dicts=1,
                query=filter_query,
            )
        else:
            search = self.isogeo.search(
                whole_share=0, page_size=0, augment=0, tags_as_dicts=1
            )
        # retourne les valeurs des champs ainsi que le nombre de métadonnées filtrées
        return search.get("tags"), search.get("total")


if __name__ == "__main__":

    pass
