def calculate(No):
    isum = 0
    while No != 0:
        digit = No % 10
        isum = isum + digit
        No = No // 10
    print("Sum of digits:", isum)


def main():
    value = int(input("Enter Number: "))
    calculate(value)


if __name__ == "__main__":
    main()
