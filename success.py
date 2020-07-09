import smtplib



def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("rchakravorty4@gmail.com", "rahulisarrow")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(rchakravorty4@gmail.com, rchakravorty4@gmail.com, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Build Message"
msg = "Accuracy is achieved"

send_email(subject, msg)
