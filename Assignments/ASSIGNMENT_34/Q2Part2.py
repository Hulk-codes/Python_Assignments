import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
from Q2Part1 import send_mail

def CreateLog(FolderName):
    Border = "*" * 40

    Ret = os.path.exists(FolderName)
    
    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to Create Folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory LogFiles get created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
    print("Log File gets created with name: " , FileName)

    fobj = open(FileName, "w")
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Data Shield System Report------\n")
    fobj.write("Log Created at: "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------Backup Started-------------------\n")

    fobj.write("Backup Started at : " + time.ctime())

    return fobj , FileName
    

def make_zip(Folder,log_file):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = Folder + "_" +timestamp + ".zip"
    log_file.write("Zip File Created : " + zip_name + "\n")

    # Open the ZIP file

    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(Folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, Folder)

            zobj.write(full_path, relative)

    
    zobj.close()

    return zip_name


def Calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination,log_file):
    Copied_files = []

    print("Creating the Backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs , files in os.walk(Source):                          # this loop is to handle nested folders 
        for file in files:                                         
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the files if its new
            if((not os.path.exists(dest_path)) or(Calculate_hash(src_path) != Calculate_hash(dest_path))):            
                shutil.copy2(src_path, dest_path)               #copy2 function will copy the fill with meta data
                Copied_files.append(relative)
                log_file.write("File Copied: " + relative + "\n")
                

    return Copied_files


def MarvellousDataShieldStart(sender, app_password, reciever, subject, body,Source="Data"):
    Border = "-" * 50
    BackupName = "MarvellousBackup"
    log_file, log_filename = CreateLog("LogFile_Q2")

    print("Backup process started successfully at: " , time.ctime())
    print(Border)

    Files = BackupFiles(Source, BackupName,log_file)

    zip_file = make_zip(BackupName,log_file)

    log_file.write(Border)
    log_file.write("Backup completed successfully" + "\n")
    log_file.write("Files copied : " + str(len(Files)) +"\n")
    log_file.write("Zip File gets created : " +  zip_file + "\n")
    log_file.write("Backup Ended At : " + time.ctime() + "\n")
    print(Border)

    log_file.close()

    send_mail(sender, app_password, reciever, subject, body,log_filename,zip_file)


def main():
        #Always use separate temporary/testing account
    sender_mail = "automationforpython0@gmail.com"

    # App Password generated from Google Account
    app_password = "yejs gqeq ryds dstx"

    # Your Second Email for testing
    reciever_email = "photos2of2025@gmail.com"

    subject = "Test Mail from Python Script"


    body = """Jay Ganesh,

This is a test email sent using Marvellous Python. I'm Attaching the log file created.

Regards,
Marvellous Infosystems
"""

    Border = "-" * 50
    print(Border)
    print("----------Marvellous Data Shield System------------")
    print(Border)

    if (len(sys.argv)== 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is Used to :")
            print("1: Takes auto backup at given time")
            print("2: Backup only new and updated files")
            print("3: Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("ScriptName.py TimeInterveal SourceDirectory")
            print("TimeInterval: The time in minutes for periodic Scheduling")
            print("SourceDirectory: Name of directory to backed up")
            
        else:
            print("Unable to proceed as there is no such option")
            print("Please use  --h or --u to get more details")
    
    #python3 Demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside Project logic")
        print("Time interval: ", sys.argv[1])
        print("Directory Name: ", sys.argv[2])

        #Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sender_mail,app_password,reciever_email,subject,body,sys.argv[2])

        print(Border)
        print("Data Shield System Started Successfully")
        print("Time Interval in minutes: ", sys.argv[1])
        print("Press Ctrl + C to Stop the Execution")
        print(Border)


        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use  --h or --u to get more details")


    print(Border)
    print("----------Thank You for using our script----------")
    print(Border)
if __name__ == "__main__":
    main()