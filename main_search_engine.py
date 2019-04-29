# -*- coding: UTF-8 -*-
#! python3

""" Classe permettant d'assembler l'interface générée à partir de ui_objs et l'API Isogeo
à laquelle on se connecte via api_client. 
 """

# ############################################################################
# ########## Libraries #############
# ##################################

# ##### Standards ##################
import logging
from logging.handlers import RotatingFileHandler

# ##### Modules ####################
from api import api_client as api
from ui import ui_objs as ui

# ############################################################################
# ########## Log ###################
# ##################################

# création du logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# formatage des messages
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# paramétrage du fichier .log
file_handler = RotatingFileHandler('test.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
# association du logger au fichier
logger.addHandler(file_handler)
logger.info('Initialisation du fichier .log')

# ############################################################################
# ########## Class #################
# ##################################

class isogeo_searchEngine(ui.interface, api.isogeo_API):
    def __init__(self, auth_file_name):
        # ###### Attributes ########
        api.isogeo_API.__init__(self, file_name = auth_file_name)
        ui.interface.__init__(self)

        logger.info("Connexion a l'API.")
        logger.info("Token de connexion : {}".format(self.token))

        self.isogeo.get_app_properties(self.token)
        self.master.title(self.isogeo.app_properties.get("name"))

        self.field_dict = {
            self.fourn_frame.cbbox: "providers",
            self.grpTrav_frame.cbbox: "owners",
            self.type_frame.cbbox: "types",
            self.keyW_frame.cbbox: "keywords",
            self.format_frame.cbbox: "formats"
        }
        self.filter_output = {
            "providers": "",
            "owners": "",
            "types": "",
            "keywords": "",
            "formats": ""
        }

        self.init_request = self.request_Maker(filter_request=0)
        self.result = self.str_result
        self.query = ""

        # ###### Functions ########
        self.set_result(self.init_request[1])
        self.fields_setting(input_request=self.init_request)
        self.field_updating()
        self.reset_btn.config(command=self.global_resetting)
        self.search_box.bind('<FocusOut>', self.free_searching)

        self.master.quit()

    def set_result(self, result):
        if result > 1:
            self.result.set("{} métadonnées trouvées".format(result))
        else:
            self.result.set("{} métadonnée trouvée".format(result))
        logger.info("Affichage du resultat : {}.".format(result))

    def fields_setting(self, input_request):
        for field in self.field_dict:
            field_values = []
            for value in input_request[0][self.field_dict[field]]:
                field_values.append(value)
            field.config(values=field_values)
        logger.info("Remplissage des champs de filtre.")

    def set_query(self):
        self.query = ""
        self.query += "{} ".format(self.search_box.get())
        for output in self.filter_output:
                self.query += "{} ".format(self.filter_output[output])

    def cbbox_callback(self, event, field):
        filter_name = self.field_dict[field]
        dict_values = self.init_request[0][filter_name]
        self.filter_output[filter_name] = dict_values[event.widget.get()]

        self.set_query()
        update_request = self.request_Maker(
            filter_request=1, filter_query=self.query)

        self.set_result(result=update_request[1])
        self.fields_setting(input_request=update_request)
        logger.info("Interaction avec le champ '{}'".format(filter_name))
        
    def field_updating(self):
        for field in self.field_dict:
            def cbbox_callback_arg(event, field=field):
                return self.cbbox_callback(event, field)
            field.bind('<<ComboboxSelected>>', cbbox_callback_arg)

    def global_resetting(self):
        self.str_search.set("")
        for field in self.field_dict:
            field.set("")
            self.filter_output[self.field_dict[field]] = ""
        self.init_request = self.request_Maker(filter_request=0)
        self.fields_setting(input_request=self.init_request)
        self.set_result(result=self.init_request[1])
        logger.info("Reset global de la valeur des champs")

    def free_searching(self, event):
        self.set_query()
        self.str_result.set(self.query)
        update_request = self.request_Maker(
            filter_request=1, filter_query=self.query)
        self.set_result(result=update_request[1])
        self.fields_setting(input_request=update_request)
        logger.info("Interraction avec la barre de recherche")

# ############################################################################
# ########## Script #################
# ##################################

if __name__ == '__main__':

    search_engine = isogeo_searchEngine(auth_file_name = "client_secrets.json")

    search_engine.mainloop()
