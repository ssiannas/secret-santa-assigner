import socket
import src.config as cfg

class SantaClient:
	def __init__(self, ip, port) -> None:
		self.ip = ip
		self.port = port
		self.__setup()
		self.__get_name()
		print("Waiting for the rest to connect :D . . .")

	def __get_name(self) -> None:
		print("Who are you?")
		for i, name in enumerate(cfg.santas):
			print(f"\t{i+1}. {name}")
		self.name = cfg.santas[int(input()) - 1]
		print("Who are you the secret santa of?")
		for i, name in enumerate(cfg.santees):
			print(f"\t{i+1}. {name}")
		self.santee = cfg.santees[int(input()) - 1]

	def __setup(self) -> None:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.ip, self.port))

	def receive(self) -> None:
		while True:
			try:
				message = self.sock.recv(1024).decode('ascii')
				if message == "NAME":
					self.sock.send(self.name.encode('ascii'))
				elif message == "SANTAOF":
					self.sock.send(self.santee.encode('ascii'))
				elif message == "END":
					print("Finished! :D")
					self.sock.close()
					break
				else:
					if message:
						print(message)
			except Exception as e:
				print("Something went wrong! ", e)
				self.sock.close()
				break
