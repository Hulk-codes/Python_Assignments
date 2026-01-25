def display(No):
    for i in range (No+1):
        print("*", end=" ")

def main():
    value = int(input("Enter number : "))
    display(value)


if __name__=="__main__":
    main()