
MaxStr = lambda abc : len(abc) > 5

def main():
  
    data = list(map(str, input("Data =  " ).split()))

    
    Fdata = list(filter(MaxStr, data))
    print("Strings containing more than 5 elements: ", Fdata)

if __name__== "__main__":
    main()