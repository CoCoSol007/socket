import pygame
import random

screen = pygame.display.set_mode((1200,900))

direction = "droit"

fps = 60
horloge = pygame.time.Clock()
bite_ = pygame.transform.scale (pygame.image.load("personage.png"), (270,270))
_bite = pygame.transform.flip(bite_, True, False)
x, y = 1200/ 2 - 270/2,  900/ 2 - 270/2



run = True
while run == True:
    for evenement in pygame.event.get():
        # Si l'évènement actuel est de type QUIT
        if evenement.type == pygame.QUIT:
            # On sort de la boucle
            run = False

    touches = pygame.key.get_pressed()
    if touches[pygame.K_q]:
        x=x-10
        direction = "gauche"
    elif touches[pygame.K_d]:
        x=x +10
        direction = "droit"
    if touches[pygame.K_z]:
        y=y-10
    elif touches[pygame.K_s]:
        y=y+10
    

    screen.fill((51, 254, 217))

    if direction == "droit" :screen.blit(bite_,(x,y))
    if direction == "gauche" :screen.blit(_bite,(x,y))
    pygame.display.update()
    horloge.tick(fps)