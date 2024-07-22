
#------------------------------------------------

#ALISTIRMA - 1 

sayi = int(input("Bir sayı giriniz: "))

if sayi % 2 == 0:
    sonuc = 'çift'
else:
    sonuc = 'tek'
    
print("Girdiğiniz sayı ", sonuc, " bir sayıdır.")

#------------------------------------------------

#ALISTIRMA - 2 

sayi = float(input("Bir sayı girin: "))
 
if sayi > 0:
    print("Girilen sayı pozitiftir.")
else:
    print("Girilen sayı pozitif değildir.")

#------------------------------------------------

#ALISTIRMA - 3

sayi = float(input("Bir sayı giriniz: "))
 
if sayi < 0:
    mutlak_deger = -sayi
else:
    mutlak_deger = sayi
 
print("Sayının mutlak değeri: ", mutlak_deger)

#------------------------------------------------

#ALISTIRMA - 4 

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
 
if sayi1 < sayi2:
    kucuk = sayi1
else:
    kucuk = sayi2
 
print("Küçük olan sayı: ", kucuk)

#------------------------------------------------

#ALISTIRMA - 5 

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
sayi3 = float(input("Üçüncü sayıyı giriniz: "))
 
if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   enBuyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   enBuyuk = sayi2
else:
   enBuyuk = sayi3
 
print("En büyük sayı: ", enBuyuk)

#------------------------------------------------

#ALISTIRMA - 6 

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
 
ortalama = (sayi1 + sayi2) / 2
 
print("Ortalamanız: ", ortalama)

#------------------------------------------------

#ALISTIRMA - 7 

for i in range(10):
    print(i)

#------------------------------------------------

#ALISTIRMA - 8

for i in range(100):
    if i % 5 == 0:
        print(i)

#------------------------------------------------

#ALISTIRMA - 9

print("*" * 10)

#------------------------------------------------

#ALISTIRMA - 10

print("Daha çok çalışmalıyım\n" * 10)

#------------------------------------------------

#ALISTIRMA - 11

print("Daha","çok","çalışmalıyım", sep="-", end=" :(")

#------------------------------------------------

#ALISTIRMA - 12

i = 1
yukari = True
sayac = 0
while True:
    sayac+=1
    if yukari:
        i+=1
        if i > 10:
            yukari = False
    else:
        i-=1
        if i < 0:
            yukari = True
    print(i*"* ")
    
    if sayac > 5:
        break

#------------------------------------------------

#ALISTIRMA - 13

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].upper(), sep="", end="")
print()

#------------------------------------------------

#ALISTIRMA - 14

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].upper(), sep=" ", end="")
print()

#------------------------------------------------

#ALISTIRMA - 15

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].upper(), sep="", end=" ")
print()

#------------------------------------------------

#ALISTIRMA - 16

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].upper(), sep="-", end=" ")
print()

#------------------------------------------------

#ALISTIRMA - 17

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].upper(), sep="-", end="-")
print()

#------------------------------------------------

#ALISTIRMA - 18

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].upper(), sep=" ", end="-")
print()

#------------------------------------------------

#ALISTIRMA - 19

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].swapcase(), end=" ")
print()

#------------------------------------------------

#ALISTIRMA - 20

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)):
    print(metin[i].isascii(), end=" ")
print()

#------------------------------------------------

#ALISTIRMA - 21

metin = "Bu bilgisayarın patronu benim..."

for i in range(len(metin)//4):
    print(metin[i].isascii(), end=" ")
print()