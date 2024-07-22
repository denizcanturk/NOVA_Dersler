foreGround = 0
backGround = 0
for method in dir(str):
    if "__" in method:
        foreGround+=1
        print(foreGround , ":", method)
    else:
        backGround+=1
        
print("Görünürde   :", foreGround , \
      "Arka Planda :", backGround)

print("""Burada yazdırılan fonksiyonlar, yansıda gördüğünüz fonksiyonlar
ile aynı değil mi? Ben de tek tek yazmadım zaten o kadar fonksiyonu...
Az önce çalıştırdığınız fonksiyonun detayları daha sonra gelecek karşınıza...""")
#------------------------------------------
        
input("Bir sornaki adım için Enter'a Basınız!")



#1: capitalize()

sampleText = """bu BeNiM DünYam"""
print(sampleText)
print(sampleText.capitalize())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------


#2: casefold()

sampleText = """bu BeNiM DünYam"""
print(sampleText.casefold())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#3: center()

sampleText = "bu BeNim dÜnyAm"
lenOfText = len(sampleText)
spaceBetween = 6 # number/2
newText = sampleText.center(lenOfText+spaceBetween)
newText2 = sampleText.center(lenOfText+spaceBetween, ".")
print(newText, "Sonraki Text")
print(newText2, "Sonraki Text")

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#4: count()

sampleText = "abc_abc_abc_abc_abc_abc_abc"
textToSearch = "ab"
print(sampleText.count(textToSearch ), "Adet eşleşme bulundu")

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#5: encode()

sampleText = "Merhaba, ü i ş ğ ç ö!"
encoded_text = sampleText.encode()
print(encoded_text)

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#6: endswith()

sampleText = "bu BeNim dÜnyAm"
print(sampleText.endswith("yAm"))
print(sampleText.endswith("yam"))
print(sampleText.endswith(("m","s","e")))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#7: expandtabs()

sampleText = "Baslik1\tBaslik2\tBaslik3"
sampleText2 = "Uzun Baslik1\tUzun Baslik2\tUzun Baslik3"
print(sampleText)
print(sampleText2)
input("Enter tuşuna basınız...")
print(sampleText.expandtabs(20))
print(sampleText2.expandtabs(20))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#8: find()

sampleText = "bu BeNim dÜnyAm"
print("Aranan metin :" , sampleText.find("dÜn"), \
      ". karakterden başlıyor")
pos = sampleText.find("dÜn")
print(pos, ". karakter : ", sampleText[pos])
print(sampleText.find("Deniz"))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#9: format()

sampleText = "{deg1} benim {deg2}"
print(sampleText.format(deg1 = "Bu", deg2 = "Dünyam"))

deg1 = "Bu"
deg2 = "dünyam"
sampleText = "{} benim {}"
print(sampleText.format(deg1, deg2))

sampleText = "{0} benim {1}"
print(sampleText.format(deg2, deg1))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#10: format_map()

infoSet = {"Adı" : "Deniz", "Yas":45}
sampleText = "Ogretmen : {Adı},{Yas}"
print(sampleText.format_map(infoSet))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#11: index()

sampleText = "Bilim adamları ay yüzeyinde muz buldular."
pos = sampleText.index("muz")
print("Konum : {}".format(pos))
print(sampleText[pos])

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#12: isalnum()

sampleText = "Bilimadamlarıayyüzeyindemuzbuldular"
sampleText2 = "Bilim adamları ay yüzeyinde muz buldular"

print(sampleText.isalnum())
print(sampleText2.isalnum())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#13: isalpha()

sampleText = "Bilim adamları ay yüzeyinde üç adet muz buldular"
sampleText2 = "Bilimadamlarıayyüzeyindeüçadetmuzbuldular"

print(sampleText.isalpha())
print(sampleText2.isalpha())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#14: isascii()

sampleText = "Made in Turkiye"
sampleText2 = "Made in Türkiye"

print(sampleText.isascii())
print(sampleText2.isascii())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#15: isdecimal()
#16: isdigit()
#17: isnumeric()

sampleText = "177a"          #Bir metinde decimal sayı varsa, hem digit hem de numeric dir
sampleText2 = "⓪①②③④⑤"  #Eger digitse, numrecdir de
sampleText3 = "壱弐参"       #Japonca ama sayı... 

print(sampleText.isdecimal())
print(sampleText2.isdigit())
print(sampleText.isnumeric())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#18: isidentifier()

var1 = "myVariable"
var2 = "_myVariable"  
var3 = "1Variable"       
var4 = "def"      

print(var1.isidentifier())
print(var2.isidentifier())
print(var3.isidentifier())
print(var4.isidentifier())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#19: islower()

sampleText = "myVariable"
sampleText2 = "_myvariable"  
sampleText2 = "myvariable"  

print(sampleText.islower())
print(sampleText2.islower())
print(sampleText2.islower())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#20: isprintable()

sampleText = "myVariable\n"
sampleText2 = "_myvariable\t"  
sampleText2 = "myvariable"  

print(sampleText.isprintable())
print(sampleText2.isprintable())
print(sampleText2.isprintable())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#21: isspace()

sampleText = "    "
sampleText2 = "   e"  

print(sampleText.isspace())
print(sampleText2.isspace())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#22: istitle()

sampleText = "merhaba Dünya"
sampleText2 = "Merhaba Dünya"  

print(sampleText.istitle())
print(sampleText2.istitle())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#23: isupper()

sampleText = "merhaba Dünya"
sampleText2 = "MERHABA DÜNYA"  

print(sampleText.istitle())
print(sampleText2.istitle())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#24: join()

sampleText = "-"

t1="Kelime 1" 
t2="Kelime 2" 
t3="Kelime 3" 

print(sampleText.join([t1,t2,t3]))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#25: ljust()
#26: rjust()

sampleText = "Merhaba Dünya"
print(sampleText.ljust(30, "_"))
print(sampleText.rjust(30, "_"))

#------------------------------------------

#27: lower()
#28: upper()

sampleText = "Merhaba Dünya"
print(sampleText.lower())
print(sampleText.upper())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#29: lstrip()
#30: rstrip()

sampleText = "Merhaba Dünya"
print(sampleText.lstrip("Merhaba"))
print(sampleText.rstrip("Dünya"))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#31: maketrans()
#32: translate()

sampleText = "Merhaba Dünya"
table = sampleText.maketrans("el", "👋")
print(table)
print(sampleText.translate(table))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#33: partition()
#34: rpartition()
#35: split()
#36: rsplit()

sampleText = "Merhaba_Dünya"
a = sampleText.partition("_")
b = sampleText.split("_")
print(type(a))
print(type(b))
print(sampleText.partition("_"))
print(sampleText.split("_"))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#37: removeprefix(str)
#38: removesuffix(str)

sampleText = "Merhaba_Dünya"
print(sampleText.removeprefix("Me"))
print(sampleText.removesuffix("ya"))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#39: replace()
#40: rfind()
#41: rindex()

sampleText = "Merhaba_Bu Dünya_Benim"
print(sampleText.replace("Bu", "O",  1))
print(sampleText.rfind("u"))
print(sampleText.rindex("e"))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#42: splitlines()

sampleText = "Merhaba Bu Dünya Benim\nve bu dünyayı python\n \
            öğrenmek üzerine kuracağım"
print(sampleText.splitlines())
print(sampleText.splitlines(True))


#------------------------------------------

#43: startswith(str)

sampleText = "Merhaba Bu Dünya Benim\n \
              ve bu dünyayı python\n \
              öğrenmek üzerine kuracağım"
print(sampleText.startswith("Mer"))


input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#44: swapcase()

sampleText = "MeRhAbA bU dÜnYa BeNiM"
print(sampleText)
print(sampleText.swapcase())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#45: title()

sampleText = "MeRhAbA bU dÜnYa BeNiM"
print(sampleText.title())

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#46: zfill()

sampleText = "MeRhAbA "
print(sampleText.zfill(30))

input("Bir sornaki adım için Enter'a Basınız!")
#------------------------------------------

#47: strip()

sampleText = "  MeRhAbA bU dÜnYa BeNiM  _"
print(sampleText.strip(".!_"))

input("Bir sornaki adım için Enter'a Basınız!")


#------------------------------------------
#               EGZERSIZ SONU
#------------------------------------------





