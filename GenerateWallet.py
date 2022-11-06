
#CONNECTING TO XRP LEDGER
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet

# Define the network client

def generateWallet(): # returns private key
    JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
    client = JsonRpcClient(JSON_RPC_URL)

#    Create a wallet using the testnet faucet:
    # https://xrpl.org/xrp-testnet-faucet.html
    test_wallet = generate_faucet_wallet(client, debug=True)


    return [test_wallet.seed, test_wallet.sequence]


