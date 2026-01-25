def Factorial(No):
    i = 1
    fact = 1
    while i <= No:
        fact = fact * i
        i = i +1
    return fact

   

def main():
    ret = 0
    value = int(input("Enter number: "))
    ret = Factorial(value)
    print("Factorial is : " , ret)


if __name__=="__main__":
    main()