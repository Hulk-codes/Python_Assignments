from functools import reduce
Prod = lambda No1 , No2 : No1 * No2

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Rdata = reduce(Prod, data)
    print("Product of elements: ", Rdata)

if __name__== "__main__":
    main()