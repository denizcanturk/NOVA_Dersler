import random

bilgisayarSayi = random.randint(1,10)
print(bilgisayarSayi)


#------------------------------------


bilgisayarSayi = random.randint(1,10)
kullaniciSayi = int(input("Bir sayı giriniz : "))

while bilgisayarSayi != kullaniciSayi:
    kullaniciSayi = int(input("Bir sayı giriniz : "))
print("Doğru tahmin ettiniz! Tebrikler!!!")
