import requests as requests_lib


#################### WORK WITH RUB ADN MATIC #################################

def get_balance(public_key=None):
    """Получить баланс кошелька в монетках"""

    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/balance'
    response = requests_lib.get(url)
    respons_json = response.json()
    maticAmount = respons_json.get("maticAmount")
    coinsAmount = respons_json.get("coinsAmount")
    balance = {"maticAmount": maticAmount, "coinsAmount": coinsAmount}
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


#################### WORK WITH NFT #################################

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


def get_balance_NFT(public_key=None):
    """Получить баланс кошелька в NFT"""

    url = f'https://hackathon.lsp.team/hk/v1/wallets/{public_key}/nft/balance'
    response = requests_lib.get(url)
    respons_json = response.json()
    balance = respons_json.get("balance")
    return balance  # fields = uri, tokens


def generate_NFT(public_key=None, amount=1):
    """Сгенерировать NFT"""

    url = f'https://hackathon.lsp.team/hk/v1/nft/generate'
    payload = {
        "toPublicKey": public_key,
        "uri": "ipfs://bafybeifesqvvmmtcjlmeso3zaqh56mhttgza2eglw7zwy4ryuyifduy4i/images/star.png",
        "nftCount": amount
    }
    response = requests_lib.post(url, data=payload).json()
    transaction_hash = response.get("transaction_hash") # transaction_hash

    return transaction_hash  #


def NFT_list(transaction_hash_input):
    """Получить список NFT по transaction_hash"""

    url = f'https://hackathon.lsp.team/hk/v1/nft/generate/{transaction_hash_input}'
    response = requests_lib.get(url).json()
    return response # fields = wallet_id, tokens


def get_info_about_NFT(token_id):
    """Получить информацию о NFT по token_id"""

    url = f'https://hackathon.lsp.team/hk/v1/nft/{token_id}'
    response = requests_lib.get(url)
    list_NFT = response.json()
    return list_NFT  # fields = tokenId, uri, publicKey
