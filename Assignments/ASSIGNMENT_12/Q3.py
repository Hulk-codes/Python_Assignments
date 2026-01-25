
def add(No1, No2):
    Ans = No1 + No2
    print("addition is: ", Ans) 
    

def Sub (No1, No2):
    Ans = No1 - No2
    print("Subtraction is: ", Ans) 
    

def multiply(No1, No2):
    Ans = No1 * No2
    print("multiplication  is: ", Ans) 
    

def div(No1, No2):
    if No2 == 0:
        print("Division not possible")
    else:
        Ans = No1 // No2
        print("Division is :", Ans)


        
def main():
    x = int(input("enter first number: "))
    y = int(input("enter second number: "))
    add(x,y)
    Sub(x,y)
    multiply(x,y)
    div(x,y)

   

if __name__== "__main__":
    main()