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

"""

INSERTAR AQUÍ EL CÓDIGO DE BATTLESHIP.PY

"""


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
