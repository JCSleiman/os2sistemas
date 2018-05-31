from random import randint

def tablero():
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
