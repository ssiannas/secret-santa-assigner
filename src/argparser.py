import argparse
from typing import DefaultDict, Tuple
import src.config as cfg

class ServerParser:
	def __init__(self) -> None:
		self.parser = argparse.ArgumentParser(description="Host the Secret Santa assignment server")
		self.parser.add_argument('-p','--port', type=int, default=cfg.port, help="The port in which the server should be setup")
		self.parser.add_argument('-n', '--number', type=int, default=cfg.participant_number, help="The number of participants that will take place")

	def parse(self) -> tuple:
		args = self.parser.parse_args()
		return args.port, args.number

class ClientParser:
	def __init__(self) -> None:
		self.parser = argparse.ArgumentParser(description="Client of the Secret Santa assignment event")
		self.parser.add_argument('-ip','--addr', type=str, default=cfg.ip, help="The ip address of the Secret Santa host")
		self.parser.add_argument('-p','--port', type=int, default=cfg.port, help="The port in which the server is setup")

	def parse(self) -> tuple:
		args = self.parser.parse_args()
		return args.addr, args.port 