print("Please input value in Row|Column value sepearted by space")
print("\t\tGame Board")

#creating game board
game_board = [[0,0,0], 
              [0,0,0],
              [0,0,0],]
k = 0
print("   0  1  2")
for i in game_board:
    print(k,i)
    k+=1
print("\n\n")
player1 = []
player2 = []

def verticalWin():  #to define vertical win condition
    x = 0
    k = 0
    while x < 3:
        counter1 = 0
        counter2 = 0
        for i in game_board:
            if i[k] == 1:
                counter1 += 1
            elif i[k] == 2:
                counter2 += 1
        if counter1 == 3:
            return 1
        elif counter2 == 3:
            return 2
        x += 1
        k += 1

def horizontalWin(): #to define horzontal win condition
    for i in game_board:
        counter1 = 0
        counter2 = 0
        for k in i:
            if k == 1:
                counter1 += 1
            if k == 2:
                counter2 += 1
        if counter1 == 3:
            return 1
        elif counter2 == 3:
            return 2
        else:
            counter1 == 0
            counter2 == 0

def diagonalWin(): #to define diagonal win condition
    k = 0
    counter1 = 0
    counter2 = 0
    for i in game_board:
        if i[k] == 1:
            counter1 += 1
            k += 1
        elif i[k] == 2:
            counter2 += 1
            k += 1

    if counter1 == 3:
        return 1
    elif counter2 == 3:
        return 2
        
    k = 2
    counter1 = 0
    counter2 = 0
    for i in game_board:
        if i[k] == 1:
            counter1 += 1
            k -= 1
        elif i[k] == 2:
            counter2 += 1
            k -= 1
    if counter1 == 3:
        return 1
    if counter2 == 3:
        return 2
    
breaker = False

def gameBoard(x,y,player): #main major function 
    k = 0
    game_board[x][y] = player
    print("   0  1  2")
    for i in game_board:
        print(k,i)
        k+=1
    horizontalWin() #win check
    diagonalWin()   #win check
    verticalWin()   #win check
    if horizontalWin() == 1 or diagonalWin() == 1 or verticalWin() == 1:
        print("Player 1 wins")
        return False
    
    elif horizontalWin() == 1 or diagonalWin() == 2 or verticalWin() == 2:
        print("Player 2 wins")
        return False

        
def insertingValuesPlayer1():
    player1 = input("Player 1: ").split(" ") #inserting
    x = player1[0]  #rows
    y = player1[1] #columns
    return gameBoard(int(x),int(y),1)
    player1 = [] #clearing values


def insertingValuesPlayer2():
    player2 = input("Player 2: ").split(" ") #inserting
    x = player2[0]  #rows
    y = player2[1]  #columns
    return gameBoard(int(x),int(y),2)
    player2 = []    #clearing values

while True:
    if insertingValuesPlayer1() == False or insertingValuesPlayer2() == False:
        break
    else:
        insertingValuesPlayer1() #asking for values
        insertingValuesPlayer2() #asking for values
