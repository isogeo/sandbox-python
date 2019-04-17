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

# Permet de remplir les combobox de filtre avec les valeurs issues d'une requête
def field_setting(input_values, field_dict):
        for field in field_dict:
                field_values = []
                for value in input_values[field_dict[field]]:
                        field_values.append(value)
                field.config(values=field_values)

# Fonction exécutée lorsque qu'une valeur est sélectionnée dans une des combobox de filtre    
def callback_cbbox(event, field_dict, filtre, filtre_dict, request_input, api):
        # récupération et formatage de la valeur sélectionnée 
        user_value = event.widget.get()
        filtre_value = filtre_dict[user_value]
        request_input[filtre] = filtre_value
        # ajout de la valeur sélectionnée à la chaîne de caractère qui sert d'entrée à la requête d'actualisation des valeurs de champs
        filter_query_str = ""
        for filtre in request_input :
                filter_query_str += "{} ".format(request_input[filtre])
        # actualisation des valeurs des champs
        update_request = api.request_Maker(filter_request = 1, filter_query = filter_query_str)
        field_setting(input_values = update_request[0], field_dict = field_dict)
        # affichage du résultat de la requête d'actualisation
        if update_request[1] != 1:
                ui.chnResult.set("{} métadonnées trouvées".format(update_request[1]))
        else :
                ui.chnResult.set("{} métadonnée trouvée".format(update_request[1]))

# Lier les combobox de filtre à la fonction qui doit s'exécuter (callback_cbbox) lorsque l'utilisateur y sélectionne une valeur 
def field_extracting(current_values, field_dict, request_input, api):
        for field in field_dict:
                def callback_arg(event, field_dict = field_dict, filtre = field_dict[field], filtre_dict = current_values[field_dict[field]], request_input = request_input, api = api):
                        return callback_cbbox(event, field_dict, filtre, filtre_dict, request_input, api)
                field.bind('<<ComboboxSelected>>', callback_arg)

# Fonction exécutée lorsque l'utilisateur appuie sur le bouton Reset
def reset(init_request, field_dict, request_input):
        # Nettoyage des combobox de filtre
        for field in field_dict:
                field.set("")
        field_setting(input_values = init_request[0], field_dict = field_dict)

        # Nettoyage du dictionnaire de stockage des valeurs de filtre
        for filtre in request_input :
                request_input[filtre] = ""
        # Réinitialisation du résultat affiché
        ui.chnResult.set("{} métadonnées accessibles au total".format(init_request[1]))
        
# Lier le bouton Reset à la fonction qui doit s'exécuter lorsque l'utilisateur appuie dessus
def resetting(init_request, field_dict, btn, request_input):
        def reset_arg(init_request = init_request, field_dict = field_dict, request_input = request_input):
                return reset(init_request, field_dict, request_input)
        btn.config(command = reset_arg)

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
# Dictionnaire permettant de faire le lien entre le résultat des requêtes à l'API et les combobox de filtre
field_dict = {
            ui.Fourn_frame.cbbox : "providers",
            ui.GrpTrav_frame.cbbox : "owners",
            ui.Type_frame.cbbox : "types",
            ui.KeyW_frame.cbbox : "keywords",
            ui.Format_frame.cbbox : "formats"
            }
# Dictionnaire permettant de stocker les valeurs sélectionnées dans les combobox de filtre
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

# Observation du bouton Reset
resetting(init_request = init_request, field_dict = field_dict, btn = ui.Reset_btn, request_input = request_input)

# AFFICHER L'INTERFACE
fenetre.mainloop()