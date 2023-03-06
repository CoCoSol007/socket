import time
import pygame
from constant_network import *
from program_client.client import client
from program_client.constant_game import *


class Player(pygame.sprite.Sprite):
    def __init__(self, conexion ):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(PATH + "\player.png"), (32,32))

        self.rect = self.image.get_rect()
        self.msg = cripteur_bytes(numbre_playing)

        self.rect.center = (100,LARGUEUR/2)

        self.conexion = conexion

    def move_right(self):
        self.rect.centerx = min(self.rect.centerx + vitesse, LONGEUR)
        self.evoi_coo()

    def move_left(self):
        self.rect.centerx = max(self.rect.centerx - vitesse, 0)
        self.evoi_coo()

    def move_up(self):
        self.rect.centery = max(self.rect.centery - vitesse, 0)
        self.evoi_coo()

    def move_down(self):
        self.rect.centery = min(self.rect.centery + vitesse, LARGUEUR)
        self.evoi_coo()

    def evoi_coo(self):
        msg = [1,self.rect.centerx,self.rect.centery,0]
        msg = cripteur_bytes(msg)
        self.conexion.send(msg)
         
    def update(self):
        pass
        
        

class Enemi(pygame.sprite.Sprite):
    def __init__(self, conexion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(PATH + "\player enemi.png"), (32,32))

        self.rect = self.image.get_rect()

        self.rect.center = (LONGEUR- 100,LARGUEUR/2)

        self.conexion = conexion
        self.data = [1,100, LARGUEUR/2,0]

        self.run = True
        self.ping = 0
        self.all_ping = []

        MyThread(self.Reception, serveur=self).start()
        MyThread(self.timer, serveur=self).start()

    def update(self):
        self.rect.centerx = self.data[1]
        self.rect.centery = self.data[2]


    def Reception(self,a):
        requet = self.conexion.recv(1024)

        requet = decripteur_bytes(requet)
        if requet == numbre_waiting: pass
        elif requet == numbre_playing : pass
        else: 
                self.data = requet
                self.ping += 1

    def timer(self,a):
        self.ping = 0
        time.sleep(1)
        self.all_ping.append(self.ping)
        print (Average(self.all_ping))
        print("____________________")


