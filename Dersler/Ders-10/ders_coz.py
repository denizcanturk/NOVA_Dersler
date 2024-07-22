# 21 MART 2024 DERS SORU ÇÖZÜMLERİ

#SORU 1 - ÇOZUM 1

metin = "Deniz"
aranacak = input("Gir : ")
metin_kucuk = metin.lower()
aranacak_kucuk = aranacak.lower()
a=metin_kucuk.count(aranacak_kucuk)
print("Metin içerisinde {} harfi, {} defa geçmektedir".format(aranacak, a))

input("Devam etmek için Enter'a basınız...")

#----------------------------------------

#SORU 1 - ÇOZUM 2



"""Metin = "Merhaba dünya"
ara = input("Giriniz : ")

metin_kucuk = metin.lower()
ara_kucuk = ara.lower()
konum=-1
sayac=0
while True:
    konum = metin_kucuk.find(ara_kucuk, konum+1)
    if konum==-1:
        break
    sayac +=1

print("Aradığınız {} defa geçmektedir".format(sayac))    
"""

#SORU 2 - ÇOZUM 1
"""
metin = "Merhaba dünya"
ara = input("Giriniz : ")

metin_kucuk = metin.lower()
ara_kucuk = ara.lower()
konum = -1

while True:
    konum = metin_kucuk.find(ara_kucuk, konum+1)
    if konum == -1:
        break
    print("Aradığın Metin {} ile {} arasında".format(konum, konum+(len(ara_kucuk))))
"""

#SORU 3 - ÇOZUM 1

metin = "Merhaba Dünya"
kucukHarf=0
buyukHarf=0
for harf in metin:
    if harf.islower():
        kucukHarf+=1
    elif harf.isupper():
        buyukHarf+=1
    else:
        None

print("Metin içinde {} adet kücük harf, {} adet büyük harf vardır" \
      .format(kucukHarf,buyukHarf))




