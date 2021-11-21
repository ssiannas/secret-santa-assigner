from src.client_handler import SantaClient
import src.config as cfg

if __name__ == "__main__":
	client = SantaClient(cfg.ip, cfg.port)
	client.receive()