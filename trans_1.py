from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

#nonce = w3.eth.getTransactionCount('0xBE0C4eDc36a2ec3e76F011ea7C2560b48b49d313')

gas_price = w3.eth.gasPrice
print(gas_price/ 10 ** 6)