import sys

def main():
    FileName = sys.argv[1]
    String = sys.argv[2]

    fobj = open(FileName, "r")

    Data = fobj.read()

    Count = Data.count(String)

    print(Count)

    fobj.close()


if __name__ == "__main__":
    main()