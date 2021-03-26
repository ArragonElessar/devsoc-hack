import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint


def send_otp(uemail):
    # generate 6 digit otp
    generated_otp = randint(100000, 999999)
    mail_content = f'Generated OTP: {generated_otp}'
    # email account details for OTP Sender Account
    sender_address = "ruparelsmailer@gmail.com"
    sender_password = '##Pranav22@@'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = uemail
    message['Subject'] = 'OTP For Ruparel'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, uemail, text)
    session.quit()
    print(generated_otp)
    return generated_otp

