from functools import reduce
Add = lambda No1, No2 : No1 + No2

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Rdata = reduce(Add , data)
    print("ADDITION IS : ", Rdata)

if __name__== "__main__":
    main()