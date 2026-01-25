def table(no):
    mult = 0
    for i in range(1,11,1):
        mult = i * no
        print(mult)

def main():
    
    value = int(input("Enter Number: "))
    table(value)
   

if __name__ == "__main__":
    main()