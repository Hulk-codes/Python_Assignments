Power2 = lambda No : 2 ** No


def main():
    ret = 0
    value=int(input("Enter the number: "))
    ret = Power2(value)
    print("Output is: ", ret)


if __name__ == "__main__":
    main()