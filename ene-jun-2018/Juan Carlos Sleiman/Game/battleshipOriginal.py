"""
La idea de este juego es el de crear una base de '0's mediante un arreglo de listas
La generación del barco a buscar completamente aleatoria
Objetivo:
Gana el primero que descubra dónde se encuentra el barco
Puede ser por turnos y simplemente tener un contador para saber cuánto tiempo se
tardaron los jugadores en encontrar el barco
Al ganador se le muestra un mensaje de WIN
"""
from random import randint

n = 8
board = []

for x in range(n):
    board.append(["O"] * n)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Let's play Battleship!")
print(str(n)+"x"+str(n))
print("Begins with 0,0 to "+str(n-1)+","+str(n-1))
print("""
row -> -
col -> |
""")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(9):
    print ("Turn", turn)
    guess_row = int(input("Guess Row:"))
    guess_col = int(
        input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Felicidades! Hundiste mi barco que estaba en " +str(ship_row)+","+str(ship_col)+"!")
        break
    else:
        if (guess_row < 0 or guess_row > n-1) or (guess_col < 0 or guess_col > n-1):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("Game Over")
    turn =+ 1
    print_board(board)
