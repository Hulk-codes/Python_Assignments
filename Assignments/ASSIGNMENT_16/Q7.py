def Divby5(No):
    flag = True
    if No % 5 == 0:
        print(flag)
    else:
        print(False)
    


def main():
    Value = int(input("Enter Number: "))
    Divby5(Value)
   

if __name__=="__main__":
    main()