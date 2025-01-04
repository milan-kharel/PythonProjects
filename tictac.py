import random

board = ["-"] * 9
CurrentPlayer = "X"
winner = None
GameRunning = True

#printing the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#take the input from the player
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter the position from 1-9: "))
            if 1<=inp<=9 and board[inp-1] == "-":
                board[inp-1] = CurrentPlayer
                break
            else:
                print("You can't go there. Try again")
        except ValueError:
            print("Invalid input. Try again")

#check for win or tie

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkRow (board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    global GameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        GameRunning = False

def checkWin(board):
    global GameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        print(winner + " won!")
        GameRunning = False
        
        

#switch the player

def switchPlayer():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer = "X"

#computer to play O 
def computerPlay(board):
    while CurrentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

    
#main game loop
while GameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    if GameRunning:
        switchPlayer()
        computerPlay(board)
        checkWin(board)
        checkTie(board)

