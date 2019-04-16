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

# 3rd party
#from isogeo_pysdk import Isogeo, IsogeoUtils, __version__
#utils = IsogeoUtils()

# #############################################################################
# ########## Classes ###############
# ##################################

class filtreFrame(Frame):
    def __init__(self, parent, champ):
        # Frame parent
        Frame.__init__(self, parent, width="5c", height="2.5c")
        self.grid_propagate(0)
        self.pack()
        self.rowconfigure(1, minsize = "0.5c")
        # Label enfant
        self.lbl = Label(self, text=champ)
        self.lbl.grid(row=0, sticky="w")
        #Combobox enfant
        self.options = []
        self.cbbox=ttk.Combobox(self, values=self.options)
        self.cbbox.grid(row=2)


class Interface(Frame): #Une classe qui hérite de la classe Frame
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre, width="13c", height="12c")
        self.grid_propagate(0)
        self.pack()
        self.rowconfigure(0, minsize = 10)
        
        # BOUTON D'AUTHENTIFICATION
        # Frame parent
        self.Auth_frame = Frame(self, width="13c", height="0.75c")
        self.Auth_frame.grid_propagate(0)
        self.Auth_frame.grid(row = 1)
        self.Auth_frame.columnconfigure(0, minsize = "13c")
        # Bouton enfant
        self.Auth_btn = Button(self.Auth_frame, text = "Tester l'Authentification")
        self.Auth_btn.grid(column = 0, row =0, sticky="ns")

        # LES FILTRES et LANCEMENT
        # Frame parent filtres 
        self.Filtres_frame = Frame(self, width="13c", height="9.5c")
        self.Filtres_frame.grid_propagate(0)
        self.Filtres_frame.grid(row=2)

        mep_filtreFrame_dict = {"row0":"1c", "row2":"0.5c", "row4":"0c", "col0":"0.5c", "col4":"0.5c", "col2":"2c"}
        for dimension in mep_filtreFrame_dict:
            if dimension[0:3]=="row":
                self.Filtres_frame.rowconfigure(int(dimension[3]), minsize = mep_filtreFrame_dict[dimension])
            else :
                self.Filtres_frame.columnconfigure(int(dimension[3]), minsize = mep_filtreFrame_dict[dimension])
        
        # Frame parent Fournisseur
        self.Fourn_frame = filtreFrame(self.Filtres_frame, champ ="Fournisseur")
        self.Fourn_frame.grid(row=1, column=1)
        
        # Frame parent Groupe de travail
        self.GrpTrav_frame = filtreFrame(self.Filtres_frame, champ = "Groupe de travail")
        self.GrpTrav_frame.grid(row=1, column=3)
        
        # Frame parent Type
        self.Type_frame = filtreFrame(self.Filtres_frame, champ ="Type")
        self.Type_frame.grid(row=3, column=1)
        
        # Frame parent Mot-clef
        self.KeyW_frame = filtreFrame(self.Filtres_frame, champ ="Mot-Clef")
        self.KeyW_frame.grid(row=3, column=3)
       
        # Frame parent Format
        self.Format_frame = filtreFrame(self.Filtres_frame, champ="Format")
        self.Format_frame.grid(row=5, column=1)
       
        # Frame parent Bouton Lancement
        self.RunBtn_frame = Frame(self.Filtres_frame, width="5c", height="2.5c")
        self.RunBtn_frame.grid_propagate(0)
        self.RunBtn_frame.grid(row=5, column=3)
        self.RunBtn_frame.rowconfigure(0, minsize = "1c")
        self.RunBtn_frame.rowconfigure(1, minsize = "0.5c")
        self.RunBtn_frame.columnconfigure(0, minsize = "5c")
        # Bouton enfant
        self.Run_btn = Button(self.RunBtn_frame, text = "Lancer l'inventaire")
        self.Run_btn.grid(row =1, column=0, sticky="ew")

        #RESULTAT DE L'INVENTAIRE
        # Frame parent
        self.Result_frame = Frame(self, width="13c", height="2c")
        self.Result_frame.grid_propagate(0)
        self.Result_frame.grid(row = 3)
        self.Result_frame.rowconfigure(0, minsize = "0.5c")
        self.Result_frame.columnconfigure(0, minsize = "0.5c")
        # Texte enfant
        self.chnResult=StringVar()
        self.chnResult.set("0 métadonnées correspondantes")
        self.Result_btn = Label(self.Result_frame, textvariable = self.chnResult, justify="left")
        self.Result_btn.grid(column = 1, row =1, sticky="w")