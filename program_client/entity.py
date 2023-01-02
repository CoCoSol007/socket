import pygame
from program_client.client import client
from program_client.constant_game import *
from constant_network import MyThread

class Player(pygame.sprite.Sprite):
    def __init__(self,client):
        super().__init__()
        self.client = client
        self.image = pygame.transform.scale(pygame.image.load("program_client\player.png"), (32,32))

        self.rect = self.image.get_rect()

        self.rect.center = (100,LARGUEUR/2)

    def move_right(self):
        self.rect.centerx -= vitesse

    def move_left(self):
        self.rect.centerx += vitesse

    def move_up(self):
        self.rect.centery -= vitesse

    def move_down(self):
        self.rect.centery += vitesse

    def evoi_coo(self):
        self.client.new_donné(self.rect.centerx, self.rect.centery)
         
    def update(self):
        
        self.evoi_coo()
        

class Enemi(pygame.sprite.Sprite):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.image = pygame.transform.scale(pygame.image.load("program_client\player enemi.png"), (32,32))

        self.rect = self.image.get_rect()

        self.rect.center = (1100,LARGUEUR/2)

    def update(self):
        self.recoi_co()

    def recoi_co(self):
        data = self.client.get_data()
        self.rect.centerx = flip(data[1])
        self.rect.centery = data[2]



