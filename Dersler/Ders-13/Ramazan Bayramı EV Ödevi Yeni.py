
#ALISTIRMA - 1
#Kullanıcı tarafından bir metin/kelime girilir. Girilen ifade ekrana tersten yazdırılır.
#------------------------------------------------

metinGir = input("Lütfen bir metin giriniz :")

print(metinGir[::-1])

print("Metnin tersten yazılışı :",metinGir[::-1])

for i in range(len(metinGir)-1,-1,-1):
    print(metinGir[i],end="")

#ALISTIRMA - 2
#Kullanıcı tarafından metin ve sayılardan olusan bir ifade girilir. Girilen ifade içinde karakterlerin ve sayıların adetleri ekrana yazdırılır.
#------------------------------------------------

metinGir = input("Lütfen bir metin giriniz :")

uzunluk = (len(metinGir))
print(uzunluk)

#ALISTIRMA - 3
#Kullanıcı bir metin/kelime ve bu metin/kelime içinde aranacak bir harf girer. Aranan harfin metin içinde kaç defa geçtigi ekrana yazdırılır.
#------------------------------------------------

metin = "Aranan harfin metin içinde kaç defa geçtigini ekrana yazdır"
metinGir = input("Lütfen aranacak harf/kelime giriniz :")

metin_kucuk = metin.lower()
aranacak_kucuk = metinGir.lower()
a = metin_kucuk.count(aranacak_kucuk)
print("Metin içerisinde {} harfi, {} defa geçmektedir".format(metinGir, a))

#ALISTIRMA - 4
#Kullanıcı tarafından girilecek olan bir kelimenin “palindrom” olup olmadıgını kontrol edip sonucu ekrana yazdırın.
#------------------------------------------------
metinGir = input("Lütfen bir kelime giriniz :")
metin_kucuk = metinGir.lower()
if metin_kucuk.lower() == "palindrom":
    print("Aranan kelime",True)
else:
    print("Aranan kelime",False)

#ALISTIRMA - 5
#Kullanıcı tarafından girilen bir metinin kaç kelimeden olustugunu bulup, ekrana yazdırınız.
#------------------------------------------------


metin = input("Bir metin giriniz :")
satırlar = metin.splitlines()
print(satırlar)
b = 0
for i in satırlar:
    kelimeler = i.split()
    for a in kelimeler:
        b = b + 1
print(f"Girilen metinde {b} adet kelime bulunmaktadır")

#ALISTIRMA - 6
#Kullanıcının girdigi matematiksel ifadeye göre islemi yapıp ekrana yazdırınız.
# NOT : Bir matematiksel islem sadece <sayı><islem><sayi> seklinde olabilir. Orn: 15+14 gibi.

sayi1 = int(input("1. Sayıyı giriniz : "))
sayi2 = int(input("1. Sayıyı giriniz : "))
toplama = sayi1+sayi2
cıkarma = sayi1-sayi2
carpma = sayi1*sayi2
bolme = sayi1/sayi2
mod = sayi1 % sayi2


print(sayi1,"+",sayi2,"Toplamı = ",toplama)
print(sayi1,"-",sayi2,"Kalanı = ",cıkarma)
print(sayi1,"*",sayi2,"carpımı = ",carpma)
print(sayi1,"/",sayi2,"bolum = ",bolme)
print(sayi1,"%",sayi2,"mod = ",mod)



#ALISTIRMA - 7
#Rastgele sayılar ile doldurulmus bir tam sayı listesinin, en küçük ve en büyük elemalarını,
# negatif sayıların ve pozitif sayıların adedini ekrana yazdırınız.
#------------------------------------------------

liste = [1,10,25,30,88,105,99,-1,-25,-65,-70,-87,-90]
ara = (len(liste))
print(f"Dizi içinde {ara} eleman bulunmaktadır")
print ("Dizinin En Küçük Elemanı: ",min(liste))
print ("Dizinin En Büyük Elemanı: ",max(liste))
for sayi in liste:
    if sayi > 0:
        print(f"{sayi} Pozitif")
    elif sayi < 0:
        print(sayi, "Negatif")
    else:
        print(sayi, "Sıfır")

#ALISTIRMA - 8
#Rastgele tam sayılardan olusan iki liste nin elemanları ile ilgili olarak :
#- Her iki listenin elemanlarını içeren üçüncü bir liste olusturun
#- Her iki listenin elemanlarını içeren ancak aynı degerlerin tekrar etmedigi bir liste olusturun
#- Her iki listenin sadece benzersiz (digerinde bulunmayan) degerlerinin bulundugu bir liste olusturun
#- Her iki listenin en büyük ve en küçük degerlerini iceren bir liste olusturun.
#------------------------------------------------

gunler = ["pazar","ptesi","sali","çarsamba","persembe","Mavi","5","6","7"]
renkler = ["Mor","Beyaz","Kırmızı","Mavi","Sari","çarsamba","sali","5","6"]
print("-"*45)
print("Günler litesi içindeki elemanlar :",gunler)
print("-"*45)
print("Renkler litesi içindeki elemanlar :",renkler)
print("-"*45)
gunler.extend(renkler)
print("Ortak liste elemanları :",gunler)
print("-"*45)
print ("Dizinin En Küçük Elemanı: ",min(gunler))
print("-"*45)
print ("Dizinin En Büyük Elemanı: ",max(gunler))
print("-"*45)
for i in gunler:
    ortak = [j for j in i if j in renkler]
    if str(len(ortak)) == str(len(i)):
        print("ortak elemanlar",str(i))
print("-"*45)

#ALISTIRMA - 9
#Klavyeden “Tamam” girilinceye kadar girilecek olan tam sayıların toplamlarını ve aritmetik ortalamalarını ekrana yazdırınız.
harf = "Tamam"
sayac = 0
toplam = 0


while True:
    sayi = input("{0} ıncı Sayiyi giriniz :".format(sayac + 1)) # Burdaki {} ve sayac değişkeni girilen değerlerin sıralaması içindir.
                                                                #giriş sayısını 1 arttırır. 1 2 3 . . .
    if sayi.isdigit(): #isdigit() Karakter dizisinin sadece sayılardan oluşup oluşmadığını sorgular.
                        #True dönderebilmesi için, sayı değeri karakter dizisinin bir tam sayıdan oluşması gerekiyor.
        toplam += int(sayi)
        sayac += 1
    elif sayi.lower() == harf.lower():
        break
print("sayıların toplamı = ",toplam)
print("Sayıların ortalaması = ",toplam/sayac)

##############    İkinci  Yöntem     ##############

liste = []
toplam = 0
sayac = 0
harf = "Tamam"
while True:
    sayı = input("{} inci sayıyı giriniz :".format(sayac+1))

    #if sayı not in liste:
    if sayı.isdigit():
        liste += [int(sayı)]
        sayac += 1
        print(liste)
    elif sayı.lower() == harf.lower():
        for i in liste:
            toplam += i
        print(f"Listenin içindeki sayıların toplamı : {toplam} ")
        print("Liste içindeki sayıların ortalaması ",toplam/sayac)
        break

#ALISTIRMA - 10
#Kullanıcı tarafından girilecek metre cinsinde degerin :
#- mil,
#- inç,
#- yard
#- feet birimlerinden olan miktarlarını ekrana yazdırır.

sayi = int(input("Lütfen bir sayı giriniz :"))
mil = sayi / 1609,344
inc = sayi * 0.0254
yard = sayi * 1.0936133
feet = sayi * 3.28

print("Bir Metre :",mil," mil eder")
print("Bir Metre :",inc," inc eder")
print("Bir Metre :",yard," yard eder")
print("Bir Metre :",feet," feet eder")

#ALISTIRMA - 11
#Klavyeden girilen tam sayının haftanın hangi gününe denk geldigini ekrana yazdırın. Orn.: Gırıs : 2, Cıkıs : Salı gibi
#------------------------------------------------
while True:

    sayi = int(input("Lütfen Bir Sayı Giriniz :"))
    if sayi not in range(1,8):
        print("Haftada kaç gün var?")
        break
    
    if sayi == 1:
        print("Pazartesi")
    elif sayi == 2:
        print("Salı")
    elif sayi == 3:
        print("Çarşamba")
    elif sayi == 4:
        print("Perşembe")
    elif sayi == 5:
        print("Cuma")
    elif sayi == 6:
        print("Cumartesi")
    elif sayi == 7:
        print("Pazar")
    else:
        print("Hafta günlerine eş gelen bir sayı girmediniz")
        break

#ALISTIRMA – 12
#Kullanıcı tarafından girilen ay numarasının hangi aya karsılık geldigini ekrana yazdırın.
#------------------------------------------------
aylar =["OCAK","ŞUBAT","MART", "NİSAN","MAYIS", "HAZİRAN","TEMMUZ","AGUSTOS","EYLÜL","EKİM","KASIM","ARALIK"]
while True:
    sayi = int(input("Lütfen Bir Sayı Giriniz :"))
    if sayi not in range(1,13):
        print("Bizim toplam 12 ayımız var... Bu nerden çıktı")
        break

    if sayi == 1:
        print("Ocak")
    elif sayi == 2:
        print("Şubat")
    elif sayi == 3:
        print("Mart")
    elif sayi == 4:
        print("Nisan")
    elif sayi == 5:
        print("Mayıs")
    elif sayi == 6:
        print("Haziran")
    elif sayi == 7:
        print("Temmuz")
    elif sayi == 8:
        print("Agustos")
    elif sayi == 9:
        print("Eylül")
    elif sayi == 10:
        print("Ekim")
    elif sayi == 11:
        print("Kasım")
    elif sayi == 12:
        print("Aralık")
    else:
        print("Ay günlerine eş gelen bir sayı girmediniz")
        break

    #İKİNCİ ÇÖZÜM ÖNERİSİ
    print(aylar[sayi-1])

#ALISTIRMA - 13
#Kullanıcı 1-100 arasında bir sayı girisi yapar.
#- Eger sayi 3’ün katıysa ekrana : Fizz
#- Eger sayi 5’in katıysa ekrana : Buzz
#- Eger sayi hem 3 ün hem de 5 in katıysa : Fizz Buzz
#- Eger girilen sayi istenen aralik disinda ise hata mesajı ekrana yazdırılmalıdır.
#------------------------------------------------
while True:
    sayi = int(input("Bir ile yüz arasında bir sayı giriniz :"))
    if sayi < 1 and sayi >100:
        print("Girilen sayı 1 ile 100 sayı aralığının dışındadır")
        break
    elif sayi % 3 and sayi % 5 == 0:
        print("Fizz Buzz")
    elif sayi % 5 == 0:
        print("Buzz")
    elif sayi % 3 == 0:
        print("Fizz")


#ALISTIRMA - 14
#Kullanıcı bir ifadenin kaç kere yazdırılacagını ve ifadeyi arada bosluk bırakmadan gırıs yapar.
# Programcının görevi, sayıdan farklı olarak girilen ifadeyi baslangıcta belirtildigi kadar ekrana yazdırır.
#Orn : 7x
#Cıktı :
#x
#x
#x
#x
#x
#x
#x

txtToPrint = input("Girbakalım bişeyler : ")
letterStartIndex = 0
for i in txtToPrint:
    if not i.isdigit():
        letterStartIndex = txtToPrint.index(i)
        if (letterStartIndex == 0):
            print("Hoppala paşam, malkara keşan")
            print("İfaden sayı ile başlamıyor senin.. Hayırdır...")
        break

numberPart = txtToPrint[:letterStartIndex:]
txtPart = txtToPrint[letterStartIndex::]

for i in range(int(numberPart)):
    print(txtPart, ":) İyi bayramlar")
















