
Add = lambda No1, No2 : No1 + No2


def main():
   
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))
    result = Add(Value1, Value2)
    print("Addition is : ", result)
    
   

if __name__=="__main__":
    main()