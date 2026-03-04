import smtplib
from email.message import EmailMessage
import os

#-------------------------------------------------------
# Function:  Marvellous_send_mail
# Description:  Sends email using Gmail SMTP Server
#--------------------------------------------------------

def send_mail(sender, app_password, reciever, subject, body, Filename):

    #Step1: Create Email Object
    msg = EmailMessage()

    #Step2: Set mail headers
    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    #Step3: Add mail body
    msg.set_content(body)

    # Adding Attachment Feature so that we can send files through mail.

    filepath = Filename

    with open(filepath , "rb") as fobj:
        File_Data = fobj.read()

        Filename = os.path.basename(filepath)

        msg.add_attachment(
            File_Data,
            maintype='text',
            subtype='plain',
            filename=Filename  # Using the extracted filename instead of the full path
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

