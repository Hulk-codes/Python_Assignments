def div(No):
    if No % 3 == 0 or No % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible")

def main():
    a = int(input("Enter number: "))

    (div(a))

if __name__ == "__main__":
    main()