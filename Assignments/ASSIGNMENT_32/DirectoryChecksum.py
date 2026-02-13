import hashlib
import os
import sys

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1000)

    while(len(buffer)> 0):
        hobj.update(buffer)
        buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryCheck(DirectoryName):
    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a Directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName , fname)
            Checksum = CalculateCheckSum(fname)

            print(f"File Name:  {fname} Checksum : {Checksum}")


def main():
    DirectoryCheck(sys.argv[1])

if __name__ == "__main__":
    main()
