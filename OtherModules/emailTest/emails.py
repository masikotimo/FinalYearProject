import smtplib


content ='saidatiiiii you looked drunck in the picture'

mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('mickeygerman1@gmail.com','mickeygerman1')


mail.sendmail('mickeygerman1@gmail.com','masikotimo@gmail.com',content)

mail.close()