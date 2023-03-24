import sys
sys.path.append('C:/Repos/BTC-Project/BTC-Project/packages/')
import json


class BTCAddress:

	def __init__ (self, jsonString):

		self.address = jsonString["address"]
		self.num_transactions = jsonString["n_tx"]
		self.total_BTC_received = jsonString["total_received"]
		self.total_BTC_sent = jsonString["total_sent"]
		self.final_balance = jsonString["final_balance"]
		self.transactions = jsonString["txs"]
		