def findmax(data):
    max = data[0]
    
    for i in data:
        if i > max:
            max = i
    return max

def main():
    ret = 0
    value = int(input("Enter number of elements: "))

    data = list()

    print("Enter the elements: " , end=" ")

    for i in range(value):
        value = int(input())
        data.append(value)
    print (data)
    ret = findmax(data)
    print("Max in elements: " , ret)



if __name__=="__main__":
    main()
