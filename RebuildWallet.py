import xrpl.wallet

def rebuildWallet(seed, sequence):
    wallet = xrpl.wallet.Wallet(seed, sequence)
    return wallet