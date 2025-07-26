from crypto_utils import CryptoWallet

my_wallet=CryptoWallet('Ruth')
my_wallet.deposit("ETH", 0.7)
print(my_wallet.view_balance())

#wallet=cryptowallet("Joseph")
#wallet.deposit("ETH", 0.7)
#wallet.deposit("BTC", 0.1)
#print(wallet.view_balance())
