#!/usr/bin/python3
# -*-coding:utf-8 -*

# ============================================================================
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
interface = PanedWindow(window, 
        orient=HORIZONTAL)
game = PanedWindow(interface, 
        orient=VERTICAL)
menu = PanedWindow(interface, 
        orient=VERTICAL)
# Les 2 frames suivantes contiendront plus tard des informations sur les
# 2 joueurs et leurs score (pions bloqués par exemple)
j2_infos = PanedWindow(game,
        orient=HORIZONTAL)
j1_infos = PanedWindow(game,
        orient=HORIZONTAL)
grid_canvas = (Canvas(game, 
                    width=NB_COLS*SCALE, 
                    height=NB_ROWS*SCALE, 
                    highlightthickness=0))

# Objets interactifs (boutons / champs de saisies / etc...)
btn_start = Button(menu, 
        text="DEBUT DE PARTIE", 
        bg="#848484",
        highlightbackground="#424242")
btn_middle = Button(menu, 
        text="MI-PARTIE", 
        bg="#848484",
        highlightbackground="#424242")
btn_end = Button(menu, 
        text="FIN DE PARTIE", 
        bg="#848484",
        highlightbackground="#424242")
btn_send = Button(menu,
        text="TESTER", 
        bg="#848484",
        highlightbackground="#424242")
fld_position = Entry(menu,
        width=7,)


#=========================
# DOCUMENTATION

""" 
-> Schéma de l'interface graphique

[-------------interface------------]
[-------game-------] [----menu-----]

|===================|==============|
| j2_infos          |              |
|___________________| btn_start    |
|                   | btn_middle   |
|                   | btn_end      |
| grid_frame        |              |
|                   |              |
|                   | fld_position |
|___________________| btn_send     |
| j1_infos          |              |
|___________________|______________|             
"""


#=========================
# FONCTIONS

# Dessine la grille
def draw_grid(canvas, grid):
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

# Dessine les pions sur la grille
def draw_tokens(canvas, grid):
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

# Initialise une liste de listes représentant les pions 
# [couleur, coordonée_x, coordonée_y]
def init_grid_start():

    return [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 2],
            [2, 2, 2, 2, 2]]
                
def init_grid_middle():

    return [[1, 2, 1, 2, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 2],
            [2, 1, 2, 0, 1],
            [2, 0, 1, 0, 2]]  
    
def init_grid_end():

    return [[2, 1, 0, 2, 1],
            [1, 0, 0, 1, 0],
            [2, 0, 0, 0, 1],
            [0, 1, 0, 0, 2],
            [2, 0, 2, 1, 2]]
            
# Affichage de game (colonne de gauche de l'interface).
# Cette fonction fait appel à la fonction draw_grid(...) pour afficher 
# la grille.
def show_game(game, j2_infos, grid_canvas, j1_infos, grid):
    # Affichage de la colone game aligné en haut de l'interface
    game.pack(side=TOP)

    player2_name = Label(j2_infos, text="Joueur 2")
    player2_name.pack(side=LEFT)
    game.add(j2_infos, sticky="nw")

    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    game.add(grid_canvas)

    player1_name = Label(j1_infos, text="Joueur 1")
    player1_name.pack(side=LEFT)
    game.add(j1_infos, sticky="nw")

    return game

def show_menu(menu, btn_start, btn_middle, btn_end):
    # Affichage de la colone menu aligné en haut de l'interface
    menu.pack(side=TOP)

    menu.add(Label(text="Choisissez une configuration :"), sticky="nw")
    menu.add(btn_start, width=135, sticky="nw")
    menu.add(btn_middle, width=135, sticky="nw")
    menu.add(btn_end, width=135, sticky="nw")
    menu.add(Label(text="\n" + 
            "Teste si une case est dans la grille, \n" +
            "Format autorisé (x, y) [ex: (0, 4)] :"
            , justify=LEFT), sticky="nw")
    menu.add(fld_position, sticky="nw")
    fld_position.focus()
    menu.add(btn_send, sticky="nw")

    return menu

# Fonction est_dans_grille, mais comme depuis le début, j'avais écris mes 
# fonctions en anglais, celle là n'échappe pas à la règle...
# Non mais en vrai, ça aurait fait tâche dans le code.
def in_grid(position):
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

    assert 0<=position[0]<5 and 0<=position[1]<5, "ERREUR_COORDONEES :" \
            + "Les coordonées ne font pas partie de la grille."
            
    print("la case fait bien partie de la grille")


#=========================
# EVENEMENTS

# Ces fonctions sont un peu spéciales.
# Elles sont déclenché par un evenement.
# Ici, l'evenement en question sera le clic sur un bouton.

def event_change_config_to_begin(grid, grid_canvas):
    grid = init_grid_start()
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()

def event_change_config_to_middle(grid, grid_canvas):
    grid = init_grid_middle()
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()

def event_change_config_to_end(grid, grid_canvas):
    grid = init_grid_end()
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()

def event_test_in_grid(position):
    in_grid(position)

#=========================
# MAIN

# Initialisation et affichage de la grille
# et de l'interface.
grid = init_grid_start()
interface.add(show_game(game, j2_infos, grid_canvas, j1_infos, grid))
interface.add(show_menu(menu, btn_start, btn_middle, btn_end))
interface.pack()

# Ajout des évenements aux boutons.
btn_start.config(command=lambda : event_change_config_to_begin(grid, grid_canvas))
btn_middle.config(command=lambda : event_change_config_to_middle(grid, grid_canvas))
btn_end.config(command=lambda : event_change_config_to_end(grid, grid_canvas))
btn_send.config(command=lambda : event_test_in_grid(fld_position.get()))

# Renommage de la fenetre
window.title("Entropie")
window.resizable(False, False)
# Affichage de la fenetre
window.mainloop()