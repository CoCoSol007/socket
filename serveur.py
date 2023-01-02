import socket
from threading import Thread
from constant import *


class NetWwork:
	def init(self, port):
		self.host = ''
		self.port = port

		self.all_conexion = []
		self.all_conexion_wait = []
		self.all_thread_client = []
		self.data = []

		self.connexion = socket.socket()
		self.connexion.bind((self.host, self.port))
		print('server launch...')
		
		self.connexion.listen()

		self.client_juste_kick = None

		self.run = True

		self.main()

	def protocole_client_wating_serveur(self,a):
		for client in self.all_conexion_wait:
			try:
				client.send(cripteur_bytes(numbre_waiting))
			except ConnectionError: 
				print("client deconecter")
				self.all_conexion_wait.remove(client)



	def accepting_clients_thread(self,a):

		# on accepte les joueur
		Client, adresse =  self.connexion.accept()

		#on l'ajoute a la liste
		self.all_conexion_wait.append(Client)


		print ("New client : " + str(adresse[0]))
		print("there is now : " + str(len(self.all_conexion_wait) + get_nombre_client(self.all_conexion)) + " client")


	def game(self,a):

		if len(self.all_conexion_wait) % 2 == 0 and len(self.all_conexion_wait) > 0 :
			print("new game")
			
			self.all_conexion.append(self.all_conexion_wait)
			self.data.append([cripteur_bytes(numbre_playing),cripteur_bytes(numbre_playing)])
			self.all_thread_client.append(False)
			self.all_conexion_wait = []
			
		self.socuper_donné_thread()

	def socuper_donné_thread(self):

		try : 
			for game in recupe_game_non_thread(self.all_conexion, self.all_thread_client):
				MyThread(self.transfere_donné, arg = [game[0],game[1]], boucle= False, Name="1", serveur = self).start()
				MyThread(self.transfere_donné, arg = [game[1],game[0]], boucle= False, Name="2", serveur = self).start()
		except : pass
	

	def transfere_donné(self, clients):

		client_prinsipal = clients[0]
		client_secondaire = clients[1]

		key, place = find_player_in_data(self.all_conexion, client_prinsipal)

		run = True
		while run:
			if self.run == True:

				try:
					msg = client_prinsipal.recv(1024)  
					if len(msg) == MAX_BYTES_MSG:
						self.data[key][place] = msg
					else: 
						decripteur_bytes(msg)
					
				except :
					try:
						self.remove_game(client_prinsipal, key)
					except: pass
					run = False
					break

				try :
					client_secondaire.send(self.data[key][place])
				except : run = False

			else: break
			



	def remove_game(self, client,key):

		remove_player_partenair(self.all_conexion, client, self.all_conexion_wait)
		del self.all_conexion[key]
		del self.all_thread_client[key]
		del self.data[key]

		print("client deconecter") 

	def consol(self,a): 
		comande = input("")
		if comande == 'close':
			self.run = False
			connexion = socket.socket()
			host = 'localhost'
			port = 8080
			connexion.connect((host, port))
			


	def main(self):
		
		MyThread(self.protocole_client_wating_serveur, serveur = self).start()
		MyThread(self.game, serveur = self).start()
		MyThread(self.accepting_clients_thread, serveur = self).start()
		MyThread(self.consol, serveur = self).start()

serveur = NetWwork().init(8080)


