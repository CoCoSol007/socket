import threading

numbre_waiting = [0,0,0,0] # requet protocole waiting
numbre_playing = [1,0,0,0] # requet protocole waiting
MAX_BYTES_MSG = 19

FRAME_CLEINT = 10000

def cripteur_bytes(data= list):
    new_data = []
    for element in data:
        new_data.append(int(element).to_bytes(4,'big'))
    new_data = b','.join(new_data)

    return new_data



def decripteur_bytes(data= list):
    new_data= []
    data = data.split(b",")
    for nbr in data:
        new_data.append(int.from_bytes(nbr,'big'))



    return new_data



def get_nombre_client(data):

        n = 0
        for ellement in data:
            for client in ellement:
                n+=1

        return n



class MyThread(threading.Thread):
    def __init__(self,  fonction, arg = None, boucle = None, Name = None, serveur = False):

        threading.Thread.__init__(self)
        self.fonction = fonction
        self.arg = arg
        self.boucle = boucle
        self.name = Name
        self.serveur = serveur
    def run(self):
            
        if self.boucle == False:
            
            self.fonction(self.arg) 
            
        else:
            while True:
                if self.serveur.run == True:
                    self.fonction(self.arg) 
                else: break

        print("thread close")




def find_player_in_data(data,player):
    game = None
    place = None
    for i in range(0,len(data)):
        for o in range(0,len(data[i])):
            if data[i][o] == player:
                game = i
                place = o

    return game, place


def remove_player_partenair(data, player, data_wait= list):

    # trouver la place du joueur partenair
    key, place = find_player_in_data(data, player)
    if place == 1 : place = 0
    else : place = 1
    joueur_partenair = data[key][place]

    data_wait.append(joueur_partenair)







def recupe_players(data, position ):
    a = []
    for elemment in data.values():
        a.append(elemment)
    return a[position]


def recupe_game_non_thread(data, thread):
    result = []

        
    for i in range(0,len(thread)):
        if not thread[i]:
            result.append(data[i])
            thread[i] = True

    return result   # returne des clef 


print(decripteur_bytes (cripteur_bytes([1,32,32,32])))


