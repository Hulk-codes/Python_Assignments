def display(No):
   
    
    for i in range(No+1) : 
        for j in range(0,i):
            j = j + 1
        
            print(j, end=" " )
        print()


def main():
    value = int(input("enter number : "))
    display(value)


if __name__=="__main__":
    main()