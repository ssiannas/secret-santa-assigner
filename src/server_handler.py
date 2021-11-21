import threading
import socket
import random

class SantaServer:
	def __init__(self, ip, port) -> None:
		self.ip = ip
		self.port = port
		self.__setup()
		self.participant_number = 2
		self.clients = []
		self.names = []
		
	def __setup(self) -> None:
		# Setup an internet, streaming server and bind it to the port / ip
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.ip, self.port))
		self.sock.listen()
		print(f"Server is listening on port {self.port} . . .")

	def __check_list(self) -> bool:
		for participant in self.participants:
			p_index = self.participants.index(participant)
			if (self.names[p_index] == participant):
				return False
		return True

	def __send_termination_msg(self) -> None:
		for client in self.clients:
			client.send("END".encode('ascii'))

	def __xmas_magic(self) -> None:
		self.participants = list(self.names)
		while not self.__check_list():
			random.shuffle(self.participants)
		for client in self.clients:
			c_index = self.clients.index(client)
			try:
				message = "You are the secret santa of: " + self.participants[c_index]
				client.send(message.encode('ascii'))
			except:
				print("Something went wrong!")
				break


	def receive(self) -> None:
		while True:
			client, addr = self.sock.accept()
			print("Connection Received by: ", str(addr))

			client.send("NAME".encode('ascii'))
			name = client.recv(1024).decode('ascii')
			self.names.append(name)
			self.clients.append(client)
			
			if len(self.clients) == self.participant_number:
				self.__xmas_magic()
				self.__send_termination_msg()
				self.sock.close()
				break

			