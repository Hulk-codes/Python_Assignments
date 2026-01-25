def findmin(data):
    min = data[0]
    
    for i in data:
        if i < min:
            min = i
    return min

def main():
    ret = 0
    value = int(input("Enter number of elements: "))

    data = list()

    print("Enter the elements: " , end=" ")

    for i in range(value):
        value = int(input())
        data.append(value)
    print (data)
    ret = findmin(data)
    print("Min in elements: " , ret)



if __name__=="__main__":
    main()
