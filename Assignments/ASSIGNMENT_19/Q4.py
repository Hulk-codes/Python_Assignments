from functools import reduce

def Even(No):
    return No %  2 == 0
    
def increment(No):
    return No ** 2

def prod(No1, No2):
    return No1 + No2


def main():
    data = list (map(int , input("Enter data: ").split()))
    print("Input List is : " , data)

    Fdata = list(filter(Even , data))
    print ("List after Filter is: ", Fdata )

    Mdata = list(map(increment, Fdata))
    print("List after mapping is: ", Mdata)

    Rdata = reduce(prod, Mdata)
    print("Output for reduce is: ", Rdata)


if __name__ == "__main__":
    main()

