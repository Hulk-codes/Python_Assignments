import os

def DirectoryScanner(DirectoryName):
  

    ret = os.path.exists(DirectoryName)
    if(ret == False):
        Logfile("There is no such Directory")
        return False
    
    ret = os.path.isdir(DirectoryName)
    if(ret == False):
        Logfile("It is not a Directory")
        return False

    Logfile("Directory validation successful")
    return True

def DirectoryFileWithExtension(DirectoryName, Extension1):

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fName in FileName:
            if fName.endswith(Extension1):
                Logfile("File Found: " +fName)

def ReplaceExtensionDoc(DirectoryName, Extension1, ReplaceExtension2):
        for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
            for fName in FileName:
                if fName.endswith(Extension1):
                    oldPath = os.path.join(FolderName, fName)

                    newName = fName.replace(Extension1, ReplaceExtension2)
                    newPath = os.path.join(FolderName, newName)

                    os.rename(oldPath, newPath)
                    Logfile("Converted file: " + fName + " -> " + newName)
                       
def Logfile(message):

    fobj = open("AutomationQ2.log" , "a")
    fobj.write(message+"\n")

    fobj.close()



