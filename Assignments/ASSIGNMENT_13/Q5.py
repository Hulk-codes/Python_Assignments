def Result(No):
    if No < 0 or No > 100:
        print("Invalid marks")
    elif No >= 75 and No <=100:
        print("Distinction")
    elif No >= 60:
        print("First Class")   
    elif No >=50:
        print("Second Class") 
    else: 
        print("Fail")

def main():
    value = int(input("Enter Marks: "))
    Result(value)
   
if __name__ == "__main__":
    main()