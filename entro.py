#!/usr/bin/python3
# -*-coding:utf-8 -*

# ============================================================================
#  ______       _
# |  ____|     | |                            
# | |__   _ __ | |_ _ __ ___      _ __  _   _ 
# |  __| | '_ \| __| '__/ _ \    | '_ \| | | |
# | |____| | | | |_| | | (_) |  _| |_) | |_| |
# |______|_| |_|\__|_|  \___/  (_) .__/ \__, |
#                                | |     __/ |
#                                |_|    |___/ 
# ---------------------------------------------------------------------------
#
# projet : Entropie
# fichier : entropie.py
# Auteur : 😎 On a dit ANONYME !
# MAJ : 13/02/18
# ----------------------------------------------------------------------------
# 
# Plan :
#   ø CONSTANTES
#   ø VARIABLES
#       -> Conteneurs grille & pions
#       -> Variables graphiques
#       -> Objets interactifs
#   ø DOCUMENTATION
#       -> Schéma de l'interface graphique
#   ø FONCTIONS
#   ø EVENEMENTS
#   ø MAIN (CODE PRINCIPAL)
# ----------------------------------------------------------------------------
#
# Remarques : Ceci est un petit mot à l'atention de mes correcteurs.
# J'ai codé ce jeu avec la bibliothèque tkinter. c'est une bibliothèque
# intégré de base dans python3 et la version 3 est obligatoire pour le projet
# (c'est marqué dans les consignes) donc pas d'excuses mécréants ! 😇
# J'ai fait pas mal d'efforts pour que le commentaire, la documentaion 
# et mes fonctions soient le plus claire possible et j'espère que ça le sera 
# suffisamment. 
# ----------------------------------------------------------------------------
# 
# © copyright : Ce code est certainement soumis à des trucs beaucoup
# trop obscurs et chiants pour que vous puissiez l'utiliser sans que l'auteur
# ait le courage de vous en tenir rigueur.
# ============================================================================

from tkinter import *

#=========================
# CONSTANTES

SCALE = 50          # Taille d'une cell de la grille
NB_COLS = 5         # Nombre de cols de la grille
NB_ROWS = 5         # Nombre de rows de la grille
PINK = "#ff1493"    # Couleur pions j1
CYAN = "#00ffff"    # Couleur pions j2
# Taille des pions
TOKEN_MARGIN = 10


#=========================
# VARIABLES

# Conteneurs grille & pions
grid = []
tokens = []

# Variables graphiques
window = Tk()
interface = Frame(window,
        bg="#242424")
game = Frame(interface,
        bg="#242424")
menu = Frame(interface,
        bg="#242424")
lbl_j2 = Label(game,
        bg="#242424",
        fg=PINK)
lbl_j1 = Label(game,
        bg="#242424",
        fg=CYAN)
grid_canvas = (Canvas(game, 
        width=NB_COLS*SCALE, 
        height=NB_ROWS*SCALE, 
        highlightthickness=0))

# Scores joueurs
score_j1 = IntVar(game, value=0)
score_j2 = IntVar(game, value=0)

# Objets interactifs (boutons / champs de saisies / etc...)
btn_start = Button(menu, 
        text="DEBUT DE PARTIE", 
        bg="#848484",
        width=14,
        highlightbackground="#424242")
btn_middle = Button(menu, 
        text="MI-PARTIE", 
        bg="#848484",
        width=14,
        highlightbackground="#424242")
btn_end = Button(menu, 
        text="FIN DE PARTIE", 
        bg="#848484",
        width=14,
        highlightbackground="#424242")
btn_send = Button(menu,
        text="TESTER", 
        bg="#848484",
        highlightbackground="#424242")
fld_position = Entry(menu,
        width=7,
        bg="#DADADA",
        fg="#242424")


#=========================
# DOCUMENTATION

""" 
-> Schéma de l'interface graphique

[-------------interface------------]
[-------game-------] [----menu-----]

|===================|==============|
| lbl_j2            |              |
|___________________| btn_start    |
|                   | btn_middle   |
|                   | btn_end      |
| grid_frame        |              |
|                   |              |
|                   | fld_position |
|___________________| btn_send     |
| lbl_j1            |              |
|___________________|______________|             
"""


#=========================
# FONCTIONS

def draw_grid(canvas, grid):
    """
    ø parametres :
        -> canvas : tkinter.Canvas()
        -> grid : list
    ø retour :
        -> None
    **  Dessine la grille, precedement initialisee dans grid, 
        sur le canvas
    """
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            # Variables de position (x1, y1) et (x2, y2) pour les rectangles
            x1 = col*SCALE
            y1 = row*SCALE
            x2 = col*SCALE+SCALE
            y2 = row*SCALE+SCALE

            # Création des rectangles gris foncés
            # représentant les cases de la grille
            if (row+col)%2 == 0:
                canvas.create_rectangle(x1, y1, x2, y2, 
                        fill="#424242")

            # Création des rectangles gris clair
            # représentant les cases de la grille
            else:
                canvas.create_rectangle(x1, y1, x2, y2, 
                        fill="#848484")
# end def

def draw_tokens(canvas, grid):
    """
    ø parametres :
        -> canvas : tkinter.Canvas()
        -> grid : list
    ø retour :
        -> None
    **  Dessine les pions, precedement initialisee dans grid, 
        dans le canvas
    """
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            # Variables de position (x1, y1) et (x2, y2) pour les rectangles
            x1 = col*SCALE + TOKEN_MARGIN
            x2 = row*SCALE + TOKEN_MARGIN
            y1 = col*SCALE+SCALE - TOKEN_MARGIN
            y2 = row*SCALE+SCALE - TOKEN_MARGIN

            # Création des ronds représentant les pions roses.
            if grid[row][col]==1:
                canvas.create_oval(x1, x2, y1, y2, fill=PINK)

            # Création des ronds représentant les pions roses.
            elif grid[row][col]==2:
                canvas.create_oval(x1, x2, y1, y2, fill=CYAN)
# end def

def init_grid_start():
    """
    ø parametres :
        -> None
    ø retour :
        -> list
    **  Retourne une grille en configuration "debut de partie"
    """
    return [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 2],
            [2, 2, 2, 2, 2]]
# end def                

def init_grid_middle():
    """
    ø parametres :
        -> None
    ø retour :
        -> list
    **  Retourne une grille en configuration "millieu de partie"
    """
    return [[1, 2, 1, 2, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 2],
            [2, 1, 2, 0, 1],
            [2, 0, 1, 0, 2]]  
# end def 

def init_grid_end():
    """
    ø parametres :
        -> None
    ø retour :
        -> list
    **  Retourne une grille en configuration "fin de partie"
    """
    return [[2, 1, 0, 2, 1],
            [1, 0, 0, 1, 0],
            [2, 0, 0, 0, 1],
            [0, 1, 0, 0, 2],
            [2, 0, 2, 1, 2]]
# end def
            
def set_score(lbl_j1, lbl_j2, score_j1, score_j2):
    """
    ø parametres :
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinterLabel()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
    ø retour :
        -> None
    **  Modifie les labels correspondant aux 2 joueurs pour
        corespondre a leurs scores actuel
    """
    lbl_j1.config(text="Joueur 1 : " + str(score_j1.get()) + " pions bloqués")
    lbl_j2.config(text="Joueur 2 : " + str(score_j2.get()) + " pions bloqués")
# end def

def test_etat(grid, x, y):
    """
    ø parametres :
        -> grid : list
        -> x : int
        -> y : int
    ø retour :
        -> str
    **  teste l'etat d'un pion (x, y) dans la grille en checkant autour
        de lui. Retourne son etat bloque ou isole ou juste None s'il
        n'est ni l'un ni l'autre.
    """
    allies = False
    enemies = False
    for row in range(x-1, x+2):
        for col in range(y-1, y+2):
            if est_dans_grille(str((row, col))) and (x, y) != (row, col):
                if grid[row][col] == grid[x][y]:
                    allies = True
                elif grid[row][col] + grid[x][y] == 3:
                    enemies = True
    
    if not allies and not enemies:
        return "isolated"
    elif not allies and enemies:
        return "blocked"
    else:
        return None
# end def

def calc_score(grid, score_j1, score_j2):
    """
    ø parametres :
        -> grid : list
        -> score_j1 : tkinter.IntVar()
        -> score_j1 : tkinter.IntVar()
    ø retour :
        -> None
    **  Calcule le score de chaques joueurs en fonction du nombre de ses
        pions bloques
    """
    score_j1.set(0)
    score_j2.set(0)
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            if grid[row][col] != 0 and test_etat(grid, row, col) == "blocked":
                if grid[row][col] == 1:
                    score_j2.set(score_j2.get() + 1)
                elif grid[row][col] == 2:
                    score_j1.set(score_j1.get() + 1)
# end def

def show_game(game, lbl_j2, grid_canvas, lbl_j1, grid):
    """
    ø parametres :
        -> game : tkinter.Frame()
        -> lbl_j2 : tkinter.Label()
        -> grid_canvas : tkinter.Canvas()
        -> lbl_j1 : tkinter.Label()
        -> grid : list
    ø retour :
        -> None
    **  Affichage de toute la colone gauche de l'interface
        (scores et grille)
    """
    game.pack(side=LEFT, anchor="nw")

    lbl_j2.config(text="Joueur 2 : " + str(score_j2.get()) + " pions bloqués")
    lbl_j2.pack(anchor="w")

    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    grid_canvas.pack(anchor="w")

    lbl_j1.config(text="Joueur 1 : " + str(score_j1.get()) + " pions bloqués")
    lbl_j1.pack(anchor="w")
# end def

def show_menu(menu, btn_start, btn_middle, btn_end):
    """
    ø parametres :
        -> menu : tkinter.Frame()
        -> btn_start : tkinter.Button()
        -> btn_middle : tkinter.Button()
        -> btn_end : tkinter.Button()
    ø retour :
        -> None
    **  Affichage de toute la colone droite de l'interface 
        (boutons et zone de test de la fonction est_dans_grille)
    """
    menu.pack(side=LEFT, anchor="nw", padx=5)

    Label(menu, 
            text="Choisissez une configuration :", 
            bg="#242424",
            fg="#DADADA").pack(anchor="w")

    btn_start.pack(anchor="w", pady=1)
    btn_middle.pack(anchor="w", pady=1)
    btn_end.pack(anchor="w", pady=1)

    Label(menu, 
            text="\n" + 
            "Teste si une case est dans la grille, \n" +
            "Format autorise (x, y). ex: (0, 4) \n" +
            "(Resultat et erreur d'assertions dans la console)",
            justify=LEFT, 
            bg="#242424",
            fg="#DADADA").pack(anchor="w")
    
    fld_position.focus()
    fld_position.pack(anchor="w", pady=2)

    btn_send.pack(anchor="w", pady=2)
# end def

# Fonction est_dans_grille, en francais 
# car c'est une fonction qui était demandé 😇
def est_dans_grille(position):
    """
    ø parametres :
        -> position : str
    ø retour :
        -> bool
    **  Verifie le format de la position passe en parametre
        puis verifie que la position pointe bien vers une case de la
        grille.
    """
    assert position != '', "ERREUR_CHAMP_DE_SAISIE_VIDE : " \
            + "Le champ de saisie est vide. " \
            + "Vous devez le remplir avec des coordonnées, au format indiqué"

    try:
        position = eval(position)
    except:
        raise AssertionError("ERREUR_FORMAT : " \
                + "Vous devez entrer les coordonées au format (x, y). " \
                + "Par exemple (1, 3) ou (2, 0)")

    assert type(position)==tuple and len(position)==2, "ERREUR_FORMAT : " \
            + "Vous devez entrer les coordonées au format (x, y). " \
            + "Par exemple (1, 3) ou 2, 0"

    assert type(position[0])==int and type(position[1])==int, "ERREUR_TYPE :" \
            + "x et y doivent etre des des entiers."

    if 0<=position[0]<5 and 0<=position[1]<5:
        return True
    else:
        return False
# end def

#=========================
# EVENEMENTS

# Ces fonctions sont un peu spéciales.
# Elles sont déclenché par un evenement.
# Par exemple, le clic sur un bouton.

def event_change_config_to_begin(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2):
    """
    ø parametres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
    ø retour :
        -> None
    **  Change la configuration de la grille vers la config
        "debut de partie", et met a jour le score en fonction.
    """
    grid = init_grid_start()
    calc_score(grid, score_j1, score_j2)
    set_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()
# end def

def event_change_config_to_middle(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2):
    """
    ø parametres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
    ø retour :
        -> None
    **  Change la configuration de la grille vers la config
        "millieu de partie", et met a jour le score en fonction.
    """
    grid = init_grid_middle()
    calc_score(grid, score_j1, score_j2)
    set_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()
# end def

def event_change_config_to_end(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2):
    """
    ø parametres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
    ø retour :
        -> None
    **  Change la configuration de la grille vers la config
        "fin de partie", et met a jour le score en fonction.
    """
    grid = init_grid_end()
    calc_score(grid, score_j1, score_j2)
    set_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()
# end def

def event_test_est_dans_grille(position):
    """
    ø parametres :
        -> position : str
    ø retour :
        -> bool
    **  Apelle la fonction est dans grille avec la position donne en 
        parametre.
    """
    return est_dans_grille(position)
# end def

#=========================
# MAIN

# Initialisation et affichage de la grille
# et de l'interface.
grid = init_grid_start()
show_game(game, lbl_j2, grid_canvas, lbl_j1, grid)
show_menu(menu, btn_start, btn_middle, btn_end)
interface.pack()

# Ajout des évenements aux boutons.
btn_start.config(command=lambda : 
        event_change_config_to_begin(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2))
btn_middle.config(command=lambda : 
        event_change_config_to_middle(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2))
btn_end.config(command=lambda : 
        event_change_config_to_end(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2))
btn_send.config(command=lambda : 
        print(event_test_est_dans_grille(fld_position.get())))

# Ajout de l'evenement lors de la pression sur la touche entree
fld_position.bind("<Return>", 
        lambda e : print(event_test_est_dans_grille(fld_position.get())))

# Renommage de la fenetre
window.title("Entropie")
# fix de la taille de la fenetre
window.resizable(False, False)
# Affichage de la fenetre
window.mainloop()