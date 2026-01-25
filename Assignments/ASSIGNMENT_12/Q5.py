def line(No):
    i = 1
    while i <= No:
        print(No, end=" ")
        No = No - 1

def main():
    x = int(input("ENTER ANY NUMBER: "))
    line(x)


if __name__=="__main__":
    main()

