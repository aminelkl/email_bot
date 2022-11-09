import smtplib

toadress = 'adressReceiver'
fromadress = 'adressSender'
message = 'theMessage'

with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('your_email', 'your_password')
  for i in range(50) :
    smtpserver.sendmail(fromadress, toadress, message)
    print (i)
