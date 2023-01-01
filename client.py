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

        self.requete_server = None
        self.ancien_requete_server= None

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

        self.requete_server = self.connexion.recv(1024)
        if len(self.requete_server) == 19:  # le client est en attente
            self.requete_server = decripteur_bytes(self.requete_server) # on converti
            
            if self.requete_server == numbre_waiting:
                if self.a:
                    self.a = False
                    print("waiting a player")
                
            elif self.requete_server == numbre_playing: pass

            elif self.requete_server[0] == 1:
                self.a = True
                print(self.requete_server)

    def main(self):

        MyThread(self.Send).start()
        MyThread(self.Reception).start()
        
        

client().init()