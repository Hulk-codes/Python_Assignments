def Factorial(No):
    fact = 0
    for i in range(1,No):
        if No % i == 0:
            fact = fact + i
            i = i + 1
    return fact



def main():
    ret = 0
    value = int(input("Enter number: "))
    ret = Factorial(value)
    print("Sum of Factors is: " , ret)


if __name__=="__main__":
    main()