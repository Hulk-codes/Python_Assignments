def count(no):
    icount = 0
    
    while no != 0:
        
        icount = icount + 1
        no = no // 10
    return icount
           
           
def main():
    ret = 0
    value = int(input("Enter Number: "))
    ret = count(value)
    print(ret)
    
   
if __name__ == "__main__":
    main()