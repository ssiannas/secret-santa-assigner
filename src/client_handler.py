import socket 

class SantaClient:
	def __init__(self, ip, port) -> None:
		self.ip = ip
		self.port = port
		self.__setup()
		self.__get_name()
		print("Waiting for the rest to connect :D . . .")
	
	def __get_name(self) -> None:
		self.name = input("What is your name?\n")

	def __setup(self) -> None:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.ip, self.port))

	def receive(self) -> None:
		while True:
			try:
				message = self.sock.recv(1024).decode('ascii')
				if message == "NAME":
					self.sock.send(self.name.encode('ascii'))
				elif message == "END":
					self.sock.close()
					break
				else:
					if message:
						print(message)
			except Exception as e:
				print("Something went wrong! ", e)
				self.sock.close()
				break
