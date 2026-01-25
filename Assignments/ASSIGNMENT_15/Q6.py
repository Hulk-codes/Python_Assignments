from functools import reduce
Min = lambda No1 , No2  : No1 if No1 < No2 else No2

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Rdata = reduce(Min, data)
    print("Lowest number is : ", Rdata)

if __name__== "__main__":
    main()