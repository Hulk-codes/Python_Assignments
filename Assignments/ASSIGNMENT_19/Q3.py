from functools import reduce

def num(No):
    return 70 <= No <= 90
    


def increment(No):
    return No+ 10

def prod(No1, No2):
    return No1 * No2


def main():
    data = list (map(int , input("Enter data: ").split()))
    print("Input List is : " , data)

    Fdata = list(filter(num , data))
    print ("List after Filter is: ", Fdata )

    Mdata = list(map(increment, Fdata))
    print("List after mapping is: ", Mdata)

    Rdata = reduce(prod, Mdata)
    print("Data after Reudcing list is: ", Rdata)


if __name__ == "__main__":
    main()

