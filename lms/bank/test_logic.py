from time import sleep

from logic import *
import json

public_key = "0x0787638C8EdA33712B1FbC2dCF3dfa6603fa0C54"

transaction_hash = generate_NFT(public_key=public_key, amount=2)
transaction_hash_input = json.loads(transaction_hash).get("transaction_hash")
print(transaction_hash_input)
sleep(10)
temp = NFT_list(transaction_hash_input=f"{transaction_hash_input}")
print(temp)
