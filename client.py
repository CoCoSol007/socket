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
        self.msg_envoi = True

        self.run = True


        self.msg = cripteur_bytes(numbre_playing)

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
            else: 
                msg = decripteur_bytes(requet)
                print(msg)


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