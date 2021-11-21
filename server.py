from src.server_handler import SantaServer
import src.config as cfg

if __name__ == "__main__":
	server = SantaServer("127.0.0.1", cfg.port)
	server.receive()