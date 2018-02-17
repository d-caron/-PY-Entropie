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
TOKEN_LEN = (SCALE/5, SCALE/5, 4*SCALE/5, 4*SCALE/5)


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
j2_frame = Frame(interface)
j1_frame = Frame(interface)
grid_frame = Frame(interface)

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
entry = StringVar() #stockera en temps réel le contenu de fld_position.
fld_position = Entry(menu,
        width=7,)


#=========================
# DOCUMENTATION

""" 
-> Schéma de l'interface graphique

[-------------interface------------]
[-------game-------] [----menu-----]

|===================|==============|
| j2_frame          |              |
|___________________| btn_start    |
|                   | btn_middle   |
|                   | btn_end      |
| grid_frame        |              |
|                   |              |
|                   | fld_position |
|___________________| btn_send     |
| j1_frame          |              |
|___________________|______________|             
"""


#=========================
# FONCTIONS

# Dessine la grille
def draw_grid(parent, grid):
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            # Présentation en grille
            grid[row][col].grid(row=row, column=col)

            # Création des rectangles gris représentant les cases
            if (row+col)%2 == 0:
                grid[row][col].create_rectangle(0, 0, SCALE, SCALE, 
                        fill="#424242")
            else:
                grid[row][col].create_rectangle(0, 0, SCALE, SCALE, 
                        fill="#848484")
    
    interface.pack()
    return grid_frame

# Dessine les pions sur la grille
def draw_tokens(grid, tokens):
    for token in tokens:
        grid[token[1]][token[2]].create_oval(*TOKEN_LEN, fill=token[0])

# Initialise une liste de listes vide pour représenter la grille 
# en "2 dimensions"
def init_grid(grid_frame, grid):
    for row in range(NB_ROWS):
        grid.append([])
        for cols in range(NB_COLS):
            grid[row].append(Canvas(grid_frame, 
                    width=SCALE, 
                    height=SCALE, 
                    highlightthickness=0))

# Initialise une liste de listes représentant les pions 
# [couleur, coordonée_x, coordonée_y]
def init_tokens_start():

    return [[PINK, 0, 0], 
            [PINK, 0, 1],
            [PINK, 0, 2],
            [PINK, 0, 3],
            [PINK, 0, 4],
            [PINK, 1, 0],
            [PINK, 1, 4],
            [CYAN, 4, 0],
            [CYAN, 4, 1],
            [CYAN, 4, 2],
            [CYAN, 4, 3],
            [CYAN, 4, 4],
            [CYAN, 3, 0],
            [CYAN, 3, 4]]

def init_tokens_middle():

    return [[PINK, 0, 0], 
            [PINK, 3, 1],
            [PINK, 4, 2],
            [PINK, 0, 2],
            [PINK, 0, 4],
            [PINK, 1, 0],
            [PINK, 3, 4],
            [CYAN, 4, 0],
            [CYAN, 3, 2],
            [CYAN, 2, 4],
            [CYAN, 0, 3],
            [CYAN, 4, 4],
            [CYAN, 3, 0],
            [CYAN, 0, 1]]
    
def init_tokens_end():

    return [[PINK, 0, 1], 
            [PINK, 0, 4],
            [PINK, 1, 0],
            [PINK, 1, 3],
            [PINK, 2, 4],
            [PINK, 3, 1],
            [PINK, 4, 3],
            [CYAN, 0, 0],
            [CYAN, 0, 4],
            [CYAN, 2, 0],
            [CYAN, 3, 4],
            [CYAN, 4, 0],
            [CYAN, 4, 2],
            [CYAN, 4, 4]]

# Affichage de game (colonne de gauche de l'interface).
# Cette fonction fait appel à la fonction draw_grid(...) pour afficher 
# la grille.
def show_game(parent, j2_frame, grid_frame, j1_frame, grid):
    parent.pack(side=TOP)

    player_1_name = Label(j2_frame, text="Joueur 2")
    player_1_name.pack(side=LEFT)
    parent.add(j2_frame, sticky="nw")

    grid_frame = draw_grid(parent, grid)
    parent.add(grid_frame)

    player_2_name = Label(j1_frame, text="Joueur 1")
    player_2_name.pack(side=LEFT)
    parent.add(j1_frame, sticky="nw")

    return parent

def show_menu(parent, btn_start, btn_middle, btn_end):
    parent.config(width=280)
    parent.pack(side=TOP)

    parent.add(Label(text="Choisissez une configuration :"), sticky="nw")
    parent.add(btn_start, width=135, sticky="nw")
    parent.add(btn_middle, width=135, sticky="nw")
    parent.add(btn_end, width=135, sticky="nw")
    parent.add(Label(text="\n" + 
            "Teste si une case est dans la grille, \n" +
            "Format autorisé (x, y) [ex: (0, 4)] :"
            , justify=LEFT), sticky="nw")
    parent.add(fld_position, sticky="nw")
    fld_position.focus()
    parent.add(btn_send, sticky="nw")

    return parent

# Fonction est_dans_grille, mais comme depuis le début, j'avais écris mes 
# fonctions en anglais, celle là n'échappe pas à la règle...
# Non mais en vrai, ça aurait fait tâche dans le code.
def in_grid(position):
    assert position.get() != '', "ERREUR_CHAMP_DE_SAISIE_VIDE : " \
            + "Le champ de saisie est vide. " \
            + "Vous devez le remplir avec des coordonnées, au format indiqué"

    position = eval(position.get())

    assert type(position)==tuple and len(position)==2, "ERREUR_FORMAT : " \
            + "Vous devez entrer les coordonées au format (x, y). " \
            + "Par exemple (1, 3) ou (2, 0)"

    assert type(position[0])==int and type(position[1])==int, "ERREUR_TYPE :" \
            + "x et y doivent etre des des entiers."

    assert 0<=position[0]<5 and 0<=position[1]<5, "ERREUR_COORDONEES :" \
            + "Les coordonées ne font pas partie de la grille."
            
    print("la case fait bien partie de la grille")


#=========================
# EVENEMENTS

# Ces fonctions sont un peu spéciales.
# Elles ne prennent pas de paramètres et ont pour but de gérer un évenement
# Ici, c'est l'évenement du clic sur les boutons qui est en jeu.

def event_change_config_to_begin():
    tokens = init_tokens_start()
    draw_grid(grid_frame, grid)
    draw_tokens(grid, tokens)
    interface.pack()

def event_change_config_to_middle():
    tokens = init_tokens_middle()
    draw_grid(grid_frame, grid)
    draw_tokens(grid, tokens)
    interface.pack()

def event_change_config_to_end():
    tokens = init_tokens_end()
    draw_grid(grid_frame, grid)
    draw_tokens(grid, tokens)
    interface.pack()

def event_test_in_grid():
    in_grid(fld_position)

#=========================
# MAIN

# Initialisation et affichage de la grille
# et de l'interface.
init_grid(grid_frame, grid)
interface.add(show_game(game, j2_frame, grid_frame, j1_frame, grid))
interface.add(show_menu(menu, btn_start, btn_middle, btn_end))
interface.pack()

# Ajout des évenements aux boutons.
btn_start.config(command=event_change_config_to_begin)
btn_middle.config(command=event_change_config_to_middle)
btn_end.config(command=event_change_config_to_end)
btn_send.config(command=event_test_in_grid)

# Initialisation et affichage des pions
tokens = init_tokens_start()
draw_tokens(grid, tokens)

# Renommage de la fenetre
window.title("Entropie")
window.resizable(False, False)
# Affichage de la fenetre
window.mainloop()