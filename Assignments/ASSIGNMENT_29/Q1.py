import os

def main():
    FileName = input("Enter The name of file: ")

    ret = os.path.exists(FileName)      # it will verify the path where the file exists 

    if (ret == True):
        fobj = open(FileName, "r")
        print("File gets successfully open")
        fobj.close()

    else:
        print("there is no File")

if __name__ == "__main__":
    main()