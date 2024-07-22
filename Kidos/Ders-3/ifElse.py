password = input("Şifrenizi Giriniz : ")
if password == "123":
    print("Şifre Doğru")

    #Burayı sonradan ekle... 
else:
    print("Yanlış şifre girildi")


#----------------------------------

kullanici = input("Kullanıcı Adinizi Girin : ")
sifre = input("Sifrenizi Girin : ")

if kullanici == "python" and sifre == "123":
    print("Dogrulama başarılı...")

else:
    print("Hatalı Giriş yapıldı...")


#----------------------------------

#BİLGİ YARIŞMASI

#Birinci Soru : 
puan = 0
cevap1 = input("Türkiye nin Başkenti Neresidir?")

if cevap1 == "Ankara" or cevap1=="ankara":
    puan = puan +1

cevap2 = input("Hangi dili ögreniyorsunuz?")
if cevap2=="python" or "Python":
    puan = puan + 1

cevap3=input("Hangi kurumda eğitim alıyorsunuz?")

if cevap3=="Nova" or cevap3=="NOVA" or cevap3 =="nova":
    puan = puan+1

print(f"Tebrikler! Toplam Puanınız {puan}")

#----------------------------------

yas = int(input("Yasinizi Giriniz : "))

if yas >0 and yas<=10 :
    print("Cocuksunuz...")
elif yas > 10 and yas <=16:
    print("Siz bir gencsiniz")
elif yas > 16 and yas < 50:
    print("Siz bir yetiskinsiniz")
elif yas > 50 and yas <=120:
    print("Siz yaslı bir insansınız...")
else:
    print("Yaş doğru mu girildi?")
    

