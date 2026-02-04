class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

    def Accept(self):
        self.Radius = int(input("Enter radius of circle: "))
        
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        
    def CalculateCircumference(self):
        self.Circumference = 2 * (Circle.PI * self.Radius)
       
    def display(self):
        print("redius is : ", self.Radius)
        print("Circumference is : " , self.Circumference)
        print("Area is : " , self.Area)

obj1 = Circle()
obj2 = Circle()

print("Enter details for first circle")
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.display()

print("-" * 100)

print("Enter details for second circle")
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.display()

print("-" * 100)


