def count(no):
    sum = 0
    iDigit= 0
    while no != 0:
        iDigit = no % 10
        print(iDigit) 
        sum = sum + iDigit
        no = no // 10
    return sum
           
           
def main():
    ret = 0
    value = int(input("Enter Number: "))
    ret = count(value)
    print(ret)
    
   
if __name__ == "__main__":
    main()