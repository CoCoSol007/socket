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

	def protocole_client_wating_serveur(self):

		for client in self.all_conexion_wait:
			try:
				client.send(cripteur_bytes(numbre_waiting))
			except ConnectionError: 
				print("client deconecter")
				self.all_conexion_wait.remove(client)

	def send_to_client(self, client, data = list):
		data = cripteur_bytes(data)
		client.send(data)

	def accepting_clients_thread(self):

		# on accepte les joueur
		Client, adresse =  self.connexion.accept()

		#on l'ajoute a la liste
		self.all_conexion_wait.append(Client)


		print ("New client : " + str(adresse[0]))
		print("there is now : " + str(len(self.all_conexion_wait) + get_nombre_client(self.all_conexion)) + " clien")


	def game(self):

		verifi_client_partenaire(self.all_conexion, self.all_conexion_wait)   # on verifi si chaque client a son partenaire 

		if len(self.all_conexion_wait) % 2 == 0 and len(self.all_conexion_wait) > 0 :
			taille = len(self.all_conexion)
			self.all_conexion[str(taille + 1)] = self.all_conexion_wait
			self.all_conexion_wait = []

		self.transfere_donné()

	def transfere_donné(self):
		
		pass



	def main(self):
		
		MyThread(self.protocole_client_wating_serveur).start()
		MyThread(self.game).start()
		MyThread(self.accepting_clients_thread).start()
		
		


NetWwork().init(8080)

			