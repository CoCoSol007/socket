LONGEUR = 1200
LARGUEUR = 600

fps = 120

vitesse = 10

back_ground_color = (150,200,255)


def flip(positionX):
    if positionX == LONGEUR/2:
        new_x = LONGEUR/2

    elif positionX > LONGEUR/2:
        new_x = LONGEUR - positionX
    
    elif positionX < LONGEUR/2:
        new_x = LONGEUR - positionX

    return new_x

