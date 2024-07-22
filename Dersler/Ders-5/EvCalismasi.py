"""
Kullanıcı tarafından girilecek olan Fahrenheit (F) cinsinden sıcaklık
birimini, Santigrat (C) birimine çevirip ekrana yazdıran programı
yazınız.
"""

sicaklikF = int(input("Sıcaklık Değerini F cinsinden giriniz : "))
C = (sicaklikF - 32) * 5/9
print("Girdiğiniz değerin C karşılığı : ", C)

#---------------------------------------------------------------
"""
Kullanıcı tarafından girilecek olan Santigrat (C) cinsinden sıcaklık
birimini, Fahrenheit (F) birimine çevirip ekrana yazdıran programı
yazınız.
"""
sicaklikC = int(input("Sıcaklık Değerini C cinsinden giriniz : "))
F = (sicaklikC * 9/5) + 32
print("Girdiğiniz değerin C karşılığı : ", F)

#---------------------------------------------------------------
"""
Kullanıcı tarafından taban kenar uzunluk ve yükseklik değerleri
girilecek olan dik üçgenin alan hesabını yapan ve ekrana yazdıran
programı yazınız.
"""

taban = float(input("Taban uzunluğu : "))
yukseklik = float(intput("Yukseklik : "))

alan = taban * yukseklik / 2

print("Ucgenin Alanı : " + str(alan))

#---------------------------------------------------------------
"""
Kullanıcı tarafından girilecek olan vize ve final notlarına göre
öğrencinin dersten geçip geçmediğini hesaplayan ve ekrana “GEÇTİ”,
“GEÇMEDİ” şeklinde yazdıran programı yazınız.
GEÇME NOTU = VİZE %30 + FİNAL %60
GEÇME KRİTERİ = 70
"""

vize = float(input("Vize notunuzu giriniz : "))
final = float(input("Final notunuzu giriniz : "))
GECME_KRITERI = 70
gecmeNotu = vize * 0.3 + final * 0.6

if gecmeNotu >= GECME_KRITERI :
	print("Tebrikler dersten geçtiniz...")
else:
	print("Dersten geçemediniz... Biz üzgün değiliz ama siz olmalısınız...")
	
#---------------------------------------------------------------
"""
Fabrikada sabit maaşla çalışan işçiler aşağıda belirtilen koşullara
göre ek maaş almaktadır.
- Çocuk sayısı 1 ise maaşının %5’i,
- Çocuk sayısı 2 ise %10’u
- Çocuk sayısı 3 ve daha fazla ise %15’i kadar ilave aile yardımı
almaktadır.
Kullanıcı tarafından girilecek olan işçi maaş ve çocuk sayısı
bilgilerine göre, işçinin ay sonunda alması gereken maaşı hesaplayıp
ekrana yazdıran programı yazınız.
"""

maas = float(input("Maas miktarınızı giriniz : "))
cocukSayisi = int(input("Kac Cocugunuz var : "))

if cocukSayisi == 1 :
	maas *= 1.05
elif cocukSayisi == 2 : 
	maas *= 1.1
else:
	maas *=1.15
	
print("Maasınız son miktarı : " + str(maas))

#---------------------------------------------------------------
"""
1 den, Kullanıcı tarafından girilecek olan sayıya kadar olan
sayıların toplamını ekrana yazdıran programı yazınız.
"""
sayi = int(input("Rastgele bir sayı giriniz : "))
sayac = 1
toplam = 0
while sayac < sayi :
	toplam += sayac
	sayac+=1
	
print("Sayıların Toplamı : ", toplam)


#---------------------------------------------------------------
"""
Kullanıcı tarafından girilecek olan ad değişkenini, 10 kere ekrana
yazdıran ekrana yazdıran programı yazınız.
"""

isim = input("Bir isim giriniz : "))

sayac = 0

while sayac < 10:
	print(isim)
	sayac+=1

#---------------------------------------------------------------
"""
1 den, Kullanıcı tarafından girilecek olan sayıya kadar olan sayı
aralığında; tek sayıların Toplamı ve Çarpımları ile, çift Sayıların
karelerinin toplamlarını ekrana yazdıran ekrana yazdıran programı
yazınız.
"""
sayi = int(input("Bir sayi giriniz : "))
tekToplam = 0
tekCarpim = 1
ciftKareToplam = 0

sayac = 1
while sayac  <= sayi :
	if sayac % 2 == 1:
		tekToplam += sayac
		tekCarpim *= sayac
	else:
		ciftKare += sayac**2

print("Tek Sayıların Toplamı :" , tekToplam, "\n",
	  "Tek Sayıların Carpımı :" , tekCarpim, "\n",
	  "Cift Kare Carpımleri  :" , ciftKareToplam, sep="") 

print("Tek Sayıların Toplamı :" + str(tekToplam) + "\n" +
	  "Tek Sayıların Carpımı :" + str(tekCarpim) + "\n" +
	  "Cift Kare Carpımleri  :" + str(ciftKareToplam))


#---------------------------------------------------------------
"""
- Aşağıdaki koddaki mantık hatasını bulunuz…
"""

sayac = 1
sayi = int(input("Sayı Giriniz : "))
toplam = 0
while sayac <= sayi:
	sayac +=1
	toplam += sayac
	
print("Toplam Değeri ", toplam)
