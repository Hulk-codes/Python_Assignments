import sys

def main():
    FileName = sys.argv[1]
    String = sys.argv[2]

    fobj = open(FileName, "r")

    Data = fobj.read()

    if String in Data:
        print(f"The word is found in {FileName}")
    else:
        print(f"The word is not found in {FileName}")


    fobj.close()


if __name__ == "__main__":
    main()