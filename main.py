import GenerateWallet
import SendCrypto


print("MAKING SENDER WALLET")
senderWallet = GenerateWallet.generateWallet()
print(senderWallet)
print("MAKING RECEIVER WALLET")
receiverWallet = GenerateWallet.generateWallet()
print(receiverWallet)

print("SENDING CRYPTO:100")

info = SendCrypto.sendCrypto(senderWallet[0],senderWallet[1],receiverWallet[0],receiverWallet[1],10)
#in info, there is [sender.seed, sender.sequence, receiver.seed, receiver.sequence]
