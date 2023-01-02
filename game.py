import pygame
pygame.init()

from program_client.entity import *
from program_client.constant_game import *


screen = pygame.display.set_mode((LONGEUR,LARGUEUR))

horloge = pygame.time.Clock()
pygame.display.set_caption('test 2 - network')

Client = client()
Client.init(8080)

player = Player(Client)
enemi = Enemi(Client)
truc_to_draw = pygame.sprite.Group(player, enemi)

run = True
while run:

    # On fait le tour de la liste des évènements
    for evenement in pygame.event.get():
        # Si l'évènement actuel est de type QUIT
        if evenement.type == pygame.QUIT:
            # On sort de la boucle
            run = False
        if evenement.type == pygame.KEYDOWN:
            pass

    
    # On gère les mouvement 
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q]:
        player.move_right()
    elif touches[pygame.K_d]:
        player.move_left()
    if touches[pygame.K_z]:
        player.move_up()
    elif touches[pygame.K_s]:
        player.move_down()
    

    # On gere les update
    truc_to_draw.update()


    # On gere l'afichage 
    screen.fill(back_ground_color)

    truc_to_draw.draw(screen)
    

    pygame.display.update()
    horloge.tick(fps)
