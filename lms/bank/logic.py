from .models import *
from .forms import *

def get_balance(public_key=None):
    """Получить баланс кошелька в монетках"""

    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/balance'
    response = requests_lib.get(url)
    respons_json = response.json()
    maticAmount = respons_json.get("maticAmount")
    coinsAmount = respons_json.get("coinsAmount")
    balance = {"maticAmount": maticAmount, "coinsAmount": coinsAmount}
    return balance

def get_balance_NFT(public_key=None):
    """Получить баланс кошелька в NFT"""

    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/nft/balance'
    response = requests_lib.get(url)
    respons_json = response.json()
    balance = respons_json.get("balance")
    return balance

def get_history_transaction(public_key=None):
    """Получить историю транзакций"""

    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/history'
    payload = {"page": 0, "offset": 100, "sort": "asc"}
    response = requests_lib.post(url, data=payload)
    history_transaction = response.json()
    return history_transaction

def get_status_transaction(transaction):
    """Получить статус транзакции"""

    url = f'https://hackathon.lsp.team/hk/v1/transfers/status/{transaction}'
    response = requests_lib.get(url).json()
    status = response.get('status')
    return status

def transfer_rubles(from_private_key, to_public_key, amount):
    """Перевести рубли"""

    url = f'https://hackathon.lsp.team/hk/v1/transfers/ruble'
    payload = {
        "fromPrivateKey": from_private_key,
        "toPublicKey": to_public_key,
        "amount": amount
        }
    response = requests_lib.post(url, data=payload)
    response = response.json()
    transfer_transaction = response.get('transaction', 0)
    if transfer_transaction:
        print(transfer_transaction)
        print(get_status_transaction(transfer_transaction))
        return get_status_transaction(transfer_transaction)
    return response

def transfer_matic(from_private_key, to_public_key, amount):
    """Перевести Матик"""

    url = f'https://hackathon.lsp.team/hk/v1/transfers/matic'
    payload = {
        "fromPrivateKey": from_private_key,
        "toPublicKey": to_public_key,
        "amount": amount
        }
    response = requests_lib.post(url, data=payload)
    transfer_transaction = response.json()
    return transfer_transaction

def transfer_NFT(from_private_key, to_public_key, tokenId):
    """Перевести NFT"""

    url = f'https://hackathon.lsp.team/hk/v1/transfers/nft'
    payload = {
        "fromPrivateKey": from_private_key,
        "toPublicKey": to_public_key,
        "tokenId": tokenId
        }
    response = requests_lib.post(url, data=payload)
    transfer_transaction = response.json()
    return transfer_transaction