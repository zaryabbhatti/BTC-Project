import sys
sys.path.append('C:/Repos/BTC-Project/BTC-Project/packages/')

from packages import requests
import json
import BTCAddress





def get_addy_data():
	bitcoin_address = "1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F"
	num_of_transactions_shown = 1
	response = requests.get(f"https://blockchain.info/rawaddr/{bitcoin_address}?limit={num_of_transactions_shown}")
	response_json = response.json()

	bitcoin_received = response_json["total_received"]
	print(f"total_received is {bitcoin_received}" )

	address = BTCAddress.BTCAddress(response_json)
	return address


x = get_addy_data()

print(x.address)
print(x.total_BTC_received)
print(x.total_BTC_sent)
print(x.final_balance)
