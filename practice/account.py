class Bank_Account():
    def __init__(self , owner , balance , account_no):
        self.owner = owner
        self.balance = balance
        self.account_no = account_no

    def deposit(self , amount):
        self.balance += amount
        print (f"this is the total amount after deposite : {self.balance}")

    def withdraw(self , ammount):
        if ammount > self.balance:
            print("Infullent Balance")

        else:
            self.balance -= ammount
            print(f"This is the total ammount after withdraw : {self.balance}")

acc1 = Bank_Account("Dev" , 5000 , "1234567890")
acc1.deposit(5000)
acc1.withdraw(10000)
        