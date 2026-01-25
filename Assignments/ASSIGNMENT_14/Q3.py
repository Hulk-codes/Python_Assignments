
Max = lambda No1, No2 : No1 if No1 > No2 else No2


def main():
   
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))
    result = Max(Value1, Value2)
    print(result, " is greater")
   

if __name__=="__main__":
    main()