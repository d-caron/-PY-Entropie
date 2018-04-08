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
# /!\ Certaines fonctions ne seront pas testées ici. Je détaillerais
# pourquoi dans un bloc de commentaire dédié a ces fonctions dans
# chaque catégorie.
# ----------------------------------------------------------------------
# 
# © copyright : Ce code est certainement soumis à des trucs beaucoup
# trop obscurs et chiants pour que vous puissiez l'utiliser sans que 
# l'auteur ait le courage de vous en tenir rigueur.
# ======================================================================
import entro as e
from tkinter import IntVar

#=========================
# FONCTION PRINCIPALE

def run_tests():
    # ~* Fonctions de tests
    print("\nPHASE 1 : Fonctions de tests")
    __TEST__est_dans_grille()
    __TEST__test_state()
    __TEST__test_isolated()
    __TEST__test_direction()
    __TEST__test_between()
    __TEST__test_neighbour_move()
    __TEST__test_isolated_move()
    __TEST__can_token_move()
    __TEST__can_player_move()
    print("\nPHASE 1 : VALIDÉE")
    print("\n--------------------------")

    # ~* Fonction de déplacement
    print("PHASE 2 : Fonction de déplacement")
    __TEST__move_token()
    print("\nPHASE 2 : VALIDÉE")
    print("\n--------------------------")
    # ~* Fonctions de gestion de l'IA
    print("PHASE 3 : Fonctions de gestion de l'IA")
    __TEST__rand_select_token()
    __TEST__rand_select_move()
    print("\nPHASE 3 : VALIDÉE")
    print("\n--------------------------")

    print("...")
    print("Tous les tests sont OK")
# end def

#=========================
# FONCTION DE TESTS

# ~* Fonctions d'initialisation des grilles

# Ces fonctions ne font que retourner une configuration de grille
# Si aucun calcul n'est fait, il est donc inutile de les tester.
# ======================================================================

# ~* Fonctions de dessin

# Ces fonctions sont purement graphique. 
# Il est donc impossible de les tester.
# ======================================================================

# ~* Fonctions d'affichage

# Ces fonctions sont purement graphique. 
# Il est don cimpossible de les tester.
# ======================================================================

# ~* Fonctions de tests
def __TEST__est_dans_grille():
    # Tests pour des cas valides
    assert e.est_dans_grille("(1, 3)"),\
            "La case (1, 3) devrait etre dans la grille"
    assert e.est_dans_grille("(4, 4)"),\
            "La case (1, 3) devrait etre dans la grille"
    assert e.est_dans_grille("(0, 0)"),\
            "La case (1, 3) devrait etre dans la grille"

    # Tests pour des cas non valides
    assert not e.est_dans_grille("(-1, 1)"),\
            "La case (-1, 1) ne devrait pas etre dans la grille"
    assert not e.est_dans_grille("(4, 6)"),\
            "La case (4, 6) ne devrait pas etre dans la grille"
    assert not e.est_dans_grille(str((e.NB_COLS, e.NB_ROWS))),\
            "La case (" + str(e.NB_COLS) + ", " + str(e.NB_ROWS) + ") " +\
            "ne devrait pas etre dans la grille"

    print("__TEST__est_dans_grille() : OK")
# end def

def __TEST__test_state():
    grid_1 = [[2, 2, 2, 2, 2],
              [2, 0, 0, 0, 2],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]
    # Test pour tout les pions de la grille en configuration initiale
    for row in range(e.NB_ROWS):
        for col in range(e.NB_COLS):
            if grid_1[row][col] != 0:
                test_state = e.test_state(grid_1, col, row)
                assert not test_state, "__TEST__test_state() : " +\
                        "Tout les pions de la grille 1 ne devraient être " +\
                        "ni isolés, ni bloqués"

    grid_2 = [[1, 2, 1, 2, 1],
              [2, 0, 0, 1, 0],
              [2, 1, 0, 2, 1],
              [0, 0, 0, 0, 0],
              [2, 0, 2, 0, 1]]
    # Tests pour des pions bloqués
    test_state = e.test_state(grid_2, 1, 2)
    assert test_state == "blocked", "__TEST__test_state() : " +\
            "(1, 2) devrait être bloqué"
    test_state = e.test_state(grid_2, 3, 2)
    assert test_state == "blocked", "__TEST__test_state() : " +\
            "(3, 2) devrait être bloqué"

    # Tests pour des pions isolés
    test_state = e.test_state(grid_2, 0, 4)
    assert test_state == "isolated", "__TEST__test_state() : " +\
            "(0, 4) devrait être isolé"
    test_state = e.test_state(grid_2, 4, 4)
    assert test_state == "isolated", "__TEST__test_state() : " +\
            "(4, 4) devrait être isolé"
    
    print("__TEST__test_state() : OK")
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

    print("__TEST__test_isolated() : OK")
# end def

def __TEST__test_direction():
    # Tests de directions valides
    test_dir = e.test_direction(2, 2, 4, 4)
    assert test_dir, "la direction (2, 2) vers (4, 4) devrait être valide"
    test_dir = e.test_direction(2, 2, 2, 4)
    assert test_dir, "la direction (2, 2) vers (2, 4) devrait être valide"
    test_dir = e.test_direction(2, 2, 0, 4)
    assert test_dir, "la direction (2, 2) vers (0, 4) devrait être valide"
    test_dir = e.test_direction(2, 2, 0, 2)
    assert test_dir, "la direction (2, 2) vers (0, 2) devrait être valide"
    test_dir = e.test_direction(2, 2, 1, 1)
    assert test_dir, "la direction (2, 2) vers (1, 1) devrait être valide"
    test_dir = e.test_direction(2, 2, 2, 1)
    assert test_dir, "la direction (2, 2) vers (2, 1) devrait être valide"
    test_dir = e.test_direction(2, 2, 3, 1)
    assert test_dir, "la direction (2, 2) vers (3, 1) devrait être valide"
    test_dir = e.test_direction(0, 2, 0, 4)
    assert test_dir, "la direction (0, 2) vers (0, 4) devrait être valide"

    # Tests de directions non valides
    test_dir = e.test_direction(0, 0, 1, 4)
    assert not test_dir, "la direction (0, 0) vers (1, 4) ne devrait pas " +\
            "être valide"
    test_dir = e.test_direction(2, 2, 4, 3)
    assert not test_dir, "la direction (2, 2) vers (4, 3) ne devrait pas " +\
            "être valide"

    print("__TEST__test_direction() : OK")
# end def

def __TEST__test_between():
    grid_1 = [[1, 2, 1, 2, 1],
              [2, 0, 0, 1, 0],
              [2, 1, 0, 2, 1],
              [0, 0, 0, 0, 0],
              [2, 0, 2, 0, 1]]
    # tests de cas valides
    test_between = e.test_between(grid_1, 1, 2, 3, 4)
    assert test_between, "le mouvement (1, 2) vers (3, 4) devrait être valide"
    test_between = e.test_between(grid_1, 3, 2, 3, 4)
    assert test_between, "le mouvement (3, 2) vers (3, 4) devrait être valide"

    # tests de cas non valides
    test_between = e.test_between(grid_1, 1, 0, 1, 4)
    assert not test_between, "le mouvement (1, 0) vers (1, 4) ne devrait " +\
            "pas être valide"
    test_between = e.test_between(grid_1, 0, 2, 2, 2)
    assert not test_between, "le mouvement (0, 2) vers (2, 2) ne devrait " +\
            "pas être valide"
    
    print("__TEST__test_between() : OK")
# end def

def __TEST__test_neighbour_move():
    grid_1 = [[1, 2, 1, 2, 1],
              [0, 0, 1, 0, 0],
              [1, 0, 0, 0, 2],
              [0, 2, 2, 0, 1],
              [2, 1, 0, 0, 2]]
    # Tests de déplacements valides
    test_move = e.test_neighbour_move(grid_1, 2, 3, 4, 1)
    assert test_move, "le mouvement (2, 3) vers (4, 1) devrait être possible"
    test_move = e.test_neighbour_move(grid_1, 2, 1, 2, 2)
    assert test_move, "le mouvement (2, 1) vers (2, 2) devrait être possible"

    # Tests de déplacements non valides
    test_move = e.test_neighbour_move(grid_1, 2, 3, 3, 1)
    assert not test_move, "le mouvement (2, 3) vers (3, 1) ne devrait pas " +\
            "être possible"
    test_move = e.test_neighbour_move(grid_1, 0, 4, 2, 2)
    assert not test_move, "le mouvement (0, 4) vers (2, 2) ne devrait pas " +\
            "être possible"

    print("__TEST__test_neighbour_move() : OK")
# end def

def __TEST__test_isolated_move():
    grid_1 = [[1, 2, 1, 2, 1],
              [2, 0, 0, 1, 0],
              [2, 1, 0, 2, 1],
              [0, 0, 0, 0, 0],
              [2, 0, 2, 0, 1]]
    isolated_1 = e.test_isolated(grid_1, 1)
    isolated_2 = e.test_isolated(grid_1, 2)
    # Tests de déplacements valides
    test_move = e.test_isolated_move(isolated_1, grid_1, 4, 2, 4, 3)
    assert test_move, "le mouvement (4, 2) vers (4, 3) devrait être possible"
    test_move = e.test_isolated_move(isolated_2, grid_1, 0, 2, 1, 3)
    assert test_move, "le mouvement (0, 2) vers (1, 3) devrait être possible"

    # Tests de déplacements non valides
    test_move = e.test_isolated_move(isolated_1, grid_1, 3, 1, 3, 3)
    assert not test_move, "le mouvement (3, 1) vers (3, 3) ne devrait pas " +\
            "être possible"
    test_move = e.test_isolated_move(isolated_1, grid_1, 4, 2, 3, 4)
    assert not test_move, "le mouvement (4, 2) vers (3, 4) ne devrait pas " +\
            "être possible"
    test_move = e.test_isolated_move(isolated_1, grid_1, 4, 2, 4, 1)
    assert not test_move, "le mouvement (4, 2) vers (4, 1) ne devrait pas " +\
            "être possible"

    print("__TEST__test_isolated_move() : OK")
# end def

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

# Les fonctions test_victory et test_draw du fichier entro.py
# n'ont pas de retours ce qui les rends impossible a tester.
# ======================================================================

# ~* Fonction de gestion de partie

# Les fonctions de cette catégorie utilisent des fonctions graphiques 
# ou n'ont pas de retour, ce qui les rends impossible a tester.
# ======================================================================

# ~* Fonction de déplacement
def __TEST__move_token():
    default_token_prop = [True, 0, 0]

    grid_1 = [[2, 2, 2, 2, 2],
              [2, 0, 0, 0, 2],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]
    # Test de mouvements dans la grille initiale
    assert grid_1[0][0] == 2, "La case (0, 0) devrait être prise par le " +\
            "joueur 2 avant le déplacement"
    assert grid_1[2][2] == 0, "La case (2, 2) devrait être vide avant le " +\
            "déplacement"

    e.move_token(default_token_prop, grid_1, 0, 0, 2, 2)
    assert grid_1[0][0] == 0, "La case (0, 0) devrait être vide après le " +\
            "déplacement"
    assert grid_1[2][2] == 2, "La case (2, 2) devrait être prise par le " +\
            "joueur 2 après le déplacement"

    e.move_token(default_token_prop, grid_1, 2, 2, 3, 2)
    assert grid_1[2][2] == 0, "La case (2, 2) devrait être vide après le " +\
            "déplacement"
    assert grid_1[2][3] == 2, "La case (3, 2) devrait être prise par le " +\
            "joueur 2 après le déplacement"

    print("__TEST__move_token() : OK")
# end def

# Les autres fonctions de cette catégorie utilisent des fonctions
# graphiques ce qui les rends impossible a tester.
# ======================================================================

# ~* Fonctions de gestion de l'IA
def __TEST__rand_select_token():
    grid_1 = [[2, 2, 2, 2, 2],
              [2, 0, 0, 0, 2],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1]]
    token_list = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), 
            (1, 0), (1, 4)]
    # Test de génération multiple d'un pion aléatoire
    for i in range(10):
        assert token_list.count(e.rand_select_token(grid_1)) == 1,\
                "Le pions sélectioné devrait être l'un de ceux présent " +\
                "dans token_list"

    print("__TEST__rand_select_token() : OK")
# end def

def __TEST__rand_select_move():
    grid_1 = [[0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1],
              [2, 0, 0, 0, 2],
              [2, 2, 2, 2, 2]]
    move_list = [(3, 1), (3, 2)]
    # Test de génération multiple d'un mouvement aléatoire
    for i in range(5):
        assert move_list.count(e.rand_select_move((grid_1), 1, 4)) == 1,\
                "Le pions (1, 4) devrait pouvoir se déplacer que " +\
                "dans une des case de move_list"

    move_list = [(3, 2), (3, 3)]
    for i in range(5):
        assert move_list.count(e.rand_select_move((grid_1), 3, 4)) == 1,\
                "Le pions (3, 4) devrait pouvoir se déplacer que " +\
                "dans une des case de move_list"

    print("__TEST__rand select_move() : OK")
# end def

# La fonction auto_play d'entro.py modifie l'interface graphique ce 
# qui la rend impossible a tester.
# ======================================================================

# ~* Lancement des tests
if __name__ == '__main__':
    run_tests()

    input("\npressez [ENTRÉE] pour terminer")