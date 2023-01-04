import math
import socket
from constant_network import *
import time
from program_client.constant_game import *


class client():
    def init(self,port):
        self.connexion = socket.socket()
        host = 'localhost'
        try :
            self.connexion.connect((host, port))
        except : 
            self.connexion.connect(("138.68.96.66", port))




