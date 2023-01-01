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
    def Send(self,a):
        try :
            msg1= int(input(""))
            msg2 = int(input(""))
            msg3 = int(input(""))
            msg = [1,msg1,msg2,msg3]
            msg = cripteur_bytes(msg)
            self.connexion.send(msg)
        except :
            pass
        
    def Reception(self,a):

        requete_server = self.connexion.recv(1024)
        if len(requete_server) == 19:  # le client est en attente
            requete_server = decripteur_bytes(requete_server) # on converti
            if requete_server == numbre_waiting:
                if self.a:
                    self.a = False
                    print("waiting a player")

            elif requete_server[0] == 1:
                self.a = True
                print(requete_server)

    def main(self):

        MyThread(self.Send).start()
        MyThread(self.Reception).start()
        
        

client().init()