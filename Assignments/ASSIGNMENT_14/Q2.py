Cube = lambda No : No * No * No

def main():
    ret = 0 
    Value = int(input("Enter Number: "))
    ret= Cube(Value)
    print("Cube of the number: ",ret)


if __name__=="__main__":
    main()