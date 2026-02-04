import threading

def Maximum(No):
    max_value = No[0]
    for i in No:
        if i > max_value:
            max_value = i
    print("maximum number in list is: ", max_value)

def Minimum(No):
    min_value = No[0]
    for i in No:
        if i < min_value:
            min_value = i
    print("minimum number in list is: ", min_value)
    

def main():
    num = list(map(int , input("Enter list of numbers: ").split()))
    t1 = threading.Thread(target=Maximum, args= (num, ))
    t2 = threading.Thread(target=Minimum, args= (num, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()