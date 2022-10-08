from .models import *
from .forms import *

def get_balance(public_key=None):
    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/balance'
    response = requests_lib.get(url)
    respons_json = response.json()
    maticAmount = respons_json.get("maticAmount")
    coinsAmount = respons_json.get("coinsAmount")
    balance = {"maticAmount": maticAmount, "coinsAmount": coinsAmount}
    return balance


def get_history_transaction(public_key=None):
    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/history'
    payload = {"page": 0, "offset": 100, "sort": "asc"}
    response = requests_lib.post(url, data=payload)
    history = response.json()
    return history

def transfer_rubles(from_private_key, to_public_key, amount):
    url = f'https://hackathon.lsp.team/hk/v1/transfers/ruble'
    payload = {
        "fromPrivateKey": from_private_key,
        "toPublicKey": to_public_key,
        "amount": amount
        }
    response = requests_lib.post(url, data=payload)
    transfer = response.json()
    return transfer