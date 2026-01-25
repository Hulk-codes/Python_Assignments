
CheckOdd = lambda No : True if No % 2 != 0 else False


def main():
   
    Value = int(input("Enter Number: "))
    print(CheckOdd(Value))
if __name__=="__main__":
    main()