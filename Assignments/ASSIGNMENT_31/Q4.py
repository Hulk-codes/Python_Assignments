import os
import sys


def DirectoryScanner(DirectoryName1):
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName1):
            for fName in FileName:
                Fullpath = os.path.join(FolderName,fName)
                print("File Name: " , Fullpath)

def CopyFilesInDirectory(DirectoryName1, DirectoryName2,Extension):

    ret = os.path.exists(DirectoryName2)
    if ret == False:
        os.mkdir(DirectoryName2)
    
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName1):
        for NewfName in FileName:

            if NewfName.endswith(Extension):
            
                SRC_path = os.path.join(FolderName,NewfName)
                DST_path = os.path.join(DirectoryName2, NewfName)

                fobj1 = open(SRC_path, "rb")
                data = fobj1.read()
                fobj1.close()

                fobj2 = open(DST_path, "wb")
                fobj2.write(data)
                fobj2.close() 

                print("Copied Files: ", NewfName)
        
def main():
    if len(sys.argv) < 3:
        print("Usage: FileName.py <SourceDir> <DestDir>")
        return

    DirectoryScanner(sys.argv[1])
    CopyFilesInDirectory(sys.argv[1], sys.argv[2], sys.argv[3])
                
                
if __name__ == "__main__":
    main()