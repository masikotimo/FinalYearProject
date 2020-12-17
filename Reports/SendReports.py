import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os




filename = "Reports/Report.pdf"  # In same directory as script

def sendEmail(email):
    subject = "System Reports "
    body = "Hello administrator, you  are receiving this email because you're an administrator of the RUAA system"
    sender_email = "mickeygerman1@gmail.com"
    receiver_email = email['Email']
    password = "mickeygerman1"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    with open(filename, "rb") as attachment:
        
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='Report.pdf')

    message.attach(part)
    text = message.as_string()

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465 )
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def sendPassword(email,password):
    subject = "RUAA account password "
    body = "you're welcome to RUAA system , your Account password is %s"%(password)
    sender_email = "mickeygerman1@gmail.com"
    receiver_email = email
    password = "mickeygerman1"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465 )
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    server.quit()