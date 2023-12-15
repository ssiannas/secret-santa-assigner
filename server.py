from src.server_handler import SantaServer
from src.argparser import ServerParser
import src.config as cfg

if __name__ == "__main__":
	parser = ServerParser()
	ip, port, participant_number = parser.parse()
	server = SantaServer(ip, port, len(cfg.santas))
	server.receive()
