# liste = []
# toplam = 0

# while True:
#     sayı = int(input("Bir sayı giriniz"))

#     if sayı not in liste:
#         liste += [sayı]
#         print(liste)
#     else:
#         for sayi in liste:
#             toplam += sayi
#         print(f"Listenin içinde {liste} sayıları bulunmakta ve sayıların toplamı : {toplam} ")
#         break


# """sevgili hocam bu da başka bir yötem ancak int sayı içine str bir kelime kullanıldığında,
# malesef işin rengi değişiyor.
# burde if not in liste ile (içinde benzer yoksa yaz ,ama içinde aynısı varsa else geç dedim yinede istediğini
# yapamadım lütfen 10. soruya geçmeme yardımcı olun.veya çözümlerin tamamını paylaşında bir miktar bayram boşluğunda
#                            üzerlerinde egzersiz yapabileyim."""

#------------------------------------------------

#ALISTIRMA - 1 

metin = input("Bir metin giriniz : ")

tersMetin = metin[::-1]

print(metin[::-1])
print(tersMetin)

#------------------------------------------------

# #ALISTIRMA - 2 

text = input("Rastgele bir metin giriniz : ")
digitNum = 0
letterNum = 0

for harf in text:
    if harf.isdigit():
        digitNum+=1
    if harf.isalpha():
        letterNum+=1

print("Metin içerisinde {} adet harf ve {} adet sayı bulunmaktadır".format(letterNum, digitNum))

#------------------------------------------------

#ALISTIRMA - 3

mainText = input("Bir uzun metin girin : ").lower()
aranacakHarf = input("Aranacak Harfi girin :").lower()
print("{} harfi, metin içinde {} defa geçmektedir".format(aranacakHarf, mainText.count(aranacakHarf)))

#------------------------------------------------

#ALISTIRMA - 4 

word = input("Bir kelime giriniz")

if word == word[::-1]:
    print("Kelimeniz bir palidromdur")
else:
    print("Sadece bir kelime işte...")    

#------------------------------------------------

#ALISTIRMA - 5 

mainText = input("en az 10 kelimelik bir metin girin : ")
wordList = mainText.split(" ")

print("Metniniz {} kelimeden oluşmaktadır.".format(len(wordList)))
#------------------------------------------------

# #ALISTIRMA - 6 

operatorler = ["+","-","*","/"]

islem = input("Matematiksel bir islem girin (Örn:10*12): ")

for n in islem:
  if n in operatorler:
    parcalar= islem.split(n)
    if n == "+":
      sonuc = int(parcalar[0]) + int(parcalar[1])
    if n == "-":
      sonuc = int(parcalar[0]) - int(parcalar[1])
    if n == "*":
      sonuc = int(parcalar[0]) * int(parcalar[1])
    if n == "/":
      sonuc = int(parcalar[0]) / int(parcalar[1])

print("{} = {}".format(islem, sonuc))

#------------------------------------------------

#ALISTIRMA - 7 

tamSayiList = [12,25,15,36,22,54,69,85,665,-51,-8,-6,54,-53]
sifirdanKucuk = 0

enBuyuk = max(tamSayiList)
enKucuk = min(tamSayiList)

for n in tamSayiList:
  if n < 0:
    sifirdanKucuk +=1
    
print("Elinizdeki listenin en küçük değeri {}, \
en büyük değeri ise {} dir. \
Sayi listenizde toplam {} adet negatif sayı bulunmaktadır.".format(enKucuk, enBuyuk, sifirdanKucuk))

#------------------------------------------------

#ALISTIRMA - 8

tamSayiList = [12,25,15,36,22,54,69,85,665,-51,-8,-6,54,-53]
tamSayiList2 = [10,20,14,3,85,57,68,83,645,-81,-7,-3,74,-23]

#İki Listenin bir birine eklendiği durum
extendedList = tamSayiList.extend(tamSayiList2)    

# Aynı elemanların tekrar etmediği liste
uniqeList= tamSayiList.copy()
for item in tamSayiList2:
    if item not in uniqeList:
        uniqeList.append(item)
        
#İki listenin min ve max elemanlarından oluşan yeni liste
minMaxList = []
minMaxList.append(min(tamSayiList),max(tamSayiList), min(tamSayiList2), max(tamSayiList2))


#Her iki liste de olmayan elemanları içeren liste
uniqeList2 = []
for item in tamSayiList:
    if item not in tamSayiList2:
        uniqeList2.append(item)

for item in tamSayiList2:
    if item not in tamSayiList:
        uniqeList2.append(item)

#------------------------------------------------
