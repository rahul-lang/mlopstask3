import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("rchakravorty4@gmail.com", "rahulisarrow")


message = "Accuracy is less than 90%.Please try again"

s.sendmail("rchakravorty4@gmail.com", "rchakravorty4@gmail.com", message)
    
s.quit()
