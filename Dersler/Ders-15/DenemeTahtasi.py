#Alistirma-2
"""metin = "python123program456"

harfSayisi = 0
numaraSayisi = 0

for harf in metin:
    if harf.isalpha():
        harfSayisi+=1
    
    if harf.isdigit():
        numaraSayisi+=1
        
print("Metin içinde {} adet harf ve {} adet sayi bulunmaktadır".format(harfSayisi, numaraSayisi))"""

#----------------------------------
#Alistirma-3
"""
metin = "python123program456"

aranacakHarf = "p"

adedi = metin.count(aranacakHarf)

print(metin.count(aranacakHarf))
"""
#----------------------------------
#Alistirma-4
"""
metin = "ey edip adanada pide ye"

if metin == metin[::-1]:
    print("Palindromdur")
else:
    print("Değildi")
"""
#----------------------------------
#Alistirma-8

liste1 = [1,5,2,6,9]
liste2 = [8,4,7,2,6]

liste3 = liste1.copy()
liste3.extend(liste2)
print(liste3)

#2
essizListe = liste1.copy()

for eleman in liste2:
    if eleman not in essizListe:
        essizListe.append(eleman)

print(essizListe)

benzersizListe = []

for item in liste1:
    if item not in liste2:
        benzersizListe.append(item)

for item in liste2:
    if item not in liste1:
        benzersizListe.append(item)

print(benzersizListe)

print(max(liste1))
print(min(liste1))


#----------------------------------
#Alistirma-9
"""toplam = 0
sayac = 0
ort = 0
while True:
    cevap = input("Giriş yapınız")

    if cevap.isdigit():
        toplam += int(cevap)
        sayac +=1
    elif cevap.lower()=="tamam":
        ort = toplam / sayac
        print("Girilen {} adet sayaının toplamı {}, ortalaması {}".format(sayac,toplam,ort))
        break

"""
#----------------------------------
#Alistirma-13
while True:
        cevap = int(input("Bir sayı giriniz: "))

        if cevap >= 1 and cevap <= 100:

            if cevap % 3 == 0 and cevap % 5 == 0:
                print("Fizz Buzz")
            elif cevap % 3 == 0 :
                print("Fizz")
            elif cevap % 5 == 0:
                print("Buzz")
            else:
                print("Hiç birine uymadı")
        else:
            if cevap == 0:
                print("Çıkıyoruz...")
                break
            print("Girdiğiniz sayı limit dışı")