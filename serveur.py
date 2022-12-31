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

        self.all_conexion = {}
        self.all_conexion_wait = []

        self.connexion = socket.socket()
        self.connexion.bind((self.host, self.port))
        print('server launch...')
        
        self.connexion.listen()

        self.main()

    def protocole_client_wating_serveur(self):

        while True:
            for client in self.all_conexion_wait:
                try:
                    client.send(cripteur_bytes(numbre_waiting))
                except ConnectionError: 
                    print("client deconecter")
                    self.all_conexion_wait.remove(client)

    def send_to_client(self, client, data = list):
        data = cripteur_bytes(data)
        client.send(data)

    def accepting_clients_thread(self):
        
        while True:

            # on accepte les joueur
            Client, adresse =  self.connexion.accept()

            #on l'ajoute a la liste
            self.all_conexion_wait.append(Client)

            if len(self.all_conexion_wait) % 2 == 0:
                taille = len(self.all_conexion)
                self.all_conexion[str(taille + 1)] = self.all_conexion_wait
                self.all_conexion_wait = []

            print ("New client : " + str(adresse[0]))
            print("there is now : " + str(len(self.all_conexion_wait) + get_nombre_client(self.all_conexion)) + " clien")


    def game(self):
        while True:

            for client in verifi_client_partenaire(self.all_conexion):   # on verifi si chaque client a son partenaire 
                self.all_conexion_wait.append(client)
            
            
    


    def main(self):
        
        CreeThread(self.accepting_clients_thread)
        CreeThread(self.protocole_client_wating_serveur)
        CreeThread(self.game)

        


NetWwork().init(8080)

            