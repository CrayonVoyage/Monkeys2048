import pandas as pd
import numpy as np
import random as rand

# récupérer une paire de coordonnées random
def randcoord() :
    return (rand.randint(0,3),rand.randint(0,3))

# rafraichir la table
def refresh() :
    print(game_table)
    print()

# check fin partie
def check_end() :
    end_game = True
    for i in range(4) :
        for j in range(4) :
            if game_table[i,j] == 0 :
                end_game = False
                break
            elif game_table[i,j] == 2048 :
                end_game = False
                break
    return end_game

#nouveau tour
def new_turn() :
    check = True
    while check :
        coordinates = randcoord()
        if game_table[coordinates] == 0 :
            game_table[coordinates] = rand.randint(1,2) * 2
            check = False
    return(game_table)
            
# movements :     
def move_up() :
    for j in range(0,4) :
        #clean des 0, on tasse vers le haut
        for i in [0,1,2,0,1,0] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i+1,j]
                game_table[i+1,j] = 0
        for i in range(0,3) : 
            if game_table[i,j] == game_table[i+1,j] :
                game_table[i,j] *= 2
                game_table[i+1,j] = 0
        for i in [0,1,2] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i+1,j]
                game_table[i+1,j] = 0
    return game_table

def move_down() :
    for j in range(0,4) :
        #clean des 0, on tasse vers le haut
        for i in [3,2,1,3,2,3] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i-1,j]
                game_table[i-1,j] = 0
        #double la valeur si 
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
        #clean des 0, on tasse vers le haut
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
        #clean des 0, on tasse vers le haut
        for j in [3,2,1,3,2,3] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i,j-1]
                game_table[i,j-1] = 0
        #double la valeur si 
        for j in [3,2,1] : 
            if game_table[i,j] == game_table[i,j-1] :
                game_table[i,j] *= 2
                game_table[i,j-1] = 0
        for j in [3,2,1] :
            if game_table[i,j] == 0 :
                game_table[i,j] = game_table[i,j-1]
                game_table[i,j-1] = 0
    return game_table

#demander le move à faire
def ask_move() :
    invalid = True
    while invalid :
        move = rand.randint(0,3)

        if move == 0 :
            move_up()
            invalid = False
        elif move == 1 :
            move_down()
            invalid = False
        elif move == 2 :
            move_left()
            invalid = False
        elif move == 3 :
            move_right()
            invalid = False
        elif move == '?' :
            print('Available Moves : \n- UP \n- DOWN \n- LEFT \n- RIGHT')
        else :
            print('réponse non valide, recommencer')
            print('Taper "?" pour aide\n')
    return(move)
        
#fin de partie >> affichage du score et tout et tout
def end_procedure() :
    score = 0
    for i in range(4) :
        for j in range(4) :
            if int(game_table[i,j]) > score :
                score = int(game_table[i,j])
    print('Turn n°' + str(turn))
    print('Max Score : '+str(score))
    result.append(score)

        
#initialisation 
results = [['#','turns','up','down','left','right','score']]
for i in range (1000) :
    print ("game "+str(i))
    score_up = 0
    score_down = 0
    score_left = 0
    score_right = 0
    result = []
    game_on = True
    turn = 1
    victory_status = False
    game_table = np.zeros((4,4))
    game_table[randcoord()] = 1

    while game_on :
        #print('\nTurn : '+str(turn))
        #refresh()
        move = ask_move()
        if move == 0 :
            score_up += 1
        elif move == 1 :
            score_down += 1
        elif move == 2 :
            score_left += 1
        elif move == 3 :
            score_right += 1
        if check_end() :
            break
        new_turn()
        turn += 1

    #refresh()
    result.append(i)
    result.append(turn)
    result.append(score_up)
    result.append(score_down)
    result.append(score_left)
    result.append(score_right)
    end_procedure()
    results.append(result)

export = np.array(results)
print(pd.DataFrame(export).head())
pd.DataFrame(export).to_csv('monkey2048.csv')
