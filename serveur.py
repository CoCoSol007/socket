import socket
from threading import Thread
from constant import *


class NetWwork:
	def init(self, port):
		self.host = ''
		self.port = port

		self.all_conexion = {}
		self.all_conexion_wait = []
		self.all_thread_client = []

		self.connexion = socket.socket()
		self.connexion.bind((self.host, self.port))
		print('server launch...')
		
		self.connexion.listen()

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

		verifi_client_partenaire(self.all_conexion, self.all_conexion_wait)   # on verifi si chaque client a son partenaire 

		if len(self.all_conexion_wait) % 2 == 0 and len(self.all_conexion_wait) > 0 :
			taille = len(self.all_conexion)
			self.all_conexion[str(taille + 1)] = self.all_conexion_wait
			self.all_conexion_wait = []
			self.all_thread_client.append(False)
			
		self.socuper_donné_thread()

	def socuper_donné_thread(self):
		
		for game in recupe_game_non_thread(self.all_conexion, self.all_thread_client):
			Game = self.all_conexion[game]
			clientA =  Game[0]
			clientB = Game[1]
			MyThread(self.transfere_donné, arg = (clientA, clientB), boucle= False).start()
			MyThread(self.transfere_donné, arg = (clientB, clientA), boucle= False).start()

				

	def transfere_donné(self, clients):
		clientA, clientB = clients[0],clients[1]
		while True:
			try:
				msg = clientB.recv(128)
				clientA.send(msg)
			except ConnectionError: 
				del clientA
				print("client deconecter")
				verifi_client_partenaire(self.all_conexion, self.all_conexion_wait, self.all_thread_client) 
				break



	def main(self):
		
		MyThread(self.protocole_client_wating_serveur).start()
		MyThread(self.game).start()
		MyThread(self.accepting_clients_thread).start()
	

NetWwork().init(8080)

			