import socket
import random
import src.config as cfg

class SantaServer:
	def __init__(self, ip, port, participant_no) -> None:
		self.ip = ip
		self.port = port
		self.__setup()
		self.participant_number = participant_no
		self.__giftees = {}
		self.__name_to_socket = {}

	def __setup(self) -> None:
		# Setup an internet, streaming server and bind it to the port / ip
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.ip, self.port))
		self.sock.listen()
		print(f"Server is listening on port {self.port} . . .")

	def __send_termination_msg(self) -> None:
		for client in self.__name_to_socket:
			self.__name_to_socket[client].send("END".encode('ascii'))

	def __xmas_magic(self) -> None:
		missing = None
		for giftee in self.__giftees:
			if giftee == "None":
				missing = self.__giftees[giftee]

		loner = list(filter(lambda x: x not in self.__giftees.keys(), cfg.santas))[0]
		try:
			message = "You are the secret santa of: " + loner
			self.__name_to_socket[missing].send(message.encode('ascii'))
		except:
			print("Something went wrong!")

	def receive(self) -> None:
		while True:
			client, addr = self.sock.accept()
			print("Connection Received by: ", str(addr))

			client.send("NAME".encode('ascii'))
			name = client.recv(1024).decode('ascii')
			client.send("SANTAOF".encode('ascii'))
			santa_of = client.recv(1024).decode('ascii')

			self.__giftees[santa_of] = name
			self.__name_to_socket[name] = client
			if len(self.__name_to_socket) == self.participant_number:
				self.__xmas_magic()
				self.__send_termination_msg()
				self.sock.close()
				break
