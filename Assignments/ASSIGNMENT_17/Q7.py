def display(No):
   
    for i in range(1,No+1):
        
        for j in range(0,No):
            j = j + 1
        
            print(j, end=" " )
        print()


def main():
    value = int(input("enter number : "))
    display(value)


if __name__=="__main__":
    main()