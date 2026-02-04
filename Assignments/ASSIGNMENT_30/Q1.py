def main():
    FileName = input("Enter File Name: ")
    fobj = open(FileName, "r")

    lines = fobj.readlines()

    print(f"Total number of lines in {FileName} : ", len(lines))

    fobj.close()

if __name__ == "__main__":
    main()