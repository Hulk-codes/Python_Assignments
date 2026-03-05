def Addition(value1, value2):
    Ans = 0
    Ans = value1 + value2
    return Ans

def Substraction(value1, value2):
    Ans = 0
    Ans = value1 - value2
    return Ans
def Multiplication(value1, value2):
    Ans = 0
    Ans = value1 * value2
    return Ans
def Division(value1, value2):
    Ans = 0 
    Ans = value1/value2
    return Ans
def main():

    No1 = 0
    No2 = 0
    Choice = 0

    print("Welcome to calcy :")

    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    print("Choices are : ")

    print("1: Addition")
    print("2: Substraction")
    print("3: Multiplication")
    print("4: Divison")

    while(Choice < 5):

        Choice = int(input("Enter your choice : "))

        if Choice == 1:
            result = Addition(No1,No2)
            print("Addition is: ",result)
        elif Choice == 2:
            result = Substraction(No1,No2)
            print("Substraction is: ",result)
        elif Choice == 3:
            result = Multiplication(No1, No2)
            print("Multiplication is: ", result)  
        elif Choice == 4:
            result = Division(No1,No2)  
            print("Division is: ", result)
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()