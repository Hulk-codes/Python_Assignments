import threading                



def DisplayOdd():
    print("Odd Numbers are: ")
    for i in range(1,21,2):
        print(i)

def main():
    t2 = threading.Thread(target=DisplayOdd)

 
    t2.start()

    
    t2.join()

    
if __name__ == "__main__":                                  
    main()