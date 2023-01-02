import socket
from threading import Thread
from constant_network import *


class client():
    def init(self,port):
        self.connexion = socket.socket()
        host = 'localhost'
        try :
            self.connexion.connect((host, port))
        except : 
            self.connexion.connect(("138.68.96.66", port))

        self.state = None
        self.msg_envoi = True

        self.run = True


        self.msg = cripteur_bytes(numbre_playing)
        self.data = [1,100, 400,0]

        self.main()

    def Send(self,a):
        if self.msg_envoi == True:
            self.connexion.send(self.msg)
            self.msg_envoi = False

        
    def Reception(self,a):
        requet = self.connexion.recv(1024)
        self.msg_envoi = True

        if len(requet) == MAX_BYTES_MSG:
            if requet == cripteur_bytes(numbre_waiting): pass
            elif requet == cripteur_bytes(numbre_playing) : pass
            else: 
                msg = decripteur_bytes(requet)
                self.data = msg


    def new_donné(self,x,y):

        msg = [1,x,y,0]
        self.msg = cripteur_bytes(msg)

    def get_data(self):

        return self.data
       

    def main(self):


        MyThread(self.Send, serveur=self).start()
        MyThread(self.Reception, serveur=self).start()
        
        


