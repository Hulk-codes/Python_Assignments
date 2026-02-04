import threading

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def Prime(numbers):
    print("Prime numbers are:", end=" ")
    for num in numbers:
        if isPrime(num):
            print(num, end=" ")
    print()


def NonPrime(numbers):
    print("Non-prime numbers are:", end=" ")
    for num in numbers:
        if not isPrime(num):
            print(num, end=" ")
    print()

def main():
    num = list(map(int , input("Enter list of numbers: ").split()))
    t1 = threading.Thread(target=Prime, args= (num, ))
    t2 = threading.Thread(target=NonPrime, args= (num, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()