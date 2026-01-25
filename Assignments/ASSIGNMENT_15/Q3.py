from functools import reduce
Checkodd = lambda No : No % 2 != 0

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Fdata = list(filter(Checkodd , data))
    print("Odd numbers are : ", Fdata)

if __name__== "__main__":
    main()