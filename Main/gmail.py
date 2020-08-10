import smtplib

SUBJECT=''
BODY=''
message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY).encode('utf-8')
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.ehlo()
mail.login('your_gmail','gmail_password')

mail.sendmail('your_gmail','recipient_email_address',message)
mail.close()
