from src.client_handler import SantaClient
from src.argparser import ClientParser

if __name__ == "__main__":
	parser = ClientParser()
	host, port = parser.parse()
	client = SantaClient(host, port)
	client.receive()