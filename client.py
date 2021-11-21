from src.client_handler import SantaClient
import src.config as cfg

client = SantaClient(cfg.ip, cfg.port)
client.receive()