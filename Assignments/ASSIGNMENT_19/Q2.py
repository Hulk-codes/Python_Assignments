Mult = lambda No1, No2 : No1 * No2


def main():
    ret = 0
    value1=int(input("Enter 1st Number: "))
    value2=int(input("Enter 2nd Number: "))
    ret = Mult(value1,value2)
    print("Multiplication is: ", ret)


if __name__ == "__main__":
    main()