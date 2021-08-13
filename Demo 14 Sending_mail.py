"""

Step1:Import Package SMTPlib
Step2: OPen Connection (Gmail/Hotmail)(username, Password
Step3: open connection in secure way (SSL/TLS)transport layer security
Step4: Send mail(User name , Sender Add, Message)
Step5: Close connection


"""

import smtplib
con = smtplib.SMTP('smtp.gmail.com',587)
con.login("sender Add","password")
con.starttls()
message = " I hope you are learning new tips and Tricks in python ..."
con.sendmail("SenderAdd ","Reciever Add",msg = message)
print("mail Sent sucessfully ......")
con.close()