import smtplib

toaddrs = " masikotimo@gmail.com,mickeygerman1@gmail.com"
fromaddr = "mickeygerman1@gmail.com"
msg="This is the message"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('mickeygerman1@gmail.com','mickeygerman1')

server.sendmail(fromaddr, toaddrs, msg)
server.quit()