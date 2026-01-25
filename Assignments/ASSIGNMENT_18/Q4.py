def count(no , data):
    cnt = 0

    for i in data:
        if i == no:
            cnt = cnt + 1
        
    return cnt

   

def main():
    
    value = int(input("Enter number of elements: "))

    data = list()

    print("Enter the elements: " , end=" ")

    for i in range(value):
        value = int(input())
        data.append(value)
    print (data)

    Ele  = int(input(("Element to find: " )))
    ret = count(Ele,data)
    print("Frequency of data: ", ret)
  
   


if __name__=="__main__":
    main()
