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

		self.client_juste_kick_1 = None
		self.client_juste_kick_2 = None

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

		
		for game in recupe_game_non_thread(self.all_conexion, self.all_thread_client):
			MyThread(self.transfere_donné_envoi, arg = game[0], boucle= False).start()
			MyThread(self.transfere_donné_envoi, arg = game[1], boucle= False).start()
			MyThread(self.transfere_donné_recoi, arg = game[0], boucle= False).start()
			MyThread(self.transfere_donné_recoi, arg = game[1], boucle= False).start()
		

				

	def transfere_donné_envoi(self, client):

		key, place = find_player_in_data(self.all_conexion, client)
		if place == 1 : data_place = 0
		if place == 0 : data_place = 1
		run = True
		while run:

			try: self.all_conexion[key][place]
			except :
				run = False
				break

			try:
				client.send(self.data[key][data_place])
			except:
				if self.client_juste_kick_1 != client:
					self.client_juste_kick_1 = client

					remove_player_partenair(self.all_conexion, client, self.all_conexion_wait)
					del self.all_conexion[key]
					del self.all_thread_client[key]
					del self.data[key][data_place]
					print("client deconecter") 

				run = False
			
	def transfere_donné_recoi(self, client):
		
		key , place = find_player_in_data(self.all_conexion, client)


		run = True
		while run:

			try: self.all_conexion[key][place]
			except :
				run = False
				break
			
			try:
				msg = client.recv(1024)
				self.data[key][place] = msg
				
			except :
				if self.client_juste_kick_1 != client:
					self.client_juste_kick_1 = client

					remove_player_partenair(self.all_conexion, client, self.all_conexion_wait)
					del self.all_conexion[key]
					del self.all_thread_client[key]
					del self.data[key][place]

					print("client deconecter") 
				run = False



	def main(self):
		
		MyThread(self.protocole_client_wating_serveur).start()
		MyThread(self.game).start()
		MyThread(self.accepting_clients_thread).start()
	

NetWwork().init(8080)

