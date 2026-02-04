def main():
    FileName = input("Enter File Name: ")
    fobj = open(FileName, "r")

    data = fobj.read()

    words = data.split()

    print(f"Total number of Words in {FileName} : ", len(words))

    fobj.close()

if __name__ == "__main__":
    main()