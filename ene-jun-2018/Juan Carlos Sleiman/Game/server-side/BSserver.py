from socket import *
from _thread import *
import time
import sys

def ini():
    host = input("Host: ")
    port = int(input("Puerto: "))
    return host, port

def crearSocket():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def ligarSocket(s, host, port):
    while True:
        try:
            s.bind((host, port))
            break

        except error as e:
            print("ERROR:", e)

def conexiones(s):

    conn, addr = s.accept()
    print("\nConexión establecida.\nEl jugador es:", addr[0] + ":" + str(addr[1])+"\n")
    return conn, addr

def enviar(conn):

        msg = input("")
        msg = "Servidor: " + msg
        try:

            conn.send(msg.encode("UTF-8"))

        except:
            print("\nAlgo ocurrió")
            print("Intentandolo 5 seg\n")
            time.sleep(5)

def enviar2(conn):

        msg = input("")
        msg = "Servidor: " + msg
        try:

            conn.send(msg.encode("UTF-8"))

        except:
            print("\nAlgo ocurrió")
            print("Intentandolo en 5 seg\n")
            time.sleep(5)

def recibir(conn):
    while True:
        global bandera
        try:
            reply = conn.recv(2048)
            reply = reply.decode("UTF-8")

            if reply[0] == "1":
                print("Jugador", reply)
                start_new_thread(enviar, (conn,))

            elif reply[0] == "2":
                print("Jugador", reply)
                start_new_thread(enviar2, (conn,))

            else:
                lista_de_jugadores.append(reply[4])
                print("\nEl jugador "+reply[4]+" se ha ido")
                bandera = True
                break



        except:
            print("\nNo recibo respuesta")
            print("Intentandolo en 5 segs\n")
            time.sleep(5)


def enviarEspecial(conn):
    global lista_de_jugadores,player
    player = lista_de_jugadores.pop()
    conn.send(player.encode("UTF-8"))

bandera = False      # Utilizada en la desconexion/conexion de jugadores

lista_de_jugadores = ["2","1"]   # El servidor le asigna un numero a los
                                # jugadores segun esta lista

player = ""     # Numero del playere

def main():

    global bandera
    host,port = ini()
    s = crearSocket()
    ligarSocket(s, host,port)
    s.listen(2)     # Espero 2 jugadores

    print("\nEL SERVIDOR ES UN ESCLAVO "
          "NO ESCRIBAS SI EL SERVIDOR NO TIENE NINGÚN MENSAJE A RESPONDER")
    print("\nEsperando jugadores")

    conn,addr = conexiones(s)
    enviarEspecial(conn)               # Espero conexion del 1 playere
    start_new_thread(recibir,(conn,))

    conn2,addr2 = conexiones(s)
    enviarEspecial(conn2)              # Espero conexion del 2 playere
    start_new_thread(recibir,(conn2,))

    while True: # Necesario para que los hilos no mueran

        if bandera != True:     # En caso de desconectarse un playere,
                                # esperara a que otro vuelve a conectarse
            conn3,addr3 = conexiones(s)
            enviarEspecial(conn3)
            start_new_thread(recibir,(conn3,))
            bandera = False


main()
