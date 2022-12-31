import socket
from threading import Thread
from constant import *


class client():
    def init(self):

        self.connexion = socket.socket()
        host = 'localhost'
        port = 8080
        self.connexion.connect((host, port))

        self.a = True
        self.b = True

        self.main()
    def Send(self):
        while True:
            msg = int(input(""))
            msg = msg.to_bytes(4, 'big')
            self.connexion.send(msg)
    def Reception(self):
        while True:
            requete_server = self.connexion.recv(1024)
            if len(requete_server) == 19:  # le client est en attente
                requete_server = decripteur_bytes(requete_server) # on converti
                if requete_server == numbre_waiting:
                    if self.a:
                        print("waiting a player")
                        self.a = False
                        self.b = True
                elif requete_server[0] == 1:
                    if self.b:
                        print("waiting a player")
                        self.a = True
                        self.b = False
                else : print(requete_server)

    def main(self):

        envoi = Thread(target=self.Send)
        recep = Thread(target=self.Reception)

        envoi.start()
        recep.start()

client().init()