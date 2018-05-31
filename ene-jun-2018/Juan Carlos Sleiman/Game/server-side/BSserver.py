#!/usr/bin/env python

#importamos el modulo socket
import socket
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

print("ESTE ES EL SERVIDOR DE SHIPSEEK!")

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

#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 8102))

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
    jugador1 =sc.recv(jugador)
    jugador2 = sc.recv(jugador)

    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":
        break

    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print (str(addr) + " dice: ", recibido)

    #Devolvemos el mensaje al cliente
    sc.send(recibido)
print ("Adios.")

#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()
