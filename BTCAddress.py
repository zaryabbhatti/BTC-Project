import sys
sys.path.append('C:/Repos/BTC-Project/BTC-Project/packages/')
import json


class BTCAddress:

	def __init__ (self, response_string):

		address_dict = response_string.json()

		self.response_string = response_string
		self.address_dict = address_dict
		self.address = address_dict["address"]
		self.num_transactions = address_dict["n_tx"]
		self.total_BTC_received = address_dict["total_received"]
		self.total_BTC_sent = address_dict["total_sent"]
		self.final_balance = address_dict["final_balance"]
		self.transactions = address_dict["txs"]
		