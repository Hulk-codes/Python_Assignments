class Arithematic:
    

    def __init__(self):
        self.Value1 = 0 
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter 1st Number: "))
        self.Value2 = int(input("Enter 2nd Number: "))
        
    def Addition(self):
        self.Add = self.Value1 + self.Value2
        print("Addition is: " ,self.Add)
       
    def Subtraction(self):
        self.sub = self.Value1 - self.Value2
        print("Subtraction is: ", self.sub)

    def Multiplication(self):
        self.Mult = self.Value1 * self.Value2
        print("Multiplication is: " , self.Mult)

    def Division(self):
        if self.Value2 != 0:
            print("Division is:", self.Value1 / self.Value2)
        else:
            print("Division by zero is not allowed")

            
obj1 = Arithematic()

obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()
