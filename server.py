from src.server_handler import SantaServer
from src.argparser import ServerParser

if __name__ == "__main__":
	parser = ServerParser()
	ip, port, participant_number = parser.parse()
	server = SantaServer(ip, port, participant_number)
	server.receive()
