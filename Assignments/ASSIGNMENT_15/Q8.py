from functools import reduce
Div = lambda No : No % 3 == 0 and No % 5 == 0

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Fdata = list(filter(Div, data))
    print("Number divisible by 3 and 5 are: ", Fdata)

if __name__== "__main__":
    main()