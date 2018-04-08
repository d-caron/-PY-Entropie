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
# fichier : entro.py
# Auteur : 😎 On a dit ANONYME !
# MAJ : 07/04/18
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
# Remarques :
# J'ai codé ce jeu avec la bibliothèque tkinter. Pour exécuter ce 
# programme, vous aurez besoin de python en version 3 minimum.
# Documentation tkinter : http://www.effbot.org/tkinterbook/
# Téléchargement de python3 : https://www.python.org/downloads/
#
# /!\ Ce programme ne s'exécute pas sous repl.it car il nécessite une 
# interface graphique.
# Pour lancer le programme : double cliquez sur l'exécutable entro.py
# ou lancez le via un interpréteur de commande.
# ----------------------------------------------------------------------
# 
# © copyright : Ce code est certainement soumis à des trucs beaucoup
# trop obscurs et chiants pour que vous puissiez l'utiliser sans que 
# l'auteur ait le courage de vous en tenir rigueur.
# ======================================================================

from tkinter import *   # Import de la bibliothèque graphique Tkinter
from random import *    # Import de la bibliothèque random
from time import sleep  # Import de la fonction sleep de la 
                        #       bibliothèque de gestion du temps

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

### Cette ligne sers lors de l'import, a ignorer les variables
### d'entro.py (dans le fichier tests.py par exemple)
if __name__ == "__main__":
    # ~* Conteneur de la grille
    grid = []

    # ~* Propriétés du jeton sélectionné
    token_prop = [False, None, None]
        # Cette liste contiendra les informations sur le jeton sélectionné
        #     ø [0] Un pion est-il sélectionné ?
        #           Oui -> True
        #           Non -> False
        #     ø [1] Coordonnées x du pion, s'il y a lieu (sinon, None)
        #     ø [2] Coordonnées y du pion, s'il y a lieu (sinon, None)

    # ~* État de la partie
    victory = [False, False]
        #     ø [0] Victoire (True) ou pas (False) du joueur 1
        #     ø [1] Victoire (True) ou pas (False) du joueur 2

    # ~* Variables graphiques (Fenêtre / Conteneur)
    window = Tk()               # Fenêtre Principale
    interface = Frame(window,   # Sous-fenêtre Globale (dans windows)
            bg="#242424")
    game = Frame(interface,     # Sous-fenêtre de gauche "game"
            bg="#242424")       #       (dans interface)
    menu = Frame(interface,     # Sous-fenêtre de droite "menu"
            bg="#242424")       #       (dans interface)

    # ~* Variables graphiques (Labels)
    lbl_j1 = Label(game,        # Label, affiche le nom et le score
            bg="#242424",       #       du joueur 1
            fg=CYAN) 
    lbl_j2 = Label(game,        # Label, affiche le nom et le score
            bg="#242424",       #       du joueur 2
            fg=PINK)
    lbl_config = Label(menu,    # Label, demande de choisir une config'
            text="Choisissez une configuration :", 
            bg="#242424",
            fg="#DADADA")
    lbl_player = Label(menu,    # Label, affiche le nom du joueur courant
            bg="#242424",
            font=(None, 21))
    lbl_turn = Label(menu,      # Label, propose de jouer son tour
            text="C'est votre tour", 
            bg="#242424",
            fg="#DADADA")
    lbl_message = Label(menu,   # Label, affiche les messages pour le joueur
            justify=LEFT,       #       (erreurs de déplacement,
            bg="#242424",       #       félicitations en fin de partie, 
            fg="#DADADA")       #       etc.)

    # ~* Variable graphique (Zone de dessin)
    grid_canvas = Canvas(game,  # Zone de dessin de la grille de jeu
            width=NB_COLS*SCALE, 
            height=NB_ROWS*SCALE, 
            highlightthickness=0)

    # ~* État d'activation de l'IA
    ai = IntVar(value=0)
        #   0 : désactivée, 1 : activée

    # ~* Scores joueurs 1 et 2
    score_j1 = IntVar(game, value=0)
    score_j2 = IntVar(game, value=0)

    # ~* N° du joueur courant
    current_player = IntVar(menu, value=1)

    # ~* Objets interactifs (Boutons)
    btn_start = Button(menu,    # Bouton "début de partie", change la grille
            text="DEBUT DE PARTIE", 
            bg="#848484",
            width=14,
            highlightbackground="#424242")
    btn_middle = Button(menu,   # Bouton "millieu de partie",
            text="MI-PARTIE",   #       change la grille
            bg="#848484",
            width=14,
            highlightbackground="#424242")
    btn_end = Button(menu,      # Bouton "fin de partie", change la grille
            text="FIN DE PARTIE", 
            bg="#848484",
            width=14,
            highlightbackground="#424242")
    btn_pass = Button(menu,     # Bouton "passer son tour", change de joueur
            text="PASSER SON TOUR", 
            bg="#848484",
            width=14,
            highlightbackground="#424242")
    chk_ai = Checkbutton(menu,  # Check-box "Jouer contre l'IA", active l'IA
            variable=ai,
            text="Jouer contre l'IA",
            bg="#242424",
            fg="#848484",
            highlightbackground="#242424")


#=========================
# DOCUMENTATION

""" 
# ~* Schéma de l'interface graphique

[-------------interface------------]
[-------game-------] [----menu-----]

|===================|==============|
| lbl_j2            | lbl_config   |
|___________________| btn_start    |
|                   | btn_middle   |
|                   | btn_end      |
| grid_frame        | chc_ai       |
|                   | lbl_player   |
|                   | lbl_turn     |
|___________________| btn_pass     |
| lbl_j1            | lbl_message  |
|___________________|______________|             
"""


#=========================
# FONCTIONS

# ~* Fonctions d'initialisation des grilles
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
    return [[1, 2, 1, 2, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2],
            [0, 2, 2, 0, 1],
            [2, 1, 0, 0, 2]]  
# end def 

# ~* Fonctions de dessin
def draw_grid(canvas, grid):
    """
    ø paramètres :
        -> canvas : tkinter.Canvas()
        -> grid : list
    ø retour :
        -> None
    **  Dessine la grille, précédemment initialisée dans grid, 
        sur le canvas (Zone de dessin)
    """
    # Pour chaque ligne :
    for row in range(NB_ROWS):
        # Pour chaque colonne :
        for col in range(NB_COLS):
            # Variables de position (x1, y1) et (x2, y2),
            #       pour les rectangles
            x1 = col*SCALE
            y1 = row*SCALE
            x2 = col*SCALE+SCALE
            y2 = row*SCALE+SCALE

            # Création des rectangles foncés
            # représentant les cases de la grille
            if (row+col)%2 == 0:
                canvas.create_rectangle(x1, y1, x2, y2, 
                        fill="#424242")

            # Création des rectangles clairs
            # représentant les cases de la grille
            else:
                canvas.create_rectangle(x1, y1, x2, y2, 
                        fill="#848484")
# end def

def draw_tokens(canvas, grid):
    """
    ø paramètres :
        -> canvas : tkinter.Canvas()
        -> grid : list
    ø retour :
        -> None
    **  Dessine les pions, precedement initialisee dans grid, 
        dans le canvas (Zone de dessin)
    """
    # Pour chaque ligne :
    for row in range(NB_ROWS):
        # Pour chaque colonne :
        for col in range(NB_COLS):
            # Variables de position (x1, y1) et (x2, y2) 
            #       pour les ovales
            x1 = col*SCALE + TOKEN_MARGIN
            y1 = row*SCALE + TOKEN_MARGIN
            x2 = col*SCALE+SCALE - TOKEN_MARGIN
            y2 = row*SCALE+SCALE - TOKEN_MARGIN

            # Création des ovales représentant les pions roses.
            if grid[row][col]==2:
                canvas.create_oval(x1, y1, x2, y2, fill=PINK)

            # Création des ovales représentant les pions cyans.
            elif grid[row][col]==1:
                canvas.create_oval(x1, y1, x2, y2, fill=CYAN)
# end def

# ~* Fonctions d'affichage
def show_blocked(player, grid, grid_canvas):
    """
    ø paramètres :
        -> player : int
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
    ø retour :
        -> None
    **  Met en évidence tous les pions bloqués d'un joueur
    """
    # Pour chaque ligne :
    for row in range(NB_ROWS):
        # Pour chaque colonne :
        for col in range(NB_COLS):
            # Si le pion appartient au joueur courant
            #       et qu'il est bloqué
            if grid[row][col] == player \
                    and test_state(grid, col, row) == "blocked":
                # Mise en évidence du pion en l'entourant avec un
                #       rectangle
                grid_canvas.create_rectangle(col*SCALE, row*SCALE,
                        col*SCALE+SCALE, row*SCALE+SCALE, 
                        outline="#FFFF00", width="3")
# end def

def show_game(game, lbl_j2, grid_canvas, lbl_j1, grid):
    """
    ø paramètres :
        -> game : tkinter.Frame()
        -> lbl_j2 : tkinter.Label()
        -> grid_canvas : tkinter.Canvas()
        -> lbl_j1 : tkinter.Label()
        -> grid : list
    ø retour :
        -> None
    **  Affichage de toute la colonne gauche de l'interface
        (scores et grille)
    """
    game.pack(side=LEFT, anchor="nw")

    # Affichage du score du joueur 2
    lbl_j2.config(text="Joueur 2 : " + str(score_j2.get()) + " pions bloqués")
    lbl_j2.pack(anchor="w")

    # Affichage de la grille et des pions
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    grid_canvas.pack(anchor="w")

    # Affichage du score du joueur 1
    lbl_j1.config(text="Joueur 1 : " + str(score_j1.get()) + " pions bloqués")
    lbl_j1.pack(anchor="w")
# end def

def show_isolated(grid_canvas, isolated):
    """
    ø paramètres :
        -> grid_canvas : tkinter.Canvas()
        -> isolated : list
    ø retour :
        -> None
    **  Met en évidence tous les pions isolés d'un joueur
    """
    # Pour chaque pion isolé :
    for elt in isolated:
        x = elt[1]
        y = elt[0]
        # Mise en évidence du pion en l'entourant avec un
        #       rectangle
        grid_canvas.create_rectangle(x*SCALE, y*SCALE,
                x*SCALE+SCALE, y*SCALE+SCALE, 
                outline="red", width="3")
# end def

def show_menu(menu, btn_start, btn_middle, btn_end, btn_pass, chk_ai,
        lbl_config, lbl_player, lbl_turn, lbl_message,
        current_player):
    """
    ø paramètres :
        -> menu : tkinter.Frame()
        -> btn_start : tkinter.Button()
        -> btn_middle : tkinter.Button()
        -> btn_end : tkinter.Button()
        -> btn_pass : tkinter.Button()
        -> chk_ai : tkinter.Checkbutton()
        -> lbl_config : tkinter.Label()
        -> lbl_player : tkinter.Label()
        -> lbl_turn : tkinter.Label()
        -> lbl_message : tkitner.Label()
        -> current_player : tkinter.IntVar()
    ø retour :
        -> None
    **  Affichage de toute la colone droite de l'interface 
        (le menu à droite)
    """
    menu.pack(side=LEFT, anchor="nw", padx=5)

    # Affichage du message de choix de la config'
    lbl_config.pack(anchor="w")

    # Affichage des 3 boutons
    btn_start.pack(anchor="w", pady=1)
    btn_middle.pack(anchor="w", pady=1)
    btn_end.pack(anchor="w", pady=1)

    # Affichage de la check-box de sélection de l'IA
    chk_ai.pack(anchor="w", pady=1)

    # Affichage des infos à propos du joueur courant
    show_player(lbl_player, current_player.get())
    lbl_player.pack(anchor="w", pady=1)
    lbl_turn.pack(anchor="w")

    # Affichage du bouton de passage de tour
    btn_pass.pack(anchor="w", pady=1)

    # Affichage du message destiné au joueur
    #       (Erreurs, félicitations en cas de victoire)
    lbl_message.config(text="\nヾ(^▽^ヾ)")
    lbl_message.pack(anchor="w", pady=1)
# end def

def show_player(lbl_player, player):
    """
    ø paramètres :
        -> lbl_player : tkinter.Label()
        -> player : int
    ø retour :
        -> None
    **  Affiche le nom du joueur avec la couleur correspondante
    """
    # Si joueur 1 :
    if player == 1:
        # Couleur cyan
        color = CYAN
    # Si joueur 2 :
    else:
        # Couleur rose
        color = PINK
    # Affichage du nom du joueur
    lbl_player.config(text="Joueur " + str(player),
            fg=color)
# end def
            
def show_score(lbl_j1, lbl_j2, score_j1, score_j2):
    """
    ø parametres :
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinterLabel()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
    ø retour :
        -> None
    **  Modifie les labels correspondant aux 2 joueurs pour
        afficher leurs scores actuel
    """
    # Affichage du score du joueur 1
    lbl_j1.config(text="Joueur 1 : " + str(score_j1.get()) + " pions bloqués")
    # Affichage du score du joueur 2
    lbl_j2.config(text="Joueur 2 : " + str(score_j2.get()) + " pions bloqués")
# end def

# ~* Fonctions de tests
### Fonction suivante FR, car expressément demandée 😇
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

    # Si la case est bien dans la grille :
    if 0<=position[0]<5 and 0<=position[1]<5:
        return True
    # Sinon :
    else:
        return False
# end def

def test_state(grid, x, y):
    """
    ø paramètres :
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
    # Pour chaque ligne autour du pion :
    for row in range(y-1, y+2):
        # Pour chaque colonne autour du pion :
        for col in range(x-1, x+2):
            # Si la case est dans la grille et que ce n'est pas celle 
            #       du pion (au centre) :
            if est_dans_grille(str((row, col))) and (y, x) != (row, col):
                # Si c'est un allié :
                if grid[row][col] == grid[y][x]:
                    allies = True
                # Si c'est un ennemi :
                elif grid[row][col] + grid[y][x] == 3:
                    enemies = True
    
    # S'il n'y a pas d'alliés autour, ni d'ennemis :
    if not allies and not enemies:
        return "isolated"
    # S'il n'y a pas d'allié autour, mais au moins un ennemi :
    elif not allies and enemies:
        return "blocked"
    # Sinon :
    else:
        return None
# end def

def test_isolated(grid, player):
    """
    ø paramètres :
        -> grid : list
        -> player : int
    ø retour :
        -> list
    **  Teste pour chaque case de la grille, s'il existe des pions
        isolés appartenant au joueur courant.
    """
    isolated = []
    # Pour chaque ligne :
    for row in range(NB_ROWS):
        # Pour chaque colonne :
        for col in range(NB_COLS):
            # S'il existe un pion du joueur courant sur la case,
            #       et qu'il est considéré comme isolés
            if grid[row][col] == player and \
                    test_state(grid, col, row) == "isolated":
                # On l'ajoute à la liste des pions isolés
                isolated.append([row, col])
    
    # Retour de la liste des pions isolés
    return isolated
# end def

def test_direction(x1, y1, x2, y2):
    """
    ø paramètres :
        -> x1 : int
        -> y1 : int
        -> x2 : int
        -> y2 : int
    ø retour :
        -> bool
    **  Teste si la direction du déplacement est valide
    """
    # Si la direction du déplacement n'est pas haut, bas, droite, gauche
    #       ou l'une des diagonales :
    if x2 != x1 and y2 != y1 and \
            max(x1, x2) - min(x1, x2) != max(y1, y2) - min(y1, y2):
        return False

    # Sinon :
    return True
# end def

def test_between(grid, x1, y1, x2, y2):
    """
    ø paramètres :
        -> grid : list
        -> x1 : int
        -> y1 : int
        -> x2 : int
        -> y2 : int
    ø retour :
        -> bool
    **  Teste pour chaque direction s'il y a un pion entre la case
        de départ et la case de destination. Retourne False s'il y 
        à un pion, True Sinon
    """
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

    # S'il n'y à pas de pion entre la case de départ et la cible :
    return True
# end def

def test_neighbour_move(grid, x1, y1, x2, y2):
    """
    ø paramètres :
        -> grid : list
        -> x1 : int
        -> y1 : int
        -> x2 : int
        -> y2 : int
    ø retour :
        -> bool
    **  Teste si un déplacement voisin vers une cible est possible selon
        les règles du jeu.
    """
    # S'il n'y à pas de pions sur la case destination:
    if grid[y2][x2] == 0:
        # Si la case destination est dans une direction valide,
        # et que les cases entre le départ et la destination sont libre:
        if test_direction(x1, y1, x2, y2) and \
                test_between(grid, x1, y1, x2, y2):
            # On peut bouger le pion
            return True
    
    return False
# end def

def test_isolated_move(isolated, grid, x1, y1, x2, y2):
    """
    ø parametres :
        -> isolated : list
        -> grid : list
        -> y1 : int
        -> x2 : int
        -> y2 : int
        -> x1 : int
    ø retour :
        -> bool
    **  Teste si un pion peut effectuer un déplacement isolé vers une 
        cible selon les règles du jeu
    """
    # Pour chaque pion isolé allié
    for i in range (len(isolated)):
        # Si la case destination est à côté d'un pion isolé allié :
        if y2-1 <= isolated[i][0] <= y2+1 and \
                x2-1 <= isolated[i][1] <= x2+1 and \
                isolated[i] != [y2, x2]:
            # Si la case destination n'est pas occupée :
            if grid[y2][x2] == 0:
                # Si la case destination est dans une direction valide,
                #       et que les cases entre le départ et la 
                #       destination sont libre :
                if test_direction(x1, y1, x2, y2) and \
                        test_between(grid, x1, y1, x2, y2):
                    return True
    
    return False
# end def

def can_token_move(grid, x, y, player):
    """
    ø parametres :
        -> grid : list
        -> x : int
        -> y : int
        -> player : int
    ø retour :
        -> bool
    **  Teste si un pion peut se déplacer quelque part 
        selon les règles du jeu
    """
    if test_state(grid, x, y):
        return False

    # Vérification de l'existence d'un pion isolé
    isolated = test_isolated(grid, player)
    # S'il existe au moins un pion isolé :
    if isolated != []:
        # Pour toute la grille :
        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                # On vérifie qu'on puisse faire un déplacement isolé
                # chacunes des cases
                if test_isolated_move(isolated, grid, x, y, col, row):
                    return True
    
    # S'il n'y à pas de pions isolé :
    else:
        # Pour toute la grille :
        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                # On vérifie qu'on puisse faire un déplacement isolé
                # chacunes des cases
                if test_neighbour_move(grid, x, y, col, row):
                    return True
    
    # Si aucun déplacement n'est possible, on renvoi False
    return False
# end def

def can_player_move(grid, player):
    """
    ø parametres :
        -> grid : list
        -> player : int
    ø retour :
        -> bool
    **  Teste si un joueur peut se déplacer quelque part 
        selon les règles du jeu
    """
    # Pour toute la grille :
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            # On vérifie que le joueur puisse jouer un de ses pions
            if grid[row][col] == player and\
                    can_token_move(grid, col, row, player):
                return True

    return False
# end def

def test_victory(victory, current_player, lbl_player, 
            lbl_turn, lbl_message, score_j1, score_j2):
    """
    ø paramètres :
        -> victory : list
        -> current_player : tkinter.IntVar()
        -> lbl_player : tkinter.Label()
        -> score_j1 : int
        -> score_j2 : int
    ø retour :
        -> None
    **  teste si le joueur 1 a le nombre bloqué suffisant pour la 
        victoire, puis de même pour le joueur 2. Déclenche ensuite
        le scénario de victoire adéquat.
    """
    # Si le joueur 1 a 7 pions bloqués :
    if score_j1 == 7:
        # Il respecte la condition de victoire
        victory[0] = True
    # Si le joueur 2 a 7 pions bloqués :
    if score_j2 == 7:
        # Il respecte la condition de victoire
        victory[1] = True
    
    # Si le joueur 1 a gagné et pas le joueur 2 :
    if victory[0] == True and victory[1] == False:
        # On déclenche la victoire du joueur 1
        trigger_victory(1, current_player, lbl_player, lbl_turn, lbl_message,
                grid, grid_canvas)
    # Si le joueur 2 a gagné et pas le joueur 1 :
    elif victory[1] == True and victory[0] == False:
        # On déclenche la victoire du joueur 2
        trigger_victory(2, current_player, lbl_player, lbl_turn, lbl_message,
                grid, grid_canvas)
    else:
        test_draw(victory, current_player, 
            lbl_player, lbl_turn, lbl_message,
            grid, grid_canvas)
# end def

def test_draw(victory, current_player, 
            lbl_player, lbl_turn, lbl_message,
            grid, grid_canvas):
    if victory[0] == True and victory[1] == True:
        # On déclenche l'égalité
        trigger_draw(lbl_player, lbl_turn, lbl_message,
                grid, grid_canvas)
# end def

# ~* Fonctions de gestions de la partie 
#       (joueurs / scores / fin de partie)
def calc_score(grid, score_j1, score_j2):
    """
    ø paramètres :
        -> grid : list
        -> score_j1 : tkinter.IntVar()
        -> score_j1 : tkinter.IntVar()
    ø retour :
        -> None
    **  Calcule le score de chaque joueur en fonction du nombre de ses
        pions bloques
    """
    score_j1.set(0)
    score_j2.set(0)
    # Pour chaque ligne :
    for row in range(NB_ROWS):
        # Pour chaque colonne :
        for col in range(NB_COLS):
            # S'il existe un pion ici et qu'il est bloqué :
            if grid[row][col] != 0 and test_state(grid, col, row) == "blocked":
                # Si le pion appartient au joueur 1 :
                if grid[row][col] == 1:
                    # +1 point pour le joueur 1
                    score_j1.set(score_j1.get() + 1)
                # Si le pion appartient au joueur 2 :
                elif grid[row][col] == 2:
                    # +1 point pour le joueur 2
                    score_j2.set(score_j2.get() + 1)   
# end def

def change_current_player(window, token_prop, grid, grid_canvas, ai,
        menu, btn_start, btn_middle, btn_end,
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        current_player, lbl_player,
        lbl_turn, lbl_message):
    current_player.set(current_player.get() % 2 +1) 

    if not can_player_move(grid, current_player.get()):
        lbl_message.config(text="\nヽ(;´Д｀)ﾉ\n" +
                "Joueur " + str(current_player.get()) + 
                " ne peut pas jouer...")
        
        window.update()
        sleep(1)
        
        skip_turn(window, token_prop, grid, grid_canvas, ai,
            menu, btn_start, btn_middle, btn_end,
            score_j1, score_j2,
            lbl_j1, lbl_j2,
            current_player, lbl_player,
            lbl_turn, lbl_message)

    if current_player.get() == 2 and ai.get() == 1:
        auto_play(window, token_prop, grid, grid_canvas, ai,
                menu, btn_start, btn_middle, btn_end,
                score_j1, score_j2,
                lbl_j1, lbl_j2,
                current_player, lbl_player,
                lbl_turn, lbl_message)
    
    show_menu(menu, btn_start, btn_middle, btn_end, btn_pass, chk_ai,
            lbl_config, lbl_player, lbl_turn, lbl_message,
            current_player)
# end def

def trigger_victory(player, current_player, lbl_player, lbl_turn, lbl_message,
            grid, grid_canvas):
    """
    ø paramètres :
        -> player : int
        -> current_player : tkinter.IntVar()
        -> lbl_player : tkinter.Label()
        -> lbl_turn : tkinter.Label()
        -> lbl_message : tkinter.Label()
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
    ø retour :
        -> None
    **  Déclenche la victoire d'un joueur et affiche a différents
        endroits que la partie est terminée
    """
    current_player.set(player)
    # Affichage de la victoire du joueur
    lbl_player.config(text="Joueur " + str(player) + ": Victoire",
            fg="#FFFF00")
    lbl_turn.config(text="C'est fini !")
    lbl_message.config(text="\n(ﾉ≧∇≦)ﾉ ﾐ┻━┻\n" +
            "Bravo, joueur " + str(player))

    # Mise en évidence des pions bloqués
    show_blocked(player, grid, grid_canvas)
# end def

def trigger_draw(lbl_player, lbl_turn, lbl_message,
            grid, grid_canvas):
    lbl_player.config(text="Égalité",
            fg="#FFFF00")
    lbl_turn.config(text="C'est fini !")
    lbl_message.config(text="\nv(´-ι_-｀)v\n" +
            "Pas de gagnant... ")

    # Mise en évidence des pions bloqués
    show_blocked(1, grid, grid_canvas)
    show_blocked(2, grid, grid_canvas)
# end def

def skip_turn(window, token_prop, grid, grid_canvas, ai,
        menu, btn_start, btn_middle, btn_end,
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        current_player, lbl_player,
        lbl_turn, lbl_message):
    cancel_move(token_prop, grid_canvas, grid)

    # On change le joueur courant et on met à jour l'affichage 
    #       du menu
    change_current_player(window, token_prop, grid, grid_canvas, ai,
            menu, btn_start, btn_middle, btn_end,
            score_j1, score_j2,
            lbl_j1, lbl_j2,
            current_player, lbl_player,
            lbl_turn, lbl_message)
    show_player(lbl_player, current_player.get())
# end def

# ~* Fonctions de déplacements
def cancel_move(token_prop, grid_canvas, grid):
    """
    ø paramètres :
        -> token_prop : list
        -> grid_canvas : tkinter.Canvas()
        -> grid : list
    ø retour :
        -> None
    **  Redéfinie les propriétés du jeton sélectionné à ses valeurs par
        défaut et re-dessine la grille et les pions afin d'annuler
        le mouvement en cours
    """
    # Redéfinitions des propriétés du pion
    token_prop.clear()
    token_prop.extend([False, None, None])

    # On re-dessine la grille et les pions
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
# end def

### Fonction suivante FR, car expressément demandée 😇
def deplacement_isole(token_prop, isolated, grid, grid_canvas, 
            x1, y1, x2, y2, lbl_message):
    """
    ø paramètres :
        -> isolated : list
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> x1 : int
        -> y1 : int
        -> x2 : int
        -> y2 : int
    ø retour :
        -> bool
    **  Tente un déplacement isolé, selon les règles du jeu. Retourne
        True si le déplacement a bien été effectué, False sinon
    """
    # Pour chaque pion isolé allié
    if test_isolated_move(isolated, grid, x1, y1, x2, y2):
        move_token(token_prop, grid, x1, y1, x2, y2)
        return True
        
    # Si la case destination n'est pas à côté d'un pion isolé allié:
    #       Annulation du mouvement, il y a erreur de déplacement
    else:
        cancel_move(token_prop, grid_canvas, grid)
        show_isolated(grid_canvas, isolated)
        
        # Affichage du message d'erreur
        lbl_message.config(text="\no(*≧□≦)o" +
                "\nVous avez des pion isolé !")

        return False
# end def

### Fonction suivante FR, car expressément demandée 😇
def deplacement_voisin(token_prop, grid, grid_canvas, x1, y1, x2, y2,
            lbl_message):
    """
    ø paramètres :
        -> token_prop : list
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> x1 : int
        -> y1 : int
        -> x2 : int
        -> y2 : int
        -> lbl_message : tkinter.Label()
    ø retour :
        -> bool
    **  Tente un déplacement voisin selon les règles du jeu. Retourne
        True si le déplacement a bien été effectué, False sinon
    """
    # S'il n'y à pas de pions sur la case destination:
    if test_neighbour_move(grid, x1, y1, x2, y2):
        move_token(token_prop, grid, x1, y1, x2, y2)
        return True
 
    else:
        # Sinon, on annule le déplacement. Il y a une erreur de déplacement
        cancel_move(token_prop, grid_canvas, grid)
        # Affichage de l'erreur
        lbl_message.config(text="\no(*≧□≦)o" +
                "\nCette case n'est pas valide !") 

        return False
# end def

def move_token(token_prop, grid, x1, y1, x2, y2):
    """
    ø paramètres :
        -> token_prop : list
        -> grid : list
        -> x1 : int
        -> y1 : int
        -> x2 : int
        -> y2 : int
    ø retour :
        -> None
    **  Permet de bouger un pion d'une case à une autre de la grille.
    """
    # Il n'y a plus de pion sélectionné
    token_prop[0] = False

    # On déplace le pion
    grid[y2][x2] = grid[y1][x1]
    grid[y1][x1] = 0
# end def

def select_token(grid, grid_canvas, x, y, player, token_prop):
    """
    ø paramètres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> x : int
        -> y : int
        -> player : int
        -> token_prop : list
    ø retour :
        -> bool
    **  Permet de sélectionner un pion dans la grille, selon s'il y a
        bien un pion qui peut être sélectionné dans la case concernée. 
        Retourne True si la sélection a bien été effectué, False sinon
    """
    # Si la case sélectionné contient bien un pion du joueur courant
    if grid[y][x] == player:
        # Si le pion n'est pas bloqué ou isolé
        if test_state(grid, x, y) == None:
            token_prop[1] = x
            token_prop[2] = y

            # On sélectionne le pion
            token_prop[0] = True

            # On met le pion en évidence en l'entourant d'un rectangle
            grid_canvas.create_rectangle(x*SCALE, y*SCALE,
                    x*SCALE+SCALE, y*SCALE+SCALE, 
                    outline="#7FFF00", width="3")
            
            # Aucune erreur, on l'affiche dans la zone de message a
            #       l'utilisateur
            lbl_message.config(text="\nヾ(^▽^ヾ)")

            return True

        # Si le pion est bloqué ou isolé
        else:
            # Affichage d'une erreur. Ce pion ne peut pas être 
            #       sélectionné
            lbl_message.config(text="\no(*≧□≦)o" +
            "\nCe pion ne peut pas bouger," +
            "\nil est isolé ou bloqué")

            return False

    # Si la case selectioné ne contient pas un pion du joueur courant
    else:
        # Affichage d'une erreur. Il n'y a pas de pion allié ici
        lbl_message.config(text="\no(*≧□≦)o" +
            "\nCe n'est pas un de vos pions")
    
        return False
# end def

# ~* Fonctions de gestion de l'IA
def rand_select_token(grid, player):
    tokens_list = []
    # Pour toute la grille :
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            # Si le jeton appartient aux joueur
            # et qu'il peut être joué :
            if grid[row][col] == player and \
                    can_token_move(grid, col, row, player):
                # On l'ajoute à la liste des pions jouable
                tokens_list.append((row, col))

    # On choisi un pion au hasard et on le retourne
    token = randint(0, len(tokens_list)-1)
    return tokens_list[token]
# end def

def rand_select_move(grid, x, y):
    moves_list = []
    # Vérification de l'existence d'un pion isolé
    isolated = test_isolated(grid, 2)
    # S'il existe au moins un pion isolé :
    if isolated != []:
        # Pour toute la grille :
        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                # On vérifie qu'on puisse faire un déplacement isolé
                # chacunes des cases
                if test_isolated_move(isolated, grid, x, y, col, row):
                    moves_list.append((row, col))
    
    # S'il n'y à pas de pions isolé :
    else:
        # Pour toute la grille :
        for row in range(NB_ROWS):
            for col in range(NB_COLS):
                # On vérifie qu'on puisse faire un déplacement isolé
                # chacunes des cases
                if test_neighbour_move(grid, x, y, col, row):
                    moves_list.append((row, col))
    
    # Si au moins un déplacement est possible :
    if moves_list != []:
        # On choisi une case au hasard, et on la retourne
        cell = randint(0, len(moves_list)-1)
        return moves_list[cell]
    
    # Si aucun déplacement n'est possible, on renvoi une liste vide
    return ()
# end def

def auto_play(window, token_prop, grid, grid_canvas, ai,
        menu, btn_start, btn_middle, btn_end,
        score_j1, score_j2,
        lbl_j1, lbl_j2,
        current_player, lbl_player,
        lbl_turn, lbl_message):
    token = rand_select_token(grid, 2)

    # Attente de 1/2 seconde
    # pour laisser le temps au joueur de voir l'action
    window.update()
    sleep(0.5)

    # On met le pion en évidence en l'entourant d'un rectangle
    grid_canvas.create_rectangle(token[1]*SCALE, token[0]*SCALE,
            token[1]*SCALE+SCALE, token[0]*SCALE+SCALE, 
            outline="#7FFF00", width="3")
    cell = rand_select_move(grid, token[1], token[0])

    # Attente de 1 seconde
    # pour laisser le temps au joueur de voir l'action
    window.update()
    sleep(1)

    move_token(token_prop, grid, token[1], token[0], cell[1], cell[0])
    
    # On calcule le score
    calc_score(grid, score_j1, score_j2)
    show_score(lbl_j1, lbl_j2, score_j1, score_j2)

    # On re-dessine la grille et les pions
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)

    # On vérifie si un joueur a gagné la partie
    test_victory(victory, current_player, lbl_player,
            lbl_turn, lbl_message,
            score_j1.get(), score_j2.get())
    
    # Si personne n'a gagné :
    if not victory[0] and not victory[1]:
        # On change de joueur courant et on met à jour 
        #       le menu
        change_current_player(window, token_prop, grid, grid_canvas, ai,
                menu, btn_start, btn_middle, btn_end,
                score_j1, score_j2,
                lbl_j1, lbl_j2,
                current_player, lbl_player,
                lbl_turn, lbl_message)
        show_menu(menu, btn_start, btn_middle, btn_end, btn_pass, chk_ai,
                lbl_config, lbl_player, lbl_turn, lbl_message,
                current_player)
# end def

#=========================
# ÉVÈNEMENTS

# Ces fonctions sont un peu spéciales. Elles sont déclenchés par 
#       un évènement, par exemple, le clic sur un bouton.

# ~* évènements de changements de config'
def event_change_config_to_begin(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2, lbl_message,
        victory):
    """
    ø parametres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
        -> victory : list
    ø retour :
        -> None
    **  Change la configuration de la grille vers la config
        "debut de partie", et met a jour le score en fonction.
    """
    # Reconfiguration du jeu en mode "début de partie"
    grid.clear()
    grid.extend(init_grid_begin())
    victory.clear()
    victory.extend([False, False])
    current_player.set(1)

    # Actualisation de l'affichage
    show_player(lbl_player, current_player.get())
    calc_score(grid, score_j1, score_j2)
    show_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    lbl_message.config(text="\nヾ(^▽^ヾ)")
    interface.pack()
# end def

def event_change_config_to_end(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2, lbl_message,
        victory):
    """
    ø parametres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
        -> victory : list
    ø retour :
        -> None
    **  Change la configuration de la grille vers la config
        "fin de partie", et met a jour le score en fonction.
    """
    # Reconfiguration du jeu en mode "milieu de partie"
    grid.clear()
    grid.extend(init_grid_end())
    victory.clear()
    victory.extend([False, False])
    current_player.set(1)

    # Actualisation de l'affichage
    show_player(lbl_player, current_player.get())
    calc_score(grid, score_j1, score_j2)
    show_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    lbl_message.config(text="\nヾ(^▽^ヾ)")
    interface.pack()
# end def

def event_change_config_to_middle(grid, grid_canvas, 
        score_j1, score_j2,
        lbl_j1, lbl_j2, lbl_message,
        victory):
    """
    ø parametres :
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
        -> victory : list
    ø retour :
        -> None
    **  Change la configuration de la grille vers la config
        "millieu de partie", et met a jour le score en fonction.
    """
    # Reconfiguration du jeu en mode "fin de partie"
    grid.clear()
    grid.extend(init_grid_middle())
    victory.clear()
    victory.extend([False, False])
    current_player.set(1)

    # Actualisation de l'affichage
    show_player(lbl_player, current_player.get())
    calc_score(grid, score_j1, score_j2)
    show_score(lbl_j1, lbl_j2, score_j1, score_j2)
    draw_grid(grid_canvas, grid)
    draw_tokens(grid_canvas, grid)
    lbl_message.config(text="\nヾ(^▽^ヾ)")
    interface.pack()
# end def

# ~* évènement de déplacement de pion
def event_move_token(window, event, token_prop, ai,
        grid, grid_canvas,
        score_j1, score_j2,
        lbl_j1, lbl_j2, lbl_message,
        victory, lbl_player,
        menu, current_player,
        btn_start, btn_middle, btn_end):
    """
    ø parametres :
        -> window = tkinter.Tk()
        -> event : tkinter.Event()
        -> token_prop : list
        -> ai = tkinter.IntVar()
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> score_j1 : tkinter.IntVar()
        -> score_j2 : tkinter.IntVar()
        -> lbl_j1 : tkinter.Label()
        -> lbl_j2 : tkinter.Label()
        -> lbl_message : tkinter.Label()
        -> victory : list
        -> lbl_player : tkinter.Label()
        -> menu : tkinter.Frame()
        -> current_player : tkinter.IntVar()
        -> btn_start : tkinter.Button()
        -> btn_middle : tkinter.Button()
        -> btn_end : tkinter.Button()
    ø retour :
        -> None
    **  Selon si un pion a déjà été sélectionné ou pas, permet de 
        sélectionner un pion ou d'en déplacer un
    """
    # Coordonnées x et y de la dernière case sélectionné
    x = event.x//SCALE
    y = event.y//SCALE

    # Si pas de cas de victoire :
    if not victory[0] and not victory[1]:

        # Si aucun pion n'a encore été sélectionné :
        if not token_prop[0]:
            # On sélectionne le pion présent sur la case
            select_token(grid, grid_canvas, x, y, 
                    current_player.get(), token_prop)

        # Si la case pointe vers le pion sélectionné :
        elif (token_prop[1], token_prop[2]) == (x, y):
            # On annule le mouvement
            cancel_move(token_prop, grid_canvas, grid)
        # Si un pion à déjà été sélectionné :
        else:
            isolated = []
            isolated = test_isolated(grid, current_player.get())

            # S'il existe des pions isolés pour le joueur courant :
            if len(isolated) > 0:
                # On tente un déplacement isolé
                move = deplacement_isole(token_prop, isolated, 
                        grid, grid_canvas, token_prop[1], token_prop[2],
                        x, y, lbl_message)
            # S'il n'existe pas de pions isolés pour le joueur courant :
            else:
                # On tente un déplacement voisin
                move = deplacement_voisin(token_prop, grid, grid_canvas,
                        token_prop[1], token_prop[2], x, y,
                        lbl_message)
            # Si un mouvement a eu lieu :
            if move:
                # On calcule le score
                calc_score(grid, score_j1, score_j2)
                show_score(lbl_j1, lbl_j2, score_j1, score_j2)

                # On re-dessine la grille et les pions
                draw_grid(grid_canvas, grid)
                draw_tokens(grid_canvas, grid)

                # On vérifie si un joueur a gagné la partie
                test_victory(victory, current_player, lbl_player,
                        lbl_turn, lbl_message,
                        score_j1.get(), score_j2.get())
                
                interface.pack()
                
                # Si personne n'a gagné :
                if not victory[0] and not victory[1]:
                    # On change de joueur courant et on met à jour 
                    #       le menu
                    change_current_player(window, token_prop, grid, grid_canvas, ai,
                            menu, btn_start, btn_middle, btn_end,
                            score_j1, score_j2,
                            lbl_j1, lbl_j2,
                            current_player, lbl_player,
                            lbl_turn, lbl_message)             
# end def

# ~* évènement de passage de tour
def event_pass(window, token_prop, grid, grid_canvas, current_player):
    """
    ø parametres :
        -> window : tkinter.Tk()
        -> token_prop : list
        -> grid : list
        -> grid_canvas : tkinter.Canvas()
        -> current_player : tkinter.IntVar()
    ø retour :
        -> None
    **  Permet de passer le tour du joueur actuel
    """
    # Si pas de cas de victoire
    if not victory[0] and not victory[1]:
        # On annule le mouvement en cours
        skip_turn(window, token_prop, grid, grid_canvas, ai,
                menu, btn_start, btn_middle, btn_end, 
                score_j1, score_j2,         
                lbl_j1, lbl_j2,         
                current_player, lbl_player,         
                lbl_turn, lbl_message)
# end def

#=========================
# MAIN

# Cette ligne sers pour l'utilisation du random dans le reste du code.
seed()

### Cette ligne sers lors de l'import, a ignorer le code principal
### d'entro.py (dans le fichier tests.py par exemple)
if __name__ == '__main__':
    # Initialisation et affichage de la grille
    # et de l'interface.
    grid = init_grid_begin()
    show_game(game, lbl_j2, grid_canvas, lbl_j1, grid)
    show_menu(menu, btn_start, btn_middle, btn_end, btn_pass, chk_ai,
            lbl_config, lbl_player, lbl_turn, lbl_message,
            current_player)

    interface.pack()

    # Ajout des évènements aux boutons.
    # Passage à la configuration début de partie
    btn_start.config(command=lambda : 
            event_change_config_to_begin(grid, grid_canvas, 
            score_j1, score_j2,
            lbl_j1, lbl_j2, lbl_message,
            victory))
    # Passage à la configuration milieu de partie
    btn_middle.config(command=lambda : 
            event_change_config_to_middle(grid, grid_canvas, 
            score_j1, score_j2,
            lbl_j1, lbl_j2, lbl_message,
            victory))
    # Passage à la configuration fin de partie
    btn_end.config(command=lambda : 
            event_change_config_to_end(grid, grid_canvas, 
            score_j1, score_j2,
            lbl_j1, lbl_j2, lbl_message,
            victory))
    # Passer son tour
    btn_pass.config(command=lambda :
            event_pass(window, token_prop, grid, grid_canvas, current_player))

    # Ajout de l'évènement du clic sur la grille pour sélectionner ou
    # déplacer un pion.
    grid_canvas.bind('<1>', lambda e: event_move_token(window, e, token_prop, ai,
            grid, grid_canvas,
            score_j1, score_j2,
            lbl_j1, lbl_j2, lbl_message,
            victory, lbl_player, 
            menu, current_player,
            btn_start, btn_middle, btn_end))

    # Renommage de la fenêtre
    window.title("Entro.py")
    # fix de la taille de la fenêtre
    window.resizable(False, False)
    # Affichage de la fenêtre
    window.mainloop()