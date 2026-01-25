def SumNaturalNumbers(no):
    Sum = 0
    for i in range(1,no+1):
        Sum = Sum + i
    return Sum 
        

def main():
    ret = 0
    value = int(input("Enter Number: "))
    ret = SumNaturalNumbers(value)
    print("Sum of natural numbers is : " , ret)
   

if __name__ == "__main__":
    main()