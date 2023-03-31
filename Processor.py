import sys
sys.path.append('C:/Repos/BTC-Project/BTC-Project/packages/')

from packages import requests
import json
import DTO.BTCAddress as BTCAddress
import DTO.Transaction as Transaction
def get_address_data(bitcoin_address):

	try:
		bitcoin_address = "bc1q3sn68x4qegp5776narh78rlh0y385mw8a3dnfq"
		response = requests.get(f"https://blockchain.info/rawaddr/{bitcoin_address}")
		address = BTCAddress.BTCAddress(response)
		return address

	except:
		raise Exception("Failed in: " + get_address_data.__qualname__ + "\nStatus Code: " + str(response.status_code))
	

def get_largest_single_payment_by_address(bitcoin_address):

	# ONLY GIVES LARGEST SENT SINGLE PAYMENT BASED ON LAST 50 TRANSACTIONS
	try:
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
	except:
		raise Exception("Failed in: " + get_largest_single_payment_by_address.__qualname__ )


def get_transaction_details(transaction):
	try:
		response = requests.get(f"https://blockchain.info/rawtx/{transaction}")
		transaction = Transaction.Transaction(response)

		return transaction

	except:
		raise Exception("Failed in: " + get_transaction_details.__qualname__ )

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

def get_largest_single_received_payment_by_address(bitcoin_address):

	# ONLY GIVES LARGEST RECEIVED PAYMENT BASED ON LAST 50 TRANSACTIONS
	try:
		address = get_address_data(bitcoin_address)
		maxReceived = -1
		list_of_transactions = address.transactions
		hasBatchTransactions = contains_batch_transactions(list_of_transactions)

		if hasBatchTransactions:
			print('********Batch transaction********')
			for transaction in address.transactions:
				for inpt in transaction["inputs"]:
					if inpt["prev_out"]["spent"] == False:
						maxReceived = max(maxReceived, inpt["prev_out"]["value"])
				
		else:
			print('********Single transaction********')
			for transaction in address.transactions:
				if transaction["inputs"][0]["prev_out"]["spent"] == False:
					transactionVal = int(transaction["inputs"][0]["prev_out"]["value"])
					maxReceived = max(maxReceived, transactionVal )

		return maxReceived
	except:
		raise Exception("Failed in: " + get_largest_single_received_payment_by_address.__qualname__ )


def get_largest_spent_transaction (bitcoin_address):
	try:
		address = get_address_data(bitcoin_address)
		maxSpent = 100
		list_of_transactions = address.transactions
		
		for transaction in list_of_transactions:

			if(transaction["result"] < 0):
				maxSpent = min(maxSpent, transaction["result"])

		return maxSpent * -1

	except:
		raise Exception("Failed in: " + get_largest_spent_transaction.__qualname__ )

def get_largest_received_transaction (bitcoin_address):
	try:
		address = get_address_data(bitcoin_address)
		maxReceived = -1
		list_of_transactions = address.transactions
		
		for transaction in list_of_transactions:
			
			if(transaction["result"] > 0):
				maxReceived = max(maxReceived, transaction["result"])

		return maxReceived 
	except:

		raise Exception("Failed in: " + get_largest_received_transaction.__qualname__ )

def sandbox (test):
	bitcoin_address = "bc1q3sn68x4qegp5776narh78rlh0y385mw8a3dnfq"
	response = requests.get(f"https://blockchain.info/rawaddr/{bitcoin_address}")
	address = BTCAddress.BTCAddress(response)
	print(address.transactions)

#

x = get_largest_spent_transaction("test")
print(x)



# 4656289 
# + 1525294
#  - 5404664
#   - 773312