#Burayı pip ile install etmen gerekebilir...
import smtplib as sm
import getpass as gp

#Genel olarak mail göndermemizi sağlayan serverlar : 
Gmail = "smtp.gmail.com"
Yahoo = "smtp.mail.yahoo.com"
Outluk = "smtp-mail.outlook.com"

#Nesneyi ayağa kaldırıyoruz
smtpObj = sm.SMTP(Gmail, 587)

#Servisi başlat
smtpObj.starttls()

#Main için şifre giriyoruz ancak görünmez şekilde :)
mailAdr = gp.getpass("Email : ")
passwd = gp.getpass("Password : ")

smtpObj.login(mailAdr, password=passwd)

from_ = mailAdr
to_ = "Hedef adres buraya"

subject = input("Subject : ")
mailTxt = input("Mail Text : ")
msg = subject + "\n" + mailTxt

smtpObj.sendmail(from_addr=from_, to_addrs=to_, msg=msg)
#Sending tamamlandı, nesneyi kapatıyoruz... 
smtpObj.quit()