import sys
sys.path.append('C:/Repos/BTC-Project/BTC-Project/packages/')

from packages import requests
import json
import DTO.BTCAddress as BTCAddress

def get_address_data(bitcoin_address):
	bitcoin_address = "bc1q3sn68x4qegp5776narh78rlh0y385mw8a3dnfq"
	response = requests.get(f"https://blockchain.info/rawaddr/{bitcoin_address}")

	if response.status_code != 200 :
		print("**************BAD RESPONSE FROM API****************\n" * 5)
		raise Exception("THE API IS RETURNING A BAD REPONSE, CHECK STATUS CODE")

	address = BTCAddress.BTCAddress(response)
	return address

def get_largest_sent_transaction_by_address(bitcoin_address):

	# ONLY GIVES LARGEST SENT TRANSACTION BASED ON LAST 50 TRANSACTIONS
	address = get_address_data(bitcoin_address)
	maxSpent = -1
	list_of_transactions = address.transactions
	hasBatchTransactions = contains_batch_transactions(list_of_transactions)

	if hasBatchTransactions:
		print('********Batch transaction********')
		for transaction in address.transactions:
			for inpt in transaction["inputs"]:
				if inpt["prev_out"]["spent"] == True:
					maxSpent = max(maxSpent, inpt["prev_out"]["value"])
			
	else:
		print('********Single transaction********')
		for transaction in address.transactions:
			print(transaction["inputs"])
			if transaction["inputs"][0]["prev_out"]["spent"] == True:
				transactionVal = int(transaction["inputs"][0]["prev_out"]["value"])
				maxSpent = max(maxSpent, transactionVal )

				
	return maxSpent


def write_to_file(stringToBeWrittenToFile):
	with open('output.txt', 'w') as f:
		f.write(stringToBeWrittenToFile)

    #with open('output.txt', 'w') as f:
    #f.write(json.dumps(x.address_dict))

def contains_batch_transactions(transaction_list):

	for transaction in transaction_list:
		if len(transaction["inputs"]) > 1:
			return True

	return False

#x = get_addy_data("gggg")
#y = get_largest_sent_transaction_by_address("bc1q3sn68x4qegp5776narh78rlh0y385mw8a3dnfq")




