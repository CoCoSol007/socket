import socket
from threading import Thread

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
        for client in self.all_conexion:
            try:
                client.send("requet_playing".encode("utf-8"))
            except: 
                print("client deconecter")

                position_client = self.all_conexion.index(client) # on cherche pour remletre son partenaire client en atente
                self.all_conexion.remove(client)
                if position_client % 2 == 0:
                    position_client += 1
                else: position_client -= 1

                self.all_conexion_wait.append(self.all_conexion[position_client])
                del self.all_conexion[position_client]


    def protocole_client_wating_serveur(self):
        for client in self.all_conexion_wait:
            try:
                client.send("requet_waitng".encode("utf-8"))
            except: 
                print("client deconecter")
                self.all_conexion_wait.remove(client)
                
            
    
    def occupé_client_thread(self):
        # on accepte les joueur
        Client, adresse =  self.connexion.accept()



        #on l'ajoute a la liste
        self.all_conexion_wait.append(Client)

        if len(self.all_conexion_wait) % 2 == 0:
            for conexion in self.all_conexion_wait:
                self.all_conexion.append(conexion)
            self.all_conexion_wait = []
        
        print ("New client : " + str(adresse[0]))
        print("there is now : " + str(len(self.all_conexion_wait) + len(self.all_conexion)) + " clien")

    
    def transfere_donné(self):
        for i in range(1,len(self.all_conexion)+1,2):
            client_1 = self.all_conexion [i-1]
            client_2 = self.all_conexion[i]
            
            Thread(target=self.transfer, args=[client_1, client_2] ).start()
            Thread(target=self.transfer, args=[client_2, client_1] ).start()


    def transfer(self , client1, client2):
        try : 
            msg = client1.recv(128).decode('utf-8')
            client2.send(msg.encode('utf-8'))
        except : pass
    def main(self):

        while True:

            CreeThread(self.occupé_client_thread)
            CreeThread(self.protocole_client_serveur)
            CreeThread(self.protocole_client_wating_serveur)
            if len(self.all_conexion) != 0: CreeThread(self.transfere_donné)

            



netWwork = NetWwork().init(8080)