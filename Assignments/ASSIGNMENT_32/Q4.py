import sys
import os
import hashlib
import time

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1000)

    while(len(buffer)> 0):
        hobj.update(buffer)
        buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryScanner(DirName):

    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("there is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("it is not a directory")
        return
    

    Duplicatefiles = {}
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName , fname)
            Checksum = CalculateCheckSum(fname)

            if Checksum in Duplicatefiles:
                Duplicatefiles[Checksum].append(fname)
            else: 
                Duplicatefiles[Checksum] = [fname]

    for Checksum, files in Duplicatefiles.items():

        if len(files) > 1:

            DuplicateFolder = os.path.dirname(files[0])

            LogFilePath = os.path.join(DuplicateFolder, "Log.txt")

            border = "-" * 52

            fobj = open(LogFilePath , "a")   
        
            fobj.write(border+"\n")
            fobj.write("This is a file created by Pranav\n")
            fobj.write(border+"\n")
                
            for file in files:
                print("Duplicate File:", file)
                fobj.write(file + "\n")

            for file in files[1:]:
                try:
                    os.remove(file)
                    print("Deleted:", file)
                except:
                    print("Unable to delete:", file)

            fobj.write("-"*50 + "\n")

            fobj.close()


def main():
    border = "-" * 52
    print(border)
    print("-----------Marvellous Directory Automation----------")
    print(border)

    if (len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("Please specify the name of Directory")
        return
    
    StartTime = time.time()
    DirectoryScanner(sys.argv[1])
    EndTime = time.time()

    print("Total time of execution: ", EndTime - StartTime)

    print(border)
    print("-----------Marvellous Directory Automation----------")
    print(border)

if __name__ =="__main__":
    main()