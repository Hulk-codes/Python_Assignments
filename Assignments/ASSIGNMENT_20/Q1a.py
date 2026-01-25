import threading                

def DisplayEven():
    print("Even Numbers are: ")
    for i in range(2,21,2):
        print(i)



def main():
    even = threading.Thread(target=DisplayEven)
   

    even.start()
    

    even.join()
    

    
if __name__ == "__main__":                                  
    main()