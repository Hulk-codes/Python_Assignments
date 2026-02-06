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

def DirectoryFileWithExtension(DirectoryName, Extension):

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
         for fName in FileName:
              if fName.endswith(Extension):
                   Logfile("File Found: " +fName)

def Logfile(message):

    fobj = open("AutomationQ1.log" , "a")
    fobj.write(message+"\n")

    fobj.close()



