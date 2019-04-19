# -*- coding: UTF-8 -*-
#! python3

""" Script permettant de générer l'interface graphique du moteur de recherche 
 """

# ############################################################################
# ########## Libraries #############
# ##################################

# Standard library
from tkinter import *
from tkinter import ttk

# #############################################################################
# ########## Classes ###############
# ##################################

class filterFrame(Frame):
    def __init__(self, parent, field):
        # Frame parent
        Frame.__init__(self, parent, width = "5.5c", height = "2c")
        self.grid_propagate(0)
        self.pack()
        self.rowconfigure(1, minsize = "0.5c")
        #self.columnconfigure(1, minsize = "0.3c")
        # Label enfant
        self.lbl = Label(self, text = field)
        self.lbl.grid(row = 0, sticky = "w")
        # Combobox enfant
        self.cbbox = ttk.Combobox(self, width = 22)
        self.cbbox.grid(row = 2)

class interface(Frame): #Une classe qui hérite de la classe Frame
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, window):
        Frame.__init__(self, window, width = "13c", height = "12c")
        self.grid_propagate(0)
        self.pack()
        self.rowconfigure(0, minsize = 10)
        
        # BOUTON D'AUTHENTIFICATION
        # Frame parent
        self.auth_frame = Frame(self, width = "13c", height = "0.75c")
        self.auth_frame.grid_propagate(0)
        self.auth_frame.grid(row = 1)
        self.auth_frame.columnconfigure(0, minsize = "13c")
        # Bouton enfant
        self.Auth_btn = Button(self.auth_frame, text = "Tester l'Authentification")
        self.Auth_btn.grid(column = 0, row = 0, sticky = "ns")

        # LA ZONE DE RECHERCHE DE TEXTE LIBRE:
        # Frame Parent
        self.search_frame = Frame(self, width = "13c", height = "2c")
        self.search_frame.grid(row = 2)
        self.search_frame.columnconfigure(0, minsize = "13c")
        self.search_frame.rowconfigure(0, minsize = "0.5c")
        self.search_frame.rowconfigure(2, minsize = "0.5c")

        # Zone de texte enfant
        self.str_search = StringVar()
        self.search_box = Entry(self.search_frame, textvariable = self.str_search, width = 70) 
        #self.search_box = Entry(self.search_frame, width=70)
        self.search_box.grid(row = 1)


        # LES FILTRES et LANCEMENT
        # Frame parent filtres 
        self.filters_frame = Frame(self, width="13c", height="8c")
        self.filters_frame.grid_propagate(0)
        self.filters_frame.grid(row = 3)

        filters_frame_grid = {"row0": "0.5c", "row2": "0.75c",
                              "row4": "0.75c", "col0": "1c", "col2": "1.5c", "col4": "0.5c"}
        for dimension in filters_frame_grid:
            if dimension[0:3] == "row":
                self.filters_frame.rowconfigure(int(dimension[3]), minsize = filters_frame_grid[dimension])
            else :
                self.filters_frame.columnconfigure(int(dimension[3]), minsize = filters_frame_grid[dimension])
        
        # Frame parent Fournisseur
        self.fourn_frame = filterFrame(self.filters_frame, field ="Fournisseur")
        self.fourn_frame.grid(row = 1, column = 1)
        
        # Frame parent Groupe de travail
        self.grpTrav_frame = filterFrame(self.filters_frame, field = "Groupe de travail")
        self.grpTrav_frame.grid(row = 1, column = 3)
        
        # Frame parent Type
        self.type_frame = filterFrame(self.filters_frame, field = "Type")
        self.type_frame.grid(row = 3, column = 1)
        
        # Frame parent Mot-clef
        self.keyW_frame = filterFrame(self.filters_frame, field = "Mot-Clef")
        self.keyW_frame.grid(row = 3, column = 3)
       
        # Frame parent Format
        self.format_frame = filterFrame(self.filters_frame, field= "Format")
        self.format_frame.grid(row = 5, column = 1)
       
        # Frame parent Bouton Lancement
        self.resetBtn_frame = Frame(self.filters_frame, width = "5.5c", height = "2c")
        self.resetBtn_frame.grid_propagate(0)
        self.resetBtn_frame.grid(row = 5, column = 3)
        self.resetBtn_frame.rowconfigure(0, minsize = "1c")
        self.resetBtn_frame.columnconfigure(0, minsize = "4c")
        # Bouton enfant
        self.reset_btn = Button(self.resetBtn_frame, text = "Reset", width = 20)
        self.reset_btn.grid(row = 1, column = 0, sticky = "w")

        #RESULTAT DE L'INVENTAIRE
        # Frame parent
        self.result_frame = Frame(self, width="13c", height="1c")
        self.result_frame.grid_propagate(0)
        self.result_frame.grid(row = 4)
        self.result_frame.rowconfigure(0, minsize = "0.5c")
        self.result_frame.columnconfigure(0, minsize = "1c")
        # Texte enfant
        self.str_result = StringVar()
        self.str_result.set("0 métadonnées correspondantes")
        self.result_lbl = Label(self.result_frame, textvariable = self.str_result, justify = "left")
        self.result_lbl.grid(column = 1, row = 1, sticky = "w")