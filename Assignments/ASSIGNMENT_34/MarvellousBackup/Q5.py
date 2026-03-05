def odd(no):
    for i in range(1,no+1):
        if i % 2 != 0:
            print(i)
            
           
           
def main():
    ret = 0
    value = int(input("Enter Number: "))
    odd(value)
    
   

if __name__ == "__main__":
    main()