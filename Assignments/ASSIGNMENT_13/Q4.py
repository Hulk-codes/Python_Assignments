def Binary(No):
    iDigit= " "
    while No != 0:
        iDigit= str(No%2) + iDigit
        No= No // 2
        
    print(iDigit)



def main():
    value = int(input("enter number: "))
    Binary(value)



if __name__ == "__main__":
    main()