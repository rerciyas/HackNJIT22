# Prepare payment
import RebuildWallet
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from xrpl.transaction import safe_sign_and_autofill_transaction
from xrpl.clients import JsonRpcClient
from xrpl.transaction import send_reliable_submission


## RETURNS AN ARRAY OF WALLETs
def sendCrypto(sender_seed, sender_sequence, receiver_seed,receiver_sequence, amount):
    JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
    client = JsonRpcClient(JSON_RPC_URL)
    sender_wallet = RebuildWallet.rebuildWallet(sender_seed,sender_sequence)
    receiver_wallet = RebuildWallet.rebuildWallet(receiver_seed,receiver_sequence)
    my_tx_payment = Payment(
        account=sender_wallet.classic_address,
        amount=xrp_to_drops(amount),
        destination=receiver_wallet.classic_address,
    )

    # Sign the transaction
    my_tx_payment_signed = safe_sign_and_autofill_transaction(my_tx_payment, sender_wallet, client)

    # Submit and send the transaction
    tx_response = send_reliable_submission(my_tx_payment_signed, client)

    return [sender_seed,sender_sequence+1,receiver_seed,receiver_sequence+1]



