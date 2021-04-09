import sys
class customer:
    bankname='indian overseas bank'
    def __init__(self,name,accno,balance=500):
        self.name=name
        self.accno=accno
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.balance)
    def withdrawal(self,amount):
        if amount>self.balance:
            print('insufficientt balance')
        else:
            self.balance=self.balance-amount
            print(self.balance)

print('welcome to',customer.bankname)
name=input('what is your name')
accno=int(input('enter your account no'))


customer1=customer(name,accno)
while True:
    print('d-deposit','w-withdraw','s-stop')
    choice=input('enter your choice')
    if choice=='d':
        amount=int(input('enter your amount'))
        customer1.deposit(amount)
    elif choice=='w':
        amount=int(input('enter amount'))
        customer1.withdrawal(amount)
    elif choice=='s':
        sys.exit()
