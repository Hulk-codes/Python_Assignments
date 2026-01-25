def Prime(no):
   
    for i in range(2,no):
        if no % i == 0:
            return False
    
    return True
           
def main():
    ret = False
    value = int(input("Enter Number: "))
    ret = Prime(value)
    
    if ret == True:
        print("It is Prime number")
    else:
        print("Not prime number")
    

if __name__ == "__main__":
    main()