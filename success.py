import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("rchakravorty4@gmail.com", "rahulisarrow")


message_success = "Achieved your desired accuracy .Congrats."

s.sendmail("rchakravorty4@gmail.com", "rchakravorty4@gmail.com", message_success)
    
s.quit()
