import threading  
            

def DisplayEven( No):
    ESum = 0  
    
    for i in range(1, No+1):
        if No % i == 0 and i % 2 == 0:
            ESum = ESum + i
    print("Sum of Even factors is : ", ESum)
            

def DisplayOdd(No):
    Osum= 0
    
    for i in range(1, No+1):
        if No % i == 0 and i % 2 != 0:
            Osum = Osum + i
    print("Sum of Odd Factors is: ", Osum)


def main():
    num = int(input("Enter Any Number: "))
    EvenFactor = threading.Thread(target=DisplayEven, args=(num ,))
    Oddfactor = threading.Thread(target=DisplayOdd, args=(num , ))

    EvenFactor.start()
    Oddfactor.start()
    

    EvenFactor.join()
    Oddfactor.join()
   
if __name__ == "__main__":                                  
    main()
    print("End of Main thread ")


