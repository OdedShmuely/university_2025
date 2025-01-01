class BankAccount:
    def __init__(self, account_holder, account_number):
        if not isinstance(account_number, int):
            raise TypeError
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0.0
    def __str__(self):
        return f'Account holder: {self.account_holder}\nAccount number: {self.account_number}\nBalance: ${self.balance}'
    def deposit(self,amount):
        self.balance += amount
        print(f'Deposited: ${amount}. New balance: ${self.balance}')
    def withdraw(self,amount):
        if amount > self.balance: print('Insufficient funds. withdrawal canceled.')
        else:
            self.balance -= amount
            print(f'Withdrawal: ${amount}. New balance: ${self.balance}')
    def __add__(self, other):
        self.account_holder = self.account_holder + ' & ' + other.account_holder
        if self.account_number < other.account_number:
            self.account_number = other.account_number
        self.balance += other.balance


oded = BankAccount('oded', 12345)
print(oded)
oded.deposit(200)
oded.withdraw(100)

# def exception_function(lst,i,value):
    # if type(value) != int or type(lst) != list or

lst = []
lst.append(1)
lst.append(2)
lst.append(3)
lst.pop()
print(lst)


