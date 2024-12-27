from cdp import *
from dotenv import load_dotenv
import os
import requests

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

