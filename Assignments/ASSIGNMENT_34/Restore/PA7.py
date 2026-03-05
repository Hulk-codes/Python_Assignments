import sys

x = 10
print(type(x))
print(id(x))

A = (input("Enter a value: "))
print("Size in bytes is: ",sys.getsizeof(A))
