import smtplib
from email.message import EmailMessage
import os


#-------------------------------------------------------
# Function:  Marvellous_send_mail
# Description:  Sends email using Gmail SMTP Server
#--------------------------------------------------------

def send_mail(sender, app_password, reciever, subject, body, log_file, zip_file):

    #Step1: Create Email Object
    msg = EmailMessage()

    #Step2: Set mail headers
    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    #Step3: Add mail body
    msg.set_content(body)

    # Adding Attachment Feature so that we can send files through mail.

        
    with open(log_file, "rb") as fobj:
        File_Data = fobj.read()

        Filename = os.path.basename(log_file)

        msg.add_attachment(
            File_Data,
            maintype='text',
            subtype='plain',
            filename=Filename
        )

    with open(zip_file, "rb") as fobj:
        File_Data = fobj.read()

        Filename = os.path.basename(zip_file)

        msg.add_attachment(
            File_Data,
            maintype='application',
            subtype='octet-stream',
            filename=Filename
        )
    

    #Step4: Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    #Step5: Login using gmail +  app password
    smtp.login(sender, app_password)

    #Step6: Send the mail
    smtp.send_message(msg)

    #Step7: Close connection manually
    smtp.quit()

#-----------------------------------------
# Function:  main
# Description:  Driver code
#-----------------------------------------

