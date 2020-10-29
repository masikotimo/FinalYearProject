import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "mickeygerman1@gmail.com"
password = "mickeygerman1"

# Create a secure SSL context
context = 'sdsdeewrewwe'

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)

    server.starttls() # Secure the connection

    server.login(sender_email, password)

    server.sendmail('masikotimo@gmail.com',context)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()