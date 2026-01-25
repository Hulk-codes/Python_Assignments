def reverse(no):
    rev = 0
 
    iDigit= 0
    while no != 0:
        iDigit = no % 10
        rev = rev * 10 + iDigit 
        no = no // 10
        
    return rev
           
           
def main():
    ret = 0
    value = int(input("Enter Number: "))
    ret = reverse(value)
    if ret == value:
        print("palindrome")
    else:
        print("not palindrome")
    print(ret)
    
   
if __name__ == "__main__":
    main()