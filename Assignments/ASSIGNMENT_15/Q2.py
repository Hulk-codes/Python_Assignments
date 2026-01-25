from functools import reduce
Checkeven = lambda No : No % 2 == 0

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Fdata = list(filter(Checkeven , data))
    print("Even numbers are : ", Fdata)

if __name__== "__main__":
    main()