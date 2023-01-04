import os


LONGEUR = 1200
LARGUEUR = 600

fps = 500

vitesse = 5

back_ground_color = (150,200,255)


def flip(positionX):
    if positionX == LONGEUR/2:
        new_x = LONGEUR/2

    elif positionX > LONGEUR/2:
        new_x = LONGEUR - positionX
    
    elif positionX < LONGEUR/2:
        new_x = LONGEUR - positionX

    return new_x

def Average(lst):
    return sum(lst) / len(lst)

PATH = os.path.dirname(__file__) 