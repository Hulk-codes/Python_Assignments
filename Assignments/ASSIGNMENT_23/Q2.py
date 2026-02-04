class BankAccount:
    ROI = 10.5
    def __init__(self,A):
        self.Name = A
        self.Amount = 1000

    def Display(self):
        print(f"{self.Name} has {self.Amount} in BANK ACCOUNT")
        print("-" * 40)

    def Deposit(self):
        value = int(input("Enter Amount to deposit: "))
        self.Amount = self.Amount + value
        print(f" Current Bank Balance is : {self.Amount}")
        print("-" * 40)

    def Withdraw(self):
        
        x = int(input("Enter Amount to Withdraw: "))
        if x <= self.Amount:
            self.Amount  = self.Amount -x
            print(f"Current Bank Balance is :  {self.Amount}")
        else:
            print("Insufficient Balance")
            print("-" * 40)
    

    def CalculateIntrest(self):
        Intrest = (self.Amount * BankAccount.ROI) / 100
        print(f"Intrest after withdrawing money is : {Intrest}")
        print("-" * 40)

obj1 = BankAccount("Pranav")
obj1.Display()

obj2 = BankAccount("Pranav")
obj2.Deposit()
obj2.Withdraw()

obj3 = BankAccount("Pranav")
obj3.CalculateIntrest()