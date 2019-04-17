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
# ########## Class #################
# ##################################

class isogeo_SE():
    def __init__(self, api, ui):
        # ###### Attributes ########
        self.api = api
        self.ui = ui
        self.field_dict = {
                            self.ui.Fourn_frame.cbbox : "providers",
                            self.ui.GrpTrav_frame.cbbox : "owners",
                            self.ui.Type_frame.cbbox : "types",
                            self.ui.KeyW_frame.cbbox : "keywords",
                            self.ui.Format_frame.cbbox : "formats"
        }
        self.filter_output = {
                            "providers" : "",
                            "owners" : "",
                            "types" : "",
                            "keywords" : "",
                            "formats" : ""
        }

        self.init_request = self.api.request_Maker(filter_request = 0)
        self.result = self.ui.chnResult
        self.query = ""

        # ###### Functions ########
        self.set_result(self.init_request[1])
        self.fields_setting(input_request = self.init_request)
        self.field_updating()    
        self.ui.Reset_btn.config(command = self.global_resetting)
            
    def set_result(self, result):
        if result > 1:
            self.result.set("{} métadonnées trouvées".format(result))
        else : 
            self.result.set("{} métadonnée trouvée".format(result))

    def fields_setting(self, input_request):
        for field in self.field_dict:
            field_values = []
            for value in input_request[0][self.field_dict[field]]:
                field_values.append(value)
            field.config(values=field_values)

    def set_query(self):
        self.query = ""
        for output in self.filter_output :
                self.query += "{} ".format(self.filter_output[output])

    def cbbox_callback(self, event, field):
        filter_name = self.field_dict[field]
        dict_values = self.init_request[0][filter_name]
        self.filter_output[filter_name] = dict_values[event.widget.get()]

        self.set_query()
        update_request = self.api.request_Maker(filter_request = 1, filter_query = self.query)

        self.set_result(result = update_request[1])
        self.fields_setting(input_request = update_request)

    def field_updating(self):
        for field in self.field_dict:
            def cbbox_callback_arg(event, field = field):
                return self.cbbox_callback(event, field)
            field.bind('<<ComboboxSelected>>', cbbox_callback_arg)

    def global_resetting(self):
        for field in self.field_dict:
            field.set("")
            self.filter_output[self.field_dict[field]] = ""
        self.init_request = self.api.request_Maker(filter_request = 0)
        self.fields_setting(input_request = self.init_request)
        self.set_result(result = self.init_request[1])

api = isogeo_API("client_secrets.json")

fenetre = Tk()
fenetre.title("Inventaire filtré des métadonnées")
ui = Interface(fenetre)

search_engine = isogeo_SE(api = api, ui = ui)

fenetre.mainloop()