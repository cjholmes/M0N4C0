from cdp import *
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

api_key_name = os.getenv('KEYNAME')

api_key_private_key = os.getenv('SECRET')

Cdp.configure(api_key_name, api_key_private_key)

print("CDP SDK has been successfully configured with CDP API key.")

'''
wallet = Wallet.create()
print(f"Wallet successfully created: {wallet}")
file_path = "garden.json"
wallet.save_seed(file_path, encrypt=True)
'''

fetched_wallet = Wallet.fetch(os.getenv('WALLETID'))
print('successful fetch')

fetched_wallet.load_seed_from_file('garden.json')
print('sucessful rehydration')

# Create a faucet request that returns a Faucet transaction, which can be used to retrieve the transaction hash.
'''faucet_transaction = fetched_wallet.faucet()

# Wait for the faucet transaction to land on-chain.
faucet_transaction.wait()

print(f"Faucet transaction successfully completed: {faucet_transaction}")

faucet_transaction.transaction_hash'''

print(fetched_wallet.balances())


'''url = 'https://api.coinbase.com/v2/exchange-rates'
response = requests.get(url)
ex_rates = json.loads(response.text)
print(ex_rates)'''

import requests

# Define the currency pair
currency_pair = "BTC-USD"

# Base API URL
base_url = "https://api.coinbase.com/v2/prices"

# Headers (optional for public endpoints)
headers = {
    "Accept": "application/json"
}

# Fetch the buy price
buy_url = f"{base_url}/{currency_pair}/buy"
buy_response = requests.get(buy_url, headers=headers)
print("Buy Response:", buy_response.json())
buy_price = buy_response.json()["data"]["amount"] if buy_response.status_code == 200 else None

# Fetch the sell price
sell_url = f"{base_url}/{currency_pair}/sell"
sell_response = requests.get(sell_url, headers=headers)
print("Sell Response:", sell_response.json())  # Debugging line
sell_price = sell_response.json()["data"]["amount"] if sell_response.status_code == 200 else None

# Output the prices
if buy_price and sell_price:
    print(f"Buy Price for {currency_pair}: ${buy_price}")
    print(f"Sell Price for {currency_pair}: ${sell_price}")
else:
    print("Failed to fetch buy or sell price.")
