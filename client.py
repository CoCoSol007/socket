import socket
from threading import Thread



class client():
    def init(self):

        self.connexion = socket.socket()
        host = '192.168.1.40'
        port = 8080
        self.connexion.connect((host, port))

        self.a = True
        self.b = True

        self.main()
    def Send(self):
        while True:
            msg = input("")
            msg = msg.encode('utf-8')
            self.connexion.send(msg)
    def Reception(self):
        while True:
            requete_server = self.connexion.recv(1024).decode("utf-8")
            if requete_server == "requet_playing" :
                if self.b:
                    print("player find")
                    self.b = False
                    self.a = True
            elif requete_server == "requet_waitng":
                if self.a:
                    print("wating a player")
                    self.a = False
                    self.b = True
            else : print(requete_server)

    def main(self):

        envoi = Thread(target=self.Send)
        recep = Thread(target=self.Reception)

        envoi.start()
        recep.start()

client().init()