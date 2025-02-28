import pandas as pd
import numpy as np
import random as rand

# Archivage des scores
results = [[]]
results[0] = ['Occur','turn_nb','max_score','moves_history']

# récupérer une paire de coordonnées aléatoire
def randcoord() :
    return (rand.randint(0,3),rand.randint(0,3))

def monkey_move(n) :
    if n == 0 :
        auto_mouv = 'UP'
    elif n == 1 : 
        auto_mouv = 'DOWN'
    elif n == 2 : 
        auto_mouv = 'LEFT'
    elif n == 3 : 
        auto_mouv = 'RIGHT'
    return auto_mouv


# -- check fin partie & lancement d'un nouveau tour : 
# on part sur 
#   Searching_in_table = False
# sonde la totalité des cases, puis :
# si on trouve 2048, on arrête la recherhe la partie s'arrête
# si on trouve au moins un 0, searching devient True et la partie peut continuer
# si on trouve ni 0 ni 2048, searching reste faux et la partie est finie
#     

def check_end_and_new_turn() :
    searching_in_table = False
    game_on = False
    for i in range(4) :
        for j in range(4) :
            if game_table[i,j] == 2048 :
                break
            elif game_table[i,j] == 0 :
                game_on = True
                searching_in_table = True
                break
    while searching_in_table :
        coordinates = randcoord()
        if game_table[coordinates] == 0 :
            game_table[coordinates] = rand.randint(1,2) * 2
            searching_in_table = False
    return game_on
            
# -- mouvements :
# Un mouvement est découpé en 3 temps : 
# 1 - on tasse dans la direction
# 2 - on double les valeurs quand il faut 
#    (et on met 0 à la place de celle qu'on a prise pour sommer)
# 3 - on retasse dans la meme direction

def move_up() :
    for j in range(0,4) :
        # clean des 0, on tasse vers le haut
        for i in [0,1,2,0,1,0] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i+1,j]
                game_table[i+1,j] = 0
        # si la valeur est identique à celle d'en dessous, on double
        # et la valeur devient 0
        for i in range(0,3) : 
            if game_table[i,j] == game_table[i+1,j] :
                game_table[i,j] *= 2
                game_table[i+1,j] = 0
        # nouveau clean des 0, on tasse vers le haut
        for i in [0,1,2] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i+1,j]
                game_table[i+1,j] = 0
    return game_table

def move_down() :
    for j in range(0,4) :
        for i in [3,2,1,3,2,3] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i-1,j]
                game_table[i-1,j] = 0
        for i in [3,2,1] : 
            if game_table[i,j] == game_table[i-1,j] :
                game_table[i,j] *= 2
                game_table[i-1,j] = 0
        for i in [3,2,1] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i-1,j]
                game_table[i-1,j] = 0
    return game_table

def move_left() :
    for i in range(0,4) :
        for j in [0,1,2,0,1,0] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i,j+1]
                game_table[i,j+1] = 0
        for j in range(0,3) : 
            if game_table[i,j] == game_table[i,j+1] :
                game_table[i,j] *= 2
                game_table[i,j+1] = 0
        for j in [0,1,2] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i,j+1]
                game_table[i,j+1] = 0
    return game_table

def move_right() :
    for i in range(0,4) :
        for j in [3,2,1,3,2,3] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i,j-1]
                game_table[i,j-1] = 0
        for j in [3,2,1] : 
            if game_table[i,j] == game_table[i,j-1] :
                game_table[i,j] *= 2
                game_table[i,j-1] = 0
        for j in [3,2,1] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i,j-1]
                game_table[i,j-1] = 0
    return game_table

#test modif
#mouvement request
def ask_move() :
    invalid = True
    game_on = True
    while invalid :
        # print('What shall we do ?')
        # je bloque sur up pour pouvoir coder tranquile
        #function_move = input().upper()
        #function_move = 'UP'
        function_move = monkey_move(rand.randint(0,3))

        if function_move == 'UP' :
            move_up()
            invalid = False
        elif function_move == 'DOWN' :
            move_down()
            invalid = False
        elif function_move == 'LEFT' :
            move_left()
            invalid = False
        elif function_move == 'RIGHT' :
            move_right()
            invalid = False
        elif function_move == '?' :
            print('Available Moves : \n - UP \n - DOWN \n - LEFT \n - RIGHT')
        elif function_move == 'EXIT' :
            invalid = False
            game_on = False
        else :
            print('réponse non valide, recommencer')
            print('Taper "?" pour aide')
            print('Taper "Exit" pour quitter\n')
    move_history.append(function_move)
    return game_on

# Check de fin pour afficher le score max et le nombre de tours
def end_procedure() :
    score = 0
    for i in range(4) :
        for j in range(4) :
            if int(game_table[i,j]) > score :
                score = int(game_table[i,j])
    if score == 2048 :
        print('------- VICTORY ! -------')
    else :
        print('\n------ GAME OVER.. ------')
    print('Turn n°' + str(turn))
    print('Max Score : '+str(score))
    return score

# fin de partie >>  enregistrement des scores 
def saving_score(turn,score,move_history) :
    in_game_result.append(1)
    in_game_result.append(turn)
    in_game_result.append(score)
    in_game_result.append(move_history)
    results.append(in_game_result)
    
        
# -- initialisation :
# Game_on en status de jeu : True quand ca fonctionne, False quand on perd.
# On crée la table de 0 et on y met 1 valeur de départ    
for i in range (10) :
    game_on = True
    in_game_result = []
    move_history = []
    game_table = np.zeros((4,4))
    
    turn = 0
    print ("------------------------\n------ Game Start ------\n------------------------")
    print('')
    
    # -- Jeu :
    # Boucle TANT QUE GAME ON EST TRUE :
    # 1 - On affiche le tour
    # 2 - On affiche la table telle qu'elle est
    # 4 - On Check si la partie tourne encore
    # 3 - On demande de choisir le mouvement 
    # 5 - On lance la procédure de NewTurn qui met 2 ou 4 dans un endroit random
    while game_on :
        turn += 1
        # print('\nTurn : '+str(turn)+'\n')
        game_on = check_end_and_new_turn()
        # print(game_table)
        # print('')
        if game_on == False :
            break
        game_on = ask_move()
    
    score = end_procedure()
    saving_score(turn,score,move_history)

export = np.array(results)
print(pd.DataFrame(export).head())
pd.DataFrame(export).to_csv('monkey2048V2.csv')
