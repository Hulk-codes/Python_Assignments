from functools import reduce
Counteven = lambda No : No % 2 == 0

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Fdata = list(filter(Counteven , data))
    print(" Total Even numbers are : ", len(Fdata))

if __name__== "__main__":
    main()