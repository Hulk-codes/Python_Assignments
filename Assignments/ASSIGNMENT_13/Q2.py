def area(No):
    PI = 3.14
    print("Area of Circle: ", end=" ")
    return (PI*(No**2))

    


def main():
    
    x= int(input("Enter radius of circle: "))
    
    print(area(x))


if __name__=="__main__":
    main()
