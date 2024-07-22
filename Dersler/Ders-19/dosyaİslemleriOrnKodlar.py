import os
from typing import IO

aDosyaYolu = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-19/metin.txt"
rDosyaYolu = "Dersler/Ders-19/metin.txt"

def dosyaDetay(file: IO[str])->None:
    print("Dosya Konum :", file.name)
    print("Dosya Mode  :", file.mode)
    print("Dosya Encde :", file.encoding)
    print("Seek Konum  :", file.tell())

def degiskenDetay(deg):
    print("Tipi    : ", type(deg))
    print("Uzunluk : ", len(deg))

if os.path.exists(aDosyaYolu):
    print("Dosya adresi DOĞRU!")

if os.path.exists(rDosyaYolu):
    print("Bu dosya adresi de DOĞRU!")

#file = open(rDosyaYolu, "r")

# icerik = file.read()
# print(icerik)
# print(file.tell())

# #-------------------

# icerik5 = file.read(5)
# print(type(icerik5))
# print(icerik5)

# #-------------------

# lines = file.readlines()
# 
# for line in lines :
#     print(line)

# #-------------------

# lines = file.readlines(5)
# for line in lines :
#     print(line)

# #-------------------

# #dosyadaki leri bi yere almadan.
# for line in file:
#     print(line)

# #-------------------
# file.close()
#Dosya ya veri ekleme:
# file = open(aDosyaYolu, "a")
# dosyaDetay(file)
# file.write("Eklediğimiz Yeni satır"+"\n") #Sonuna \n
# #-------------------
# print(file.read())
# file.close()
#-------------------

#Dosya ya veri ekleme ve okuma:
# file = open(aDosyaYolu, "a+")
# dosyaDetay(file)
# file.write("Eklediğimiz Yeni satır"+"\n") #Sonuna \n
# #-------------------
# print(file.read())
# file.close()
#-------------------

#Dosya ya veri ekleme writelines:
file = open(aDosyaYolu, "a+")
dosyaDetay(file)
data=["Birinci Eleman\n", "İkinci Eleman\n", "Üçüncü Eleman\n"]
file.writelines(data) #Sonuna \n
#-------------------
print(file.read())
file.close()
#-------------------

#Dosya ya veri YAZMA MODU:
file = open(aDosyaYolu, "w")
dosyaDetay(file)
data=["Birinci Eleman\n", "İkinci Eleman\n", "Üçüncü Eleman\n"]
file.writelines(data) #Sonuna \n
#-------------------
print(file.read())
file.close()
#-------------------

#Dosya ya veri YAZMA MODU:
file = open(aDosyaYolu, "w+")
dosyaDetay(file)
data=["Birinci Eleman\n", "İkinci Eleman\n", "Üçüncü Eleman\n"]
file.writelines(data) #Sonuna \n
#-------------------
file.seek(0)
print(file.read())
file.close()
#-------------------



