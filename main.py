import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

password='jjegseicvpliwpcr'
server.login('shreyawath123@gmail.com',password)

otp=''.join([str(random.randint(0,9)) for i in range(6)])
msg='Your OTP is '+str(otp)

sender='shreyawath123@gmail.com'
receiver = input("Enter your email : ")

server.sendmail(sender,receiver,msg)
server.quit()

print("OTP Sent Successfully")