    #def sqr(No):
    #print("Square of the number: ")
    #return No * No

sqr = lambda No : No * No

def main():
    ret = 0 
    Value = int(input("Enter Number: "))
    ret= sqr(Value)
    print("Square of the number: ",ret)


if __name__=="__main__":
    main()