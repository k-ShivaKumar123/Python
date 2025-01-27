#Banking system...
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_number = acc   
        
        
        
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("total balance = ",self.get_balance())
        
    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("total balance = ",self.get_balance())
        
    #balance method
    def get_balance(self):
        return self.balance
    
acc1 = Account(20000,12345)
acc1.debit(10000)
acc1.credit(50000)
acc1.debit(10000)

