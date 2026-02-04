class Demo:
    value = 10

    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def fun(self):
        print(self.No1)
        print(self.No2)

    def gun(self):
        print(self.No1)
        print(self.No2)
        
obj1 = Demo(11,21)
obj2 = Demo(51,101)

# print(Demo.value)

obj1.fun()
obj1.gun()

obj2.fun()
obj2.gun()