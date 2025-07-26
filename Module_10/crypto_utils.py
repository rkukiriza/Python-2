
class CryptoWallet:
    def init_(self, owner):
        self.owner= owner
        self.balance={} 
# creating  a function
def deposit(self,token,amount):
    self.balance[token]=self.balance.get(token,0) + amount
def withdraw(self, token, amount):
    if self.balance.get(token,0)>=amount:
        self.balance[token]-=amount 
#[token,O] means that if the token owner is trying to withdraw,and there is  no balance yet--> it should return 0 instead of 
# creating an error
        return True
    else:
        return False
# show balance
def view_balance(self):
    return self.balance
