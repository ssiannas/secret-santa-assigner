from src.server_handler import SantaServer
from src.argparser import ServerParser

if __name__ == "__main__":
	parser = ServerParser()
	port, participant_number = parser.parse()
	server = SantaServer("127.0.0.1", port, participant_number)
	server.receive()