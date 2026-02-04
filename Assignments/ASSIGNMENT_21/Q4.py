import threading

def Sum(No):
    isum = 0
    for i in No:
        isum= isum + i
    print("Sum is: " ,isum)


def Product(No):
    prod= 1
    for i in No:
        prod = prod * i
    print("Product is: " ,prod)
    

def main():
    num = list(map(int , input("Enter list of numbers: ").split()))
    t1 = threading.Thread(target=Sum, args= (num, ))
    t2 = threading.Thread(target=Product, args= (num, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()