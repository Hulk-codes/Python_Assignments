from Arithemtic import Add,Sub,Mult,Div

def main():
    Value1 = int(input("Enter 1st Number: "))
    Value2 = int(input("Enter 2nd Number: "))
    print("Additon is:  " , Add(Value1,Value2))
    print("Subtraction is: " , Sub(Value1,Value2))
    print("Multiplication is: " , Mult(Value1,Value2))
    print("Division is: " , Div(Value1,Value2))


if __name__=="__main__":
    main()