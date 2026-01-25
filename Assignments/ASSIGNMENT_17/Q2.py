def display(No):
    for i in range(No):
        i=" * " * No
        
        print(i)


def main():
    value = int(input("enter number to print *: "))
    display(value)


if __name__=="__main__":
    main()