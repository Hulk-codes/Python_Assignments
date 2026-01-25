def Add(No1, No2):

    return No1 + No2
    


def main():
    ret = 0
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))
    ret = Add(Value1, Value2)
    print("Addition is: ", ret)
    
   


if __name__=="__main__":
    main()