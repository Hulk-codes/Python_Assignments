def add(data):
    sumdata = 0
    for i in data:
        sumdata = sumdata + i
    return(sumdata)

def main():
    ret = 0
    value = int(input("Enter number of elements: "))

    data = list()

    print("Enter the elements: " , end=" ")

    for i in range(value):
        value = int(input())
        data.append(value)
    print (data)
    ret = add(data)
    print("Sum of elements: " , ret)



if __name__=="__main__":
    main()