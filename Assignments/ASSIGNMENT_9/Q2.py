def CHECKGREATER(a,b):
    if a > b :
        print(a,"IS GREATER")
    else:
        print(b, "IS GREATER")

def main():
    x = int(input("ENTER FIRST NUMBER: "))
    y = int(input("ENTER SECOND NUMBER: "))    

    CHECKGREATER(x,y)  




if __name__== "__main__":
    main()