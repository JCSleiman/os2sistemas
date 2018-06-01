
from socket import *
import time
from _thread import *
from random import randint

def ini():
    host = input("Server Address: ")
    port = int(input("Port: "))
    return host, port

def crearSocket():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def conectarse (host, port, s):
    s.connect((host, port))

def intentoConexion(host, port, s):

        while True:
            print("\nIntentando conectarse a:", host + ":" + str(port))
            try:
                conectarse(host, port, s)
                break
            except:
                print("No hay un servidor en:", host + ":" + str(port))
                print("Intentando en 5 segs\n")
                time.sleep(5)

def enviar(s):

    while True:

        global exit

        try:
            msg = input("")
            msg = jugador +": " + msg
            if msg == jugador+": salir":
                exit = True
                msg = "El "+jugador+" Jugador se ha ido"
                s.send(msg.encode("UTF-8"))
                s.close
                break
            else:
                s.send(msg.encode("UTF-8"))
                start_new_thread(recibir,(s,))


        except:
            print("Algo ocurrió\n")
            print("Reintentando en 5 segs")
            time.sleep(5)

def recibir(s):
    while True:

        try:
          reply = s.recv(2048)
          print(reply.decode("UTF-8"))
          break


        except:
            print("No se puede recibir respuesta\n")
            print("Reintentando en 5 segs")
            time.sleep(5)

def recibirEspecial(s):
    global jugador
    jugador = s.recv(2048).decode("UTF-8")

exit=False      # Si el jugador envia salir, exit se pone en true y el
                # el programa termina
jugador = ""

def main():


    host, port = ini()
    s = crearSocket()
    intentoConexion(host,port,s)
    recibirEspecial(s)
    print("\nConexión al servidor establecida!\nEl servidor es:", host+":"+str(port)+"\n")
    #############CODIGO DEL JUEGO###################
    n = 5
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
    #############CODIGO DEL JUEGO###################
    print("Escribe tus mensajes\n")
    start_new_thread(enviar,(s,))

    while exit!=True:   # Necesarios para que los hilos no mueran
        pass

    print("\nLo sentimos, algo salió mal! Has perdido la conexión al servidor.:(")
    print("Cerrando las ventanas en 5 seg")
    time.sleep(10)

main()
