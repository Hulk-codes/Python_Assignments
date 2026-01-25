from functools import reduce
Max = lambda No1 , No2  : No1 if No1 > No2 else No2

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Rdata = reduce(Max, data)
    print("Highest number is : ", Rdata)

if __name__== "__main__":
    main()