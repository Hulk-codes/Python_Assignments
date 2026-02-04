class Numbers:
    def __init__(self):
        self.Value = int(input("Enter Number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            print(False)
            return
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                print(False)
                return
        print(True)

    def ChkPerfect(self):
        Sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                Sum = Sum+i
        if Sum == self.Value:
            print(True)
        else:
            print(False)

    def Factors(self):
        print("Factors are: ")
        for i in range (1,(self.Value+1)):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        Fsum = 0
        for i in range (1,(self.Value+1)):
            if self.Value % i == 0:
                Fsum = Fsum + i
        print("Sum of Factors is : " , Fsum)

obj = Numbers()
obj.ChkPrime()
obj.ChkPerfect()
obj.Factors()
obj.SumFactors()