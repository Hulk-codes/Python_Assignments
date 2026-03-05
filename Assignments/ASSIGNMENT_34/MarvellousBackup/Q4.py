def Even(no):
    for i in range(2,no+1):
        if i % 2 == 0:
            print(i)
            
           
           
def main():
    ret = 0
    value = int(input("Enter Number: "))
    Even(value)
    
   

if __name__ == "__main__":
    main()