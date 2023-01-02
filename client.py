import socket
from threading import Thread
from constant import *


class client():
    def init(self):
        self.connexion = socket.socket()
        host = 'localhost'
        port = 8080
        try :
            
            self.connexion.connect((host, port))
        except : 
            self.connexion.connect(("138.68.96.66", port))

        self.state = None
        self.msg_envoi = 0

        self.run = True

        self.requete_server = None
        self.ancien_requete_server= None

        self.msg = cripteur_bytes(numbre_playing)
        self.ancien_msg = None

        self.main()

    def Send(self,a):

        if self.msg_envoi == 1:
            self.connexion.send(self.msg)
        self.msg_envoi +=1
        if self.msg_envoi == FRAME_CLEINT:
            self.msg_envoi = 0

        
    def Reception(self,a):

        self.requete_server = self.connexion.recv(1024)
        if len(self.requete_server) == MAX_BYTES_MSG:  # le client est en attente
            self.requete_server = decripteur_bytes(self.requete_server) # on converti
            
            if self.requete_server == numbre_waiting:
                if self.state != 'waiting':
                    self.state = "waiting"
                    self.msg = cripteur_bytes(numbre_playing)
                    print("waiting a player")
                

            elif self.requete_server[0] == 1:
                self.state = 'playing'
                if self.requete_server == numbre_playing: pass
                else: print(self.requete_server)

    def recupe_donné(self,a):
        try:
            msg1= int(input(""))
            msg2 = int(input(""))
            msg3 = int(input(""))
            self.msg = cripteur_bytes([1,msg1,msg2,msg3])
             
        except ValueError: pass
                
       

    def main(self):

        MyThread(self.recupe_donné, serveur=self).start()
        MyThread(self.Send, serveur=self).start()
        MyThread(self.Reception, serveur=self).start()
        
        

client().init()