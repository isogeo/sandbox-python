# -*- coding: UTF-8 -*-
#! python3

""" Script permettant de générer l'interface graphique du moteur de recherche 
 """

# ############################################################################
# ########## Libraries #############
# ##################################

# Modules
from request_api_module import *
from user_interface import *

# ############################################################################
# ########## Functions #############
# ##################################

def field_setting(input_values, field_dict):
        for field in field_dict:
                field_values = []
                for value in input_values[field_dict[field]]:
                        field_values.append(value)
                field.config(values=field_values)

def callback_cbbox(event, field_dict, filtre, filtre_dict, request_input, api):
        user_value = event.widget.get()
        filtre_value = filtre_dict[user_value]
        request_input[filtre] = filtre_value

        filter_query_str = ""
        for filtre in request_input :
                filter_query_str += "{} ".format(request_input[filtre])

        update_request = api.request_Maker(filter_request = 1, filter_query = filter_query_str)
        field_setting(input_values = update_request[0], field_dict = field_dict)

        if update_request[1] != 1:
                ui.chnResult.set("{} métadonnées trouvées".format(update_request[1]))
        else :
                ui.chnResult.set("{} métadonnée trouvée".format(update_request[1]))

def field_extracting(current_values, field_dict, request_input, api):
        for field in field_dict:
                def callback_arg(event, field_dict = field_dict, filtre = field_dict[field], filtre_dict = current_values[field_dict[field]], request_input = request_input, api = api):
                        return callback_cbbox(event, field_dict, filtre, filtre_dict, request_input, api)
                field.bind('<<ComboboxSelected>>', callback_arg)

def run_invent(api, request_input, lbl_result):
        filter_query_str = ""
        for filtre in request_input :
                filter_query_str += "{} ".format(request_input[filtre])

        final_request = api.request_Maker(filter_request = 1, filter_query = filter_query_str)
        if final_request[1] != 1:
                lbl_result.set("{} métadonnées trouvées".format(final_request[1]))
        else :
                lbl_result.set("{} métadonnée trouvée".format(final_request[1]))

def inventory_runing(run_btn, api, request_input, lbl_result):

        def run_invent_arg(api = api, request_input = request_input, lbl_result = lbl_result):
                return run_invent(api, request_input, lbl_result)
                
        run_btn.config(command = run_invent_arg)

# ############################################################################
# ########## Script #############
# ##################################

# CONNECTION A L'API
api = isogeo_API("client_secrets.json")

# RECUPERATION DES INFORMATIONS INITIALES
init_request = api.request_Maker(filter_request = 0) # requête d'initialisation
nb_md_tot = init_request[1] # nombre total de métadonnées accessibles
init_values = init_request[0] # valeurs initiales des champs de filtre

# GENERER L'INTERFACE UTILISATEUR
fenetre = Tk()
fenetre.title("Inventaire filtré des métadonnées")
ui = Interface(fenetre)

# INITIALISATION DES DICTIONNAIRES
field_dict = {
            ui.Fourn_frame.cbbox : "providers",
            ui.GrpTrav_frame.cbbox : "owners",
            ui.Type_frame.cbbox : "types",
            ui.KeyW_frame.cbbox : "keywords",
            ui.Format_frame.cbbox : "formats"
            }

request_input = {
                "providers" : "",
                "owners" : "",
                "types" : "",
                "keywords" : "",
                "formats" : ""
                }

# Affichage du nombre total de métadonnées accessibles dans l'interface
ui.chnResult.set("{} métadonnées accessibles au total".format(nb_md_tot))

# Remplissage des champs de filtre avec les valeurs initiales
field_setting(input_values = init_values, field_dict = field_dict)

# Observation des champs pour récupérer les valeurs et les actualiser
field_extracting(current_values = init_values, field_dict = field_dict, request_input = request_input, api = api)

# Observation du bouton de lancement de l'inventaire
inventory_runing(run_btn = ui.Run_btn, api = api, request_input = request_input, lbl_result = ui.chnResult)

# AFFICHER L'INTERFACE
fenetre.mainloop()