import socket
from threading import Thread
from constant import *


def CreeThread(foction):
    thread = Thread(target=foction)
    thread.start()


class NetWwork:
    def init(self, port):
        self.host = ''
        self.port = port

        self.all_conexion = []
        self.all_conexion_wait = []

        self.connexion = socket.socket()
        self.connexion.bind((self.host, self.port))
        print('server launch...')
        
        self.connexion.listen()

        self.main()


    def protocole_client_serveur(self):
        while True:
            if len(self.all_conexion) > 0:
                for client in self.all_conexion:
                    try:
                        client.send(int(numbre_playing).to_bytes(4,'big'))
                    except ConnectionError: 
                        print("client deconecter")

                        position_client = self.all_conexion.index(client) # on cherche pour remletre son partenaire client en atente
                        if position_client % 2 == 0:
                            position_client += 1
                        else: position_client -= 1

                        self.all_conexion_wait.append(self.all_conexion[position_client])
                        del self.all_conexion[position_client]
                        self.all_conexion.remove(client)


    def protocole_client_wating_serveur(self):

        while True:
            for client in self.all_conexion_wait:
                try:
                    client.sendall(int(numbre_waiting).to_bytes(4,'big') )
                except ConnectionError: 
                    print("client deconecter")
                    self.all_conexion_wait.remove(client)

                
            
    
    def occupé_client_thread(self):
        
        while True:

            # on accepte les joueur
            Client, adresse =  self.connexion.accept()

            #on l'ajoute a la liste
            self.all_conexion_wait.append(Client)
            
            print ("New client : " + str(adresse[0]))
            print("there is now : " + str(len(self.all_conexion_wait) + len(self.all_conexion)) + " clien")

    
    def transfere_donné(self):
        while True:
            if len(self.all_    conexion) > 1: 
                for i in range(1, len(self.all_conexion), 2):
                    
                    Thread(target=self.transfer, args=[self.all_conexion[i-1], self.all_conexion[i]] ).start()
                    Thread(target=self.transfer, args=[self.all_conexion[i], self.all_conexion[i-1]] ).start()
            

    def transfer(self , client1, client2):
        try:
            client2.send(client1.recv(128))
        except: pass
    def main(self):



        

        CreeThread(self.occupé_client_thread)
        CreeThread(self.protocole_client_serveur)
        CreeThread(self.protocole_client_wating_serveur)
        CreeThread(self.transfere_donné)

        while True:
            
            if len(self.all_conexion_wait) % 2 == 0:
                for conexion in self.all_conexion_wait:
                    self.all_conexion.append(conexion)
                self.all_conexion_wait = []


            



snetWwork = NetWwork().init(8080)


