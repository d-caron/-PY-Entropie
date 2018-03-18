#!/usr/bin/python3
# -*-coding:utf-8 -*

# ======================================================================
#  ______       _
# |  ____|     | |                            
# | |__   _ __ | |_ _ __ ___      _ __  _   _ 
# |  __| | '_ \| __| '__/ _ \    | '_ \| | | |
# | |____| | | | |_| | | (_) |  _| |_) | |_| |
# |______|_| |_|\__|_|  \___/  (_) .__/ \__, |
#                                | |     __/ |
#                                |_|    |___/ 
# ----------------------------------------------------------------------
#
# projet : Entropie
# fichier : entropie.py
# Auteur : 😎 On a dit ANONYME !
# MAJ : 18/03/18
# ----------------------------------------------------------------------
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
# ----------------------------------------------------------------------
#
# Remarques : Ceci est un petit mot à l'attention de mes correcteurs.
# J'ai codé ce jeu avec la bibliothèque tkinter. C'est une bibliothèque
# intégré de base dans python3 et la version 3 est obligatoire pour le 
# projet.
# (c'est marqué dans les consignes) donc pas d'excuses mécréants ! 😇
# J'ai fait pas mal d'efforts pour que le commentaire, la documentation 
# et mes fonctions soient les plus clairs possible et j'espère que ça le 
# sera suffisamment. 
# ----------------------------------------------------------------------
# 
# © copyright : Ce code est certainement soumis à des trucs beaucoup
# trop obscurs et chiants pour que vous puissiez l'utiliser sans que 
# l'auteur ait le courage de vous en tenir rigueur.
# ======================================================================

from tkinter import *

#=========================
# CONSTANTES

# ~* Propriétés fixes de la grille
NB_COLS = 5         # Nombre de colonnes de la grille
NB_ROWS = 5         # Nombre de lignes de la grille

# ~* Tailles fixes
SCALE = 50          # Taille d'une case de la grille
TOKEN_MARGIN = 10   # Taille d'un pion

# ~* Couleurs fixes
CYAN = "#00ffff"    # Couleur des pions du joueur 2
PINK = "#ff1493"    # Couleur des pions du joueur 1


#=========================
# VARIABLES

# ~* Conteneur de la grille
grid = []

# Propriétés du jeton sélectionné
token_prop = [False, None, None]
    # Cette liste contiendra les informations sur le jeton sélectionné
    #     ø [0] Un pion est-il sélectionné ?
    #           Oui -> True
    #           Non -> False
    #     ø [1] Coordonnées x du pion, s'il y a lieu (sinon, None)
    #     ø [2] Coordonnées y du pion, s'il y a lieu (sinon, None)

# Etat de la partie
victory = [False, False]
#     ø [0] Victoire (True) ou pas (False) du joueur 1
#     ø [1] Victoire (True) ou pas (False) du joueur 2

# Variables graphiques
window = Tk()
interface = Frame(window,
        bg="#242424")
game = Frame(interface,
        bg="#242424")
menu = Frame(interface,
        bg="#242424")
lbl_config = Label(menu, 
        text="Choisissez une configuration :", 
        bg="#242424",
        fg="#DADADA")
lbl_j1 = Label(game,
        bg="#242424",
        fg=CYAN) 
lbl_j2 = Label(game,
        bg="#242424",
        fg=PINK)
lbl_player = Label(menu,
        bg="#242424",
        font=(None, 21))
lbl_turn = Label(menu, 
        text="C'est votre tour", 
        bg="#242424",
        fg="#DADADA")
lbl_message = Label(menu, 
        justify=LEFT, 
        bg="#242424",
        fg="#DADADA")

grid_canvas = Canvas(game, 
        width=NB_COLS*SCALE, 
        height=NB_ROWS*SCALE, 
        highlightthickness=0)

# Scores joueurs
score_j1 = IntVar(game, value=0)
score_j2 = IntVar(game, value=0)

# Joueur courrant
current_player = IntVar(menu, value=1)

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
btn_pass = Button(menu, 
        text="PASSER SON TOUR", 
        bg="#848484",
        width=14,
        highlightbackground="#424242")


#=========================
# DOCUMENTATION

""" 
-> Schéma de l'interface graphique

[-------------interface------------]
[-------game-------] [----menu-----]

|===================|==============|
| lbl_j2            | lbl_config   |
|___________________| btn_start    |
|                   | btn_middle   |
|                   | btn_end      |
| grid_frame        | lbl_player   |
|                   | lbl_turn     |
|                   | btn_pass     |
|___________________| lbl_message  |
| lbl_j1            |              |
|___________________|______________|             
"""


#=========================
# FONCTIONS

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
            if grid[row][col] != 0 and test_state(grid, col, row) == "blocked":
                if grid[row][col] == 1:
                    score_j1.set(score_j1.get() + 1)
                elif grid[row][col] == 2:
                    score_j2.set(score_j2.get() + 1)   
# end def

def cancel_move(token_prop, grid_canvas, grid):
    """
    ø parametres :
        -> token_prop : list
        -> grid_canvas : tkinter.Canvas()
        -> grid : list
    ø retour :
        -> None
    **  Redéfinie les propriétées du jeton sélectioné à ses valeurs par
        défaut et redéssine la grille et les pions afin d'éffacer toutes
        traces d'un mouvement , ceci permettant de l'annuler.
    """
    token_prop.clear()
    token_prop.extend([False, None, None])
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
# end def

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
            y1 = row*SCALE + TOKEN_MARGIN
            x2 = col*SCALE+SCALE - TOKEN_MARGIN
            y2 = row*SCALE+SCALE - TOKEN_MARGIN

            # Création des ronds représentant les pions roses.
            if grid[row][col]==2:
                canvas.create_oval(x1, y1, x2, y2, fill=PINK)

            # Création des ronds représentant les pions roses.
            elif grid[row][col]==1:
                canvas.create_oval(x1, y1, x2, y2, fill=CYAN)
# end def

def init_grid_begin():
    """
    ø parametres :
        -> None
    ø retour :
        -> list
    **  Retourne une grille en configuration "debut de partie"
    """
    return [[2, 2, 2, 2, 2],
            [2, 0, 0, 0, 2],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
# end def

def init_grid_end():
    """
    ø parametres :
        -> None
    ø retour :
        -> list
    **  Retourne une grille en configuration "fin de partie"
    """
    return [[1, 2, 0, 1, 2],
            [2, 0, 0, 2, 0],
            [1, 0, 0, 0, 2],
            [0, 2, 0, 0, 1],
            [1, 0, 1, 2, 1]]
# end def                

def init_grid_middle():
    """
    ø parametres :
        -> None
    ø retour :
        -> list
    **  Retourne une grille en configuration "millieu de partie"
    """
    return [[2, 1, 2, 1, 2],
            [2, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 2, 1, 0, 2],
            [1, 0, 2, 0, 1]]  
# end def 

def move_token(token_prop, grid, x1, y1, x2, y2):
    """
    ø parametres :
        -> event : tkinter.Event()
        -> token_prop : list
        -> grid : list
    ø retour :
        -> None
    **  Permet de bouger le pion d'une case à une autre de la grille.
        Cette fonction fais partie d'un enssemble, apellé lors de
        l'évenement de clic sur la grille (Canvas)
    """
    token_prop[0] = False
    grid[y2][x2] = grid[y1][x1]
    grid[y1][x1] = 0
    return True
# end def

def select_token(event, grid, x, y, player, token_prop):
    # Si la case selectioné contient bien un pion du joueur courant
    if grid[y][x] == player:
        # Si le pion n'est pas bloqué ou isolé
        if test_state(grid, x, y) == None:
            token_prop[1] = x
            token_prop[2] = y
            token_prop[0] = True
            event.widget.create_rectangle(x*SCALE, y*SCALE,
                    x*SCALE+SCALE, y*SCALE+SCALE, 
                    outline="#7FFF00", width="3")
            lbl_message.config(text="\nヾ(^▽^ヾ)")

            return True

        # Si le pion est bloqué ou isolé
        else:
            lbl_message.config(text="\no(*≧□≦)o" +
            "\nCe pion ne peut pas bouger," +
            "\nil est soit isolé, soit bloqué.")

            return False
    # Si la case selectioné ne contient pas un pion 
    # du joueur courant
    else:
        lbl_message.config(text="\no(*≧□≦)o" +
            "\nCe n'est pas un de vos pions")
    
        return False
# end def

def set_player(lbl_player, player):
    if player == 1:
        color = CYAN
    else:
        color = PINK
    lbl_player.config(text="Joueur " + str(player),
            fg=color)
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

def show_blocked(player, grid, grid_canvas):
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            if grid[row][col] == player \
                    and test_state(grid, col, row) == "blocked":
                grid_canvas.create_rectangle(col*SCALE, row*SCALE,
                        col*SCALE+SCALE, row*SCALE+SCALE, 
                        outline="#FFFF00", width="3")
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

def show_isolated(grid_canvas, isolated):
    for elt in isolated:
        x = elt[1]
        y = elt[0]
        grid_canvas.create_rectangle(x*SCALE, y*SCALE,
                x*SCALE+SCALE, y*SCALE+SCALE, 
                outline="red", width="3")
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
        (le menu à droite)
    """
    menu.pack(side=LEFT, anchor="nw", padx=5)

    lbl_config.pack(anchor="w")

    btn_start.pack(anchor="w", pady=1)
    btn_middle.pack(anchor="w", pady=1)
    btn_end.pack(anchor="w", pady=1)

    set_player(lbl_player, current_player.get())
    lbl_player.pack(anchor="w", pady=1)
    lbl_turn.pack(anchor="w")

    btn_pass.pack(anchor="w", pady=1)
    lbl_message.config(text="\nヾ(^▽^ヾ)")
    lbl_message.pack(anchor="w", pady=1)
# end def

def test_between(x1, y1, x2, y2):
    # Cas bas, droite
    if x2 > x1 and y2 > y1:
        for i in range(1, x2-x1):
            if grid[y1+i][x1+i] != 0:
                return False

    # Cas droite
    elif x2 > x1 and y2 == y1:
        for i in range(1, x2-x1):
            if grid[y1][x1+i] != 0:
                return False

    # Cas haut, droite
    elif x2 > x1 and y2 < y1:
        for i in range(1, x2-x1):
            if grid[y1-i][x1+i] != 0:
                return False

    # Cas bas, gauche
    elif x2 < x1 and y2 > y1:
        for i in range(1, x1-x2):
            if grid[y1+i][x1-i] != 0:
                return False

    # Cas gauche
    elif x2 < x1 and y2 == y1:
        for i in range(1, x1-x2):
            if grid[y1][x1-i] != 0:
                return False
            
    # Cas haut, gauche
    elif x2 < x1 and y2 < y1:
        for i in range(1, x1-x2):
            if grid[y1-i][x1-i] != 0:
                return False
    
    # Cas bas
    elif x2 == x1 and y2 > y1:
        for i in range(1, y2-y1):
            if grid[y1+i][x1] != 0:
                return False

    # Cas haut
    elif x2 == x1 and y2 < y1:
        for i in range(1, y1-y2):
            if grid[y1-i][x1] != 0:
                return False

    return True
# end def

def test_direction(x1, y1, x2, y2):
    if x2 == x1 or y2 == y1 or \
            x1 - x2 == y2 - y1 or \
            x2 - x1 == y1 - y2 or \
            x2 - x1 == y2 - y1 or \
            x1 - x2 == y1 - y2:
        return True

    else:
        return False
# end def

def test_isolated(grid, player):
    isolated = []
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            if grid[row][col] == player and \
                    test_state(grid, col, row) == "isolated":
                isolated.append([row, col])
    return isolated
# end def

def test_state(grid, x, y):
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
    for row in range(y-1, y+2):
        for col in range(x-1, x+2):
            if est_dans_grille(str((row, col))) and (y, x) != (row, col):
                if grid[row][col] == grid[y][x]:
                    allies = True
                elif grid[row][col] + grid[y][x] == 3:
                    enemies = True
    
    if not allies and not enemies:
        return "isolated"
    elif not allies and enemies:
        return "blocked"
    else:
        return None
# end def

def test_victory(victory, current_player, lbl_player, score_j1, score_j2):
    if score_j1 == 7:
        print("0 True")
        victory[0] = True
    if score_j2 == 7:
        print("1 True")
        victory[1] = True
    
    if victory[0] == True and victory[1] == False:
        print("victory 1")
        trigger_victory(1, current_player, lbl_player, grid, grid_canvas)
    elif victory[1] == True and victory[0] == False:
        print("victory 2")
        trigger_victory(2, current_player, lbl_player, grid, grid_canvas)
# end def

def trigger_victory(player, current_player, lbl_player, grid, grid_canvas):
    current_player.set(player)
    lbl_player.config(text="Joueur " + str(player) + ": Victoire",
            fg="#FFFF00")
    lbl_turn.config(text="C'est fini !")
    lbl_message.config(text="\nヾ(^▽^ヾ)\n" +
            "Bravo, joueur " + str(player))

    show_blocked(player, grid, grid_canvas)
# end def

# **** #
#  FR  #
# **** #
# Les fonctions suivantes seront en francais,
# car c'était des fonctions qui étaient demandées 😇

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

def deplacement_isole(isolated, grid, grid_canvas, x1, y1, x2, y2):
    for i in range (len(isolated)):
        # Si la case destination est à coté d'un pion isolé allié:
        if y2-1 <= isolated[i][0] <= y2+1 and \
                x2-1 <= isolated[i][1] <= x2+1 and \
                isolated[i] != [y2, x2]:
            # Si la case destination n'est pas occupé:
            if grid[y2][x2] == 0:
                # Si la case destination est dans une direction valide,
                # et que les cases entre le départ et la destination 
                # sont libre:
                if test_direction(x1, y1, x2, y2) and \
                        test_between(x1, y1, x2, y2):

                    # On bouge le pion
                    return move_token(token_prop, grid, x1, y1, x2, y2)
        
    # Si la case destination n'est pas à coté d'un pion isolé allié:
    cancel_move(token_prop, grid_canvas, grid)
    show_isolated(grid_canvas, isolated)
    lbl_message.config(text="\no(*≧□≦)o" +
            "\nVous avez des pion isolé !")

    return False
# end def

def deplacement_voisin(grid, x1, y1, x2, y2):
    # S'il n'y à pas de pions sur la case destination:
    if grid[y2][x2] == 0:
        # Si la case destination est dans une direction valide,
        # et que les cases entre le départ et la destination sont libre:
        if test_direction(x1, y1, x2, y2) and \
                test_between(x1, y1, x2, y2):
            # On bouge le pion
            return move_token(token_prop, grid, x1, y1, x2, y2)
 
    cancel_move(token_prop, grid_canvas, grid)
    lbl_message.config(text="\no(*≧□≦)o" +
            "\nCette case n'est pas valide !") 

    return False
# end def

#=========================
# EVENEMENTS

# Ces fonctions sont un peu spéciales.
# Elles sont déclenché par un evenement.
# Par exemple, le clic sur un bouton.

def event_change_config_to_begin(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory):
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
    grid.clear()
    grid.extend(init_grid_begin())
    victory.clear()
    victory.extend([False, False])
    current_player.set(1)
    set_player(lbl_player, current_player.get())
    calc_score(grid, score_j1, score_j2)
    set_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()
# end def

def event_change_config_to_end(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory):
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
    grid.clear()
    grid.extend(init_grid_end())
    victory.clear()
    victory.extend([False, False])
    current_player.set(1)
    set_player(lbl_player, current_player.get())
    calc_score(grid, score_j1, score_j2)
    set_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()
# end def

def event_change_config_to_middle(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory):
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
    grid.clear()
    grid.extend(init_grid_middle())
    victory.clear()
    victory.extend([False, False])
    current_player.set(1)
    set_player(lbl_player, current_player.get())
    calc_score(grid, score_j1, score_j2)
    set_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    interface.pack()
# end def

def event_move_token(event, token_prop, 
        grid, grid_canvas,
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory, lbl_player,
        menu, current_player,
        btn_start, btn_middle, btn_end):
    x = event.x//SCALE
    y = event.y//SCALE

    if not victory[0] and not victory[1]:

        # Si aucun pion n'a encore été selectioné:
        if not token_prop[0]:
            select_token(event, grid, x, y, current_player.get(), token_prop)

        # Si un pion à déjà été sélectioné:
        elif (token_prop[1], token_prop[2]) == (x, y):
            cancel_move(token_prop, grid_canvas, grid)
        # Si un pion à déjà été sélectioné:
        else:
            isolated = []
            isolated = test_isolated(grid, current_player.get())

            # S'il existe des pions isolé pour le joueur courant:
            if len(isolated) > 0:
                # On tente un déplacement isolé
                move = deplacement_isole(isolated, grid, grid_canvas,
                        token_prop[1], token_prop[2], x, y)
            # S'il n'existe pas de pions isolé pour le joueur courant:
            else:
                # On tente un déplacement voisin
                move = deplacement_voisin(grid,
                        token_prop[1], token_prop[2], x, y)

            if move:
                calc_score(grid, score_j1, score_j2)
                set_score(lbl_j1, lbl_j2, score_j1, score_j2)
                draw_grid(grid_canvas, grid)
                draw_tokens(grid_canvas, grid)

                test_victory(victory, current_player, lbl_player,
                        score_j1.get(), score_j2.get())

                if not victory[0] and not victory[1]:
                    current_player.set(current_player.get() % 2 +1) 
                    show_menu(menu, btn_start, btn_middle, btn_end)

                interface.pack()
# end def

def event_pass(token_prop, grid_canvas, grid, current_player):
    if not victory[0] and not victory[1]:
        cancel_move(token_prop, grid_canvas, grid)
        current_player.set(current_player.get() % 2 + 1)
        set_player(lbl_player, current_player.get())

#=========================
# MAIN

# Initialisation et affichage de la grille
# et de l'interface.
grid = init_grid_begin()
show_game(game, lbl_j2, grid_canvas, lbl_j1, grid)
show_menu(menu, btn_start, btn_middle, btn_end)

interface.pack()

# Ajout des évenements aux boutons.
# Passage à la configuration début de partie
btn_start.config(command=lambda : 
        event_change_config_to_begin(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory))
# Passage à la configuration millieu de partie
btn_middle.config(command=lambda : 
        event_change_config_to_middle(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory))
# Passage à la configuration fin de partie
btn_end.config(command=lambda : 
        event_change_config_to_end(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory))
# Passer son tour
btn_pass.config(command=lambda :
        event_pass(token_prop, grid_canvas, grid, current_player))

# Ajout de l'évenement du clic sur la grille pour selectioner ou
# déplacer un pion.
grid_canvas.bind('<1>', lambda e: event_move_token(e, token_prop, 
        grid, grid_canvas,
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        victory, lbl_player, 
        menu, current_player,
        btn_start, btn_middle, btn_end))

# Renommage de la fenetre
window.title("Entro.py")
# fix de la taille de la fenetre
window.resizable(False, False)
# Affichage de la fenetre
window.mainloop()