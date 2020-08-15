import smtplib

SUBJECT=''
BODY=''
message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY).encode('utf-8')
mail=smtplib.SMTP('smtp-mail.outlook.com',587)
mail.ehlo()
mail.starttls()
mail.ehlo()
mail.login('your_outlook_mail','your_outlook_mail_password')

mail.sendmail('your_outlook_mail','recipient_email_address',message)
mail.close()