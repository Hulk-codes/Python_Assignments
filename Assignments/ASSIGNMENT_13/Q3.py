def Factor(No):
    isum = 0
    for i in range(1,No):
        if No % i == 0:
            isum = isum+i
    if isum == No:
        print("Perfect Number")
    else:
        print("Not a perfect Number")
    
       
def main():
   
    value =int (input("enter the number : "))
    Factor(value)
    

    

if __name__ == "__main__":
    main()