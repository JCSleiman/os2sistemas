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

jugador1=0
jugador2=0
n = 2
board = []

for x in range(n):
    board.append(["O"] * n)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("JUGUEMOS A 'ENCUENTRA MI BARCO'!")
jugador1=input('Nombre del jugador 1... ')
jugador2=input('Nombre del jugador 2... ')

print(str(n)+"x"+str(n))
print("El tablero empieza con 0,0 hasta "+str(n-1)+","+str(n-1))
print("""
fila -> -
columna -> |
""")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(1,1000):

    if turn % 2 != 0:
        print ("\nTurno", turn)
        print("Turno de", jugador1 )
        guess_row = int(input("\nAdivina la fila:"))
        guess_col = int(input("Adivina la columna:"))
        winner1 = True
        winner2 = False

    else:
        print ("\nTurno", turn)
        print("Turno de", jugador2 )
        guess_row = int(input("\nAdivina la fila:"))
        guess_col = int(input("Adivina la columna:"))
        winner1 = False
        winner2 = True

    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "+"

        if winner1:
            print("\nFELICIDADES "+jugador1+" HUNDISTE MI BARCO QUE ESTABA EN " +str(ship_row)+","+str(ship_col)+"!")
            print(jugador1+", ¡HAS GANADO EL JUEGO!")
            print_board(board)
            break
        elif winner2:
            print("\nFELICIDADES "+jugador2+" HUNDISTE MI BARCO QUE ESTABA EN " +str(ship_row)+","+str(ship_col)+"!")
            print(jugador2+", ¡HAS GANADO EL JUEGO!")
            break
            print_board(board)

    else:
        if (guess_row < 0 or guess_row > n-1) or (guess_col < 0 or guess_col > n-1):
            print("\nLo siento, eso ni estuvo en el oceano.")
        elif(board[guess_row][guess_col] == "X"):
            print("\nYa habías dicho ese.")
        else:
            print("\nFallaste mi barco!\n")
            board[guess_row][guess_col] = "X"
    turn =+ 1
    print_board(board)
