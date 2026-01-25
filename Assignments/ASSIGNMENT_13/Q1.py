def area(No1, No2):
    print("Area of Rectangle: ", end=" ")
    return (No1 * No2)

    


def main():
    
    x= int(input("Enter lenght of Rectangel: "))
    y= int(input("Enter breadth of Recatangle: "))
    print(area(x,y))


if __name__=="__main__":
    main()
