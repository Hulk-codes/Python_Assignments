def checkNum(No):
    if No > 0:
        print ("Positive number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter Number: "))
    checkNum(Value)


if __name__=="__main__":
    main()