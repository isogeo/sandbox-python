""" Script permettant de générer l'interface graphique du moteur de recherche 
 """

# ############################################################################
# ########## Libraries #############
# ##################################

#Standard library
from tkinter import *

# Package
from isogeo_pysdk import Isogeo, IsogeoUtils, __version__
utils = IsogeoUtils()


class filtreFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width="5c", height="2.5c")
        self.grid_propagate(0)
        self.pack()
        self.rowconfigure(0, minsize = 10)


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
        self.Fourn_frame = filtreFrame(self.Filtres_frame)
        self.Fourn_frame.grid(row=1, column=1)
        self.Fourn_frame.rowconfigure(1, minsize = "0.5c")
        # Label enfant
        self.Fourn_lbl = Label(self.Fourn_frame, text="Fournisseur")
        self.Fourn_lbl.grid(row=0, sticky="w")
        # Menu enfant
        self.Fourn_menuBtn = Menubutton(self.Fourn_frame, width = 30, relief = "ridge")
        self.Fourn_menuBtn.menu = Menu(self.Fourn_menuBtn, tearoff=0)
        self.Fourn_menuBtn['menu'] = self.Fourn_menuBtn.menu
        self.Fourn_menuBtn.grid(row=2)

        # Frame parent Groupe de travail
        self.GrpTrav_frame = filtreFrame(self.Filtres_frame)
        self.GrpTrav_frame.grid(row=1, column=3)
        self.GrpTrav_frame.rowconfigure(1, minsize = "0.5c")
        # Label enfant
        self.GrpTrav_lbl = Label(self.GrpTrav_frame, text="Groupe de travail")
        self.GrpTrav_lbl.grid(row=0, sticky="w")
        # Menu enfant
        self.GrpTrav_menuBtn = Menubutton(self.GrpTrav_frame, width = 30, relief = "ridge")
        self.GrpTrav_menuBtn.menu = Menu(self.GrpTrav_menuBtn, tearoff=0)
        self.GrpTrav_menuBtn['menu'] = self.GrpTrav_menuBtn.menu
        self.GrpTrav_menuBtn.grid(row=2)

        # Frame parent Type
        self.Type_frame = filtreFrame(self.Filtres_frame)
        self.Type_frame.grid(row=3, column=1)
        self.Type_frame.rowconfigure(1, minsize = "0.5c")
        # Label enfant
        self.Type_lbl = Label(self.Type_frame, text="Type")
        self.Type_lbl.grid(row=0, sticky="w")
        # Menu enfant
        self.Type_menuBtn = Menubutton(self.Type_frame, width = 30, relief = "ridge")
        self.Type_menuBtn.menu = Menu(self.Type_menuBtn, tearoff=0)
        self.Type_menuBtn['menu'] = self.Type_menuBtn.menu
        self.Type_menuBtn.grid(row=2)

        # Frame parent Mot-clef
        self.KeyW_frame = filtreFrame(self.Filtres_frame)
        self.KeyW_frame.grid(row=3, column=3)
        self.KeyW_frame.rowconfigure(1, minsize = "0.5c")
        # Label enfant
        self.KeyW_lbl = Label(self.KeyW_frame, text="Mot-Clef")
        self.KeyW_lbl.grid(row=0, sticky="w")
        # Menu enfant
        self.KeyW_menuBtn = Menubutton(self.KeyW_frame, width = 30, relief = "ridge")
        self.KeyW_menuBtn.menu = Menu(self.KeyW_menuBtn, tearoff=0)
        self.KeyW_menuBtn['menu'] = self.KeyW_menuBtn.menu
        self.KeyW_menuBtn.grid(row=2)

        # Frame parent Format
        self.Format_frame = filtreFrame(self.Filtres_frame)
        self.Format_frame.grid(row=5, column=1)
        self.Format_frame.rowconfigure(1, minsize = "0.5c")
        # Label enfant
        self.Format_lbl = Label(self.Format_frame, text="Format")
        self.Format_lbl.grid(row=0, sticky="w")
        # Menu enfant
        self.Format_menuBtn = Menubutton(self.Format_frame, width = 30, relief = "ridge")
        self.Format_menuBtn.menu = Menu(self.Format_menuBtn, tearoff=0)
        self.Format_menuBtn['menu'] = self.Format_menuBtn.menu
        self.Format_menuBtn.grid(row=2)

        # Frame parent Bouton Lancement
        self.RunBtn_frame = filtreFrame(self.Filtres_frame)
        self.RunBtn_frame.grid(row=5, column=3)
        self.RunBtn_frame.rowconfigure(0, minsize = "1c")
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
        chnResult=StringVar()
        chnResult.set("0 métadonnées correspondantes")
        self.Result_btn = Label(self.Result_frame, textvariable = chnResult, justify="left")
        self.Result_btn.grid(column = 1, row =1, sticky="w")

        
fenetre = Tk()
fenetre.title("Inventaire filtré des métadonnées")
interface = Interface(fenetre)

interface.mainloop()