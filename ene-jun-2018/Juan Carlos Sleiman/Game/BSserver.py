"""
La idea de este juego es el de crear una base de '0's mediante un arreglo de listas
La generación del barco a buscar completamente aleatoria
Objetivo:
Gana el primero que descubra dónde se encuentra el barco
Puede ser por turnos y simplemente tener un contador para saber cuánto tiempo se
tardaron los jugadores en encontrar el barco
Al ganador se le muestra un mensaje de WIN
"""
 #importamos el modulo socket
import socket
from random import randint

class Battleship():

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    def tablero():

        n = 2
        board = []

        for x in range(n):
            board.append(["O"] * n)

        def print_board(board):
            for row in board:
                print((" ").join(row))

        print("Juguemos Battleship!")
        print(str(n)+"x"+str(n))
        print("Empieza con 0,0 hasta "+str(n-1)+","+str(n-1))
        print("""
        fila -> -
        columna -> |
        """)
        print_board(board)

        ship_row = random_row(board)
        ship_col = random_col(board)

    def turnos(addr):

        for turn in range(100):

            winner1 = False
            winner2 = False
            if turn % 2 == 0:
                print ("\nTurno", turn)
                print("Turno del J1" )
                guess_row = int(input("Adivina la FILA:"))
                guess_col = int(
                    input("Adivina la COLUMNA:"))
                winner1 = True

            else:
                print ("\nTurno", turn)
                print("Turno del J2" )
                guess_row = int(input("Adivina la FILA:"))
                guess_col = int(input("Adivina la COLUMNA:"))
                winner2 = True

            if guess_row == ship_row and guess_col == ship_col:
                print("¡FELICIDADES! Hundiste mi barco que estaba en " +str(ship_row)+","+str(ship_col)+"!")
                if winner1:
                    puntaje1 += 1
                elif winner2:
                    puntaje2 += 1
                break
            else:
                if (guess_row < 0 or guess_row > n-1) or (guess_col < 0 or guess_col > n-1):
                    print("Oops, no estuviste ni cerca compi.")
                elif(board[guess_row][guess_col] == "X"):
                    print("Ya habías dicho esa coordenada perrin.")
                else:
                    print("Fallaste mi barco chato!")
                    board[guess_row][guess_col] = "X"
            print("Game Over")
            print("P1 puntos: ", puntaje1)
                print("P2 puntos: ", puntaje2)
            # implementear la espera en el servidor cuando uno de los jugadores ya haya escogido coordenadas

            turn =+ 1
            print_board(board)


#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 8081))

#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
s.listen(2)

#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
sc, addr = s.accept()

while True:

    #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro
    #la cantidad de bytes para recibir
    recibido = sc.recv(1024)

    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":
        break

    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print str(addr[0]) + " dice: ", recibido

    #Devolvemos el mensaje al cliente
    sc.send(recibido)
print ("Adios.")

#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()
