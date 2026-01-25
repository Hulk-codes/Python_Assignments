from functools import reduce
Sqr = lambda No : No * No

def main():
  
    data = list(map(int,input("Data =  " ).split()))

    
    Mdata = list(map(Sqr , data))
    print("Square of the data is : ", Mdata)

if __name__== "__main__":
    main()