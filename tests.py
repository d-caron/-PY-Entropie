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
# fichier : tests.py
# Auteur : 😎 On a dit ANONYME !
# MAJ : 07/04/18
# ----------------------------------------------------------------------
#
# Remarques : 
# Lancer ce fichier lancera d'abbord simplement le jeu. Pour que les 
# tests s'exécutent, il faudra fermer le jeu. Certains résultats seront 
# affichés dans le terminal.
#
# Ce fichier sera sera organisée en "fonctions de tests"
# Chaque fonction __TEST__ testera une fonction dans le fichier 
# principal : entro.py
#
# /!\ Les fonctions purement graphiques ne pourront être testés
# (puisqu'elles ne font qu'afficher des choses a l'écran) Merci de 
# prendre ceci en considération.
# ----------------------------------------------------------------------
# 
# © copyright : Ce code est certainement soumis à des trucs beaucoup
# trop obscurs et chiants pour que vous puissiez l'utiliser sans que 
# l'auteur ait le courage de vous en tenir rigueur.
# ======================================================================
import entro as e

#=========================
# FONCTION PRINCIPALE

def run_tests():
    # test_deplacement_isole()
    # test_deplacement_voisin()
    # test_victoire()

    __TEST__can_token_move()
    __TEST__can_player_move()
    __TEST__test_isolated()

    print("\n...")
    print("Tous les tests sont OK")
# end def

#=========================
# FONCTION DE TESTS

def __TEST__can_token_move():
    grid_1 = [[2, 2, 2, 2, 2],
              [2, 0, 0, 0, 2],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]
    # Test pour tout les pions de la grille en configuration initiale
    for row in range(e.NB_ROWS):
        for col in range(e.NB_COLS):
            if grid_1[row][col] != 0:
                test_move = e.can_token_move(grid_1, col, row, 
                        grid_1[row][col])
                assert test_move, "__TEST__can_token_move() : " +\
                        "Tout les pions de la grille 1 devraient pouvoir " +\
                        "bouger"

    grid_2 = [[1, 2, 1, 2, 1],
              [0, 0, 1, 0, 0],
              [1, 0, 0, 0, 2],
              [0, 2, 2, 0, 1],
              [2, 1, 0, 0, 2]] 
    # Quelques tests sur des pions qui ne peuvent pas bouger
    assert not e.can_token_move(grid_2, 1, 4, 1),\
            "__TEST__can_token_move() : " +\
            "Le pion [1,4] de la grille 2 ne devrait pas pouvoir bouger"
    assert not e.can_token_move(grid_2, 4, 0, 1),\
            "__TEST__can_token_move() : " +\
            "Le pion [4,0] de la grille 2 ne devrait pas pouvoir bouger"
    assert not e.can_token_move(grid_2, 3, 0, 2),\
            "__TEST__can_token_move() : " +\
            "Le pion [3,0] de la grille 2 ne devrait pas pouvoir bouger"

    # Print en cas de réussite des tests
    print("__TEST__can_token_move() : OK")
# end def

def __TEST__can_player_move():
    grid_1 = [[2, 2, 2, 2, 2],
              [2, 0, 0, 0, 2],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]
    # Test pour les 2 joueurs en configuration initiale
    test_move = e.can_player_move(grid_1, 1)
    assert test_move, "__TEST__can_player_move() : " *\
            "Le joueur 1 devrait pouvoir jouer dans la grille 1"
    test_move = e.can_player_move(grid_1, 2)
    assert test_move, "__TEST__can_player_move() : " *\
            "Le joueur 2 devrait pouvoir jouer dans la grille 1"

    grid_2 = [[1, 2, 1, 2, 1],
              [0, 0, 1, 0, 0],
              [1, 0, 0, 0, 2],
              [0, 2, 2, 0, 1],
              [2, 1, 0, 0, 2]]
    # Tests dans un autre cas valide
    test_move = e.can_player_move(grid_2, 1)
    assert test_move, "__TEST__can_player_move() : " *\
            "Le joueur 1 devrait pouvoir jouer dans la grille 2"
    test_move = e.can_player_move(grid_2, 2)
    assert test_move, "__TEST__can_player_move() : " *\
            "Le joueur 2 devrait pouvoir jouer dans la grille 2"

    # Tests dans un cas non-valide
    grid_3 = [[1, 2, 1, 2, 1],
              [0, 0, 0, 0, 0],
              [2, 1, 0, 2, 1],
              [0, 0, 0, 0, 0],
              [2, 1, 2, 1, 2]]
    test_move = e.can_player_move(grid_3, 1)
    assert not test_move, "__TEST__can_player_move() : " *\
            "Le joueur 1 ne devrait pas pouvoir jouer dans la grille 3"
    test_move = e.can_player_move(grid_3, 2)
    assert not test_move, "__TEST__can_player_move() : " *\
            "Le joueur 2 ne devrait pas pouvoir jouer dans la grille 3"
    
    print("__TEST__can_player_move() : OK")
# end def

def __TEST__test_isolated():
    grid_1 = [[2, 2, 2, 2, 2],
              [2, 0, 0, 0, 2],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]
    # test pour une grille sans pions isolé
    test_isolated = e.test_isolated(grid_1, 1)
    assert test_isolated == [], "__TEST__test_isolated() : " +\
            "Le joueur 1 ne devrait pas avoir de pions isolés " +\
            "dans la grille 1"
    test_isolated = e.test_isolated(grid_1, 2)
    assert test_isolated == [], "__TEST__test_isolated() : " +\
            "Le joueur 2 ne devrait pas avoir de pions isolés " +\
            "dans la grille 1"
    
    print("__TEST__test_isolated() : OK")

    grid_2 = [[1, 2, 1, 2, 1],
              [2, 0, 0, 1, 0],
              [2, 1, 0, 2, 1],
              [0, 0, 0, 0, 0],
              [2, 0, 2, 0, 1]]
    # test pour une grille sans pions isolé
    test_isolated = e.test_isolated(grid_2, 1)
    assert test_isolated == [[4, 4]], "__TEST__test_isolated() : " +\
            "Le joueur 1 ne devrait pas avoir de pions isolés " +\
            "dans la grille 2"
    test_isolated = e.test_isolated(grid_2, 2)
    assert test_isolated == [[4, 0], [4, 2]], "__TEST__test_isolated() : " +\
            "Le joueur 2 ne devrait pas avoir de pions isolés " +\
            "dans la grille 2"
# end def

def __TEST__test_isolated_move():
    pass
# end def

'''
def test_deplacement_isole():
    # Création des variables nécessaire aux fonctions
    window = Tk()
    grid = [[2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0],
            [0, 0, 1, 0, 2],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0]]
    grid_canvas = Canvas(window)
    lbl_message = Label(window)
    
    # Test de la fonction test_isolated()
    isolated = []
    isolated = test_isolated(grid,1)
    assert isolated == [[2, 2]], "isolated devrait valoir [[2, 2]], il vaut :"\
            + str(isolated)

    # Test de la fonction deplacement_isole()
    move = deplacement_isole([True, 3, 4], isolated, grid, grid_canvas, 
            3, 4, 4, 4, lbl_message)

    assert move == False, "Ce mouvement ne devrait pas etre possible "\
            + "car il y a un pion isole"
    
    move = deplacement_isole([True, 3, 4], isolated, grid, grid_canvas, 
            3, 4, 3, 3, lbl_message)

    assert move == True, "Ce mouvement devrait etre possible car a proximite "\
            + "d'un pion isole"

    move = deplacement_isole([True, 3, 0], isolated, grid, grid_canvas, 
            3, 0, 3, 1, lbl_message)

    assert move == True, "Ce mouvement devrait etre possible car a proximite "\
            + "d'un pion isole"

    print("deplacement isolé OK")
# end def

def test_deplacement_voisin():
    # Création des variables nécessaire aux fonctions
    window = Tk()
    grid = [[2, 2, 2, 2, 2],
            [2, 0, 0, 0, 2],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    grid_canvas = Canvas(window)
    lbl_message = Label(window)

    # test de la fonction deplacement_voisin()
    move = deplacement_voisin([True, 3, 0], grid, grid_canvas, 3, 0, 3, 3, 
            lbl_message)
    
    assert move == True, "Ce mouvement devrait etre possible"

    move = deplacement_voisin([True, 4, 0], grid, grid_canvas, 4, 0, 3, 3, 
            lbl_message)
    
    assert move == False, "Ce mouvement devrait etre impossible"

    move = deplacement_voisin([True, 4, 1], grid, grid_canvas, 4, 0, 2, 0,
            lbl_message)
    
    assert move == False, "Ce mouvement devrait etre impossible"

    print("deplacement voisin OK")
# end def

def test_victoire():
    # Création des variables nécessaire aux fonctions
    window = Tk()
    grid = [[2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0],
            [0, 0, 1, 0, 2],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 0]]
    current_player = IntVar(window, value=1)
    score_j1 = IntVar(window, value=0)
    score_j2 = IntVar(window, value=0)
    lbl_player = Label(window)
    lbl_turn = Label(window)
    lbl_message = Label(window)
    victory = [False, False]

    # Test de calc_score() et test_victory() [1]
    calc_score(grid, score_j1, score_j2)

    assert score_j1.get() == 1 and score_j2 .get() == 1, ""\
            + "le score devrait etre 1 - 1"

    test_victory(victory, current_player, lbl_player, lbl_turn, 
            lbl_message, score_j1.get(), score_j2.get())

    assert victory[0] == False and victory[1] == False, ""\
            + "Aucun des deux joueurs n'a gagne"

    # Re-création des variables nécessaire aux fonctions
    grid = [[1, 2, 0, 1, 2],
            [2, 0, 0, 2, 0],
            [1, 0, 0, 1, 2],
            [0, 2, 0, 0, 0],
            [1, 0, 1, 2, 1]]

    # Test de calc_score() et test_victory() [2]
    calc_score(grid, score_j1, score_j2)

    assert score_j1.get() == 7 and score_j2 .get() == 2, ""\
            + "le score devrait etre 7 - 2"

    test_victory(victory, current_player, lbl_player, lbl_turn, 
            lbl_message, score_j1.get(), score_j2.get())
            
    assert victory[0] == True and victory[1] == False, ""\
            + "le joueur 1 devrait avoir gagne"

    print("victoire OK")
# end def
'''
run_tests()
