import threading

numbre_waiting = [0,0,0,0] # requet protocole waiting

def cripteur_bytes(data= list):
    new_data = []
    for element in data:
        new_data.append(int(element).to_bytes(4,'big'))
    new_data = b' '.join(new_data)

    return new_data

def decripteur_bytes(data= list):
    new_data= []
    data = data.split(b" ")
    for nbr in data:
        new_data.append(int.from_bytes(nbr,'big'))



    return new_data


def get_nombre_client(data):

        n = 0
        for ellement in data.items():
            n+=len(ellement)

        return n

def verifi_client_partenaire(data, liste, thread_list =list):
    client = []
    client_a_sup = [] 
    for game in data.items():
        if len(game[1]) == 1:
            client.append(game[1][0])
            client_a_sup.append(game[0])

    for c in client_a_sup:   # on suprime les
        del data[c]

    for c in client:
        liste.append(c)

    return client

class MyThread(threading.Thread):
   def __init__(self,  fonction, arg = None, boucle = None):
      threading.Thread.__init__(self)
      self.fonction = fonction
      self.arg = arg
      self.boucle = boucle
   def run(self):
    if self.boucle == False:
        self.fonction(self.arg) 
    else:
        while True:
            self.fonction(self.arg) 
               



def recupe_players(data, position ):
    a = []
    for elemment in data.values():
        a.append(elemment)
    return a[position]


def recupe_game_non_thread(data, thread):

    Games = []

    result = []

    for game in data.keys():
        Games.append(game)
        
    for i in range(0,len(thread)):
        if not thread[i]:
            result.append(Games[i])
            thread[i] = True

    return result   # returne des clef 
