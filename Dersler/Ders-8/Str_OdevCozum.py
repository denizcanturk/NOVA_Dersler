"""ornekMetin = " ""EEG (Elektroensefalografi) kayıtları, beyin aktivitesini ölçmek için kullanılan bir tıbbi testtir. Epilepsi tanısı için EEG kayıtları genellikle önemlidir çünkü epileptik nöbetler genellikle beyin aktivitesindeki anormal deşarjlarla ilişkilidir. EEG kayıtları, beyin aktivitesinin elektriksel aktivitesini ölçerek epileptik aktiviteyi tespit etmeye çalışır.EEG kayıtlarının incelenmesi, epileptik aktiviteyi tanımlamak için kullanılabilir. Epileptik nöbetler sırasında veya nöbetler arasında bile bazı belirtiler olabilir ve EEG bu belirtileri tespit etmeye yardımcı olabilir. Ancak, EEG kayıtları her zaman kesin bir teşhis koymak için yeterli olmayabilir ve bazen tekrarlanması veya uzman bir nörolog tarafından dikkatlice değerlendirilmesi gerekebilir.Bu nedenle, EEG kayıtlarının nöbetler sırasında ve nöbetler arasında alınması, nöroloji uzmanı tarafından değerlendirilmesi ve diğer klinik bulgularla birlikte incelenmesi önemlidir. EEG kayıtları, epilepsi tanısına katkıda bulunabilir ve uygun tedavi ve yönetim stratejilerinin belirlenmesine yardımcı olabilir."" "

#----------------------#
#  SORU 1 - ÇÖZÜM - 1  #
#----------------------#

print("Soru - 1 , Çözüm - 1 ")
aranacakKelime = input("Aranacak Kelimeyi Giriniz : ")
kucukHarfliMetin = ornekMetin.casefold()
bilgisayarSayisi = kucukHarfliMetin.count(aranacakKelime.casefold())
print(bilgisayarSayisi)
print("Metin içerisinde '{}' kelimesi, {} defa tekrar edilmiştir.".format(aranacakKelime, bilgisayarSayisi))

#----------------------#
#  SORU 1 - ÇÖZÜM - 2  #
#----------------------#

print("Soru - 1 , Çözüm - 2 ")
ilgincOrnek = ornekMetin.lower().count(aranacakKelime.casefold())
print("Metin içerisinde '{}' kelimesi, {} defa tekrar edilmiştir.".format(aranacakKelime, ilgincOrnek))

#####################################################################

#----------------------#
#  SORU 2 - ÇÖZÜM - 1  #
#----------------------#

print("Soru - 2 , Çözüm - 1 ")
aranacakKelime = input("Aranacak Kelimeyi Giriniz : ")
konum = -1

while True:
    konum = ornekMetin.casefold().find(aranacakKelime.casefold(), konum+1)
    if konum == -1:
        break
    
    print("Aranan kelime : {}.konumda bulundu".format(konum))
    
#####################################################################

#----------------------#
#  SORU 2 - ÇÖZÜM - 2  #
#----------------------#

print("Soru - 2 , Çözüm - 2")
aranacakKelime = input("Aranacak Kelimeyi Giriniz : ")
duzeltilmisAranakcakKelime = aranacakKelime.casefold()
konum = -1
bulunanSayisi = ornekMetin.casefold().count(duzeltilmisAranakcakKelime)

for bulunacak in range(bulunanSayisi):
    konum = ornekMetin.casefold().find(duzeltilmisAranakcakKelime,konum+1)
    print("{}.-Aranan kelime : {}.konumda bulundu".format(bulunacak, konum))
    
#####################################################################

#----------------------#
#  SORU 2 - ÇÖZÜM - 3  #
#----------------------#

print("Soru - 2 , Çözüm - 3 ")
aranacakKelime = input("Aranacak Kelimeyi Giriniz : ")
duzeltilmisAranakcakKelime = aranacakKelime.casefold()
konum = 0
bulunanSayisi = ornekMetin.count(duzeltilmisAranakcakKelime)

while konum != -1:
    konum = ornekMetin.casefold().find(duzeltilmisAranakcakKelime, konum+1)
    if konum == -1:
        break
    print("Aranan kelime : {}.konumda bulundu".format(konum))
    
#####################################################################

#----------------------#
#  SORU 3 - ÇÖZÜM - 1  #
#----------------------#

print("Soru - 3 , Çözüm - 1 ")
aranacakKelime = input("Aranacak Kelimeyi Giriniz : ")
duzeltilmisAranakcakKelime = aranacakKelime.casefold()
konum = 0
bulunanSayisi = ornekMetin.count(duzeltilmisAranakcakKelime)

while konum != -1:
    konum = ornekMetin.casefold().find(duzeltilmisAranakcakKelime, konum+1)
    if konum == -1:
        break
    print("Aranan kelime : {}-{}.konumda bulundu".format(konum, konum+len(aranacakKelime)))
    
    
"""

isim = "göktengri"

#den = input("gir")
print("Metin içinde bulunan konumu {}".format("Bu da böyle bi örnek \
      olsun".casefold().find(input("gir :").casefold())))