
print(help(list))
"""onPlan = 0
arkaPlan = 0

for method in dir(tuple):
    if not "__" in method:
        onPlan+=1
        print(onPlan , ":", method)
    else:
        arkaPlan+=1
        
print("Görünürde   :", onPlan , \
      "Arka Planda :", arkaPlan)"""

"""

#print([mey for mey in dir(tuple) if not "__" in mey])

demet = ("Ayçiçeği", "Açelya", "Gerbera", "Karanfil", "Lilyum", "Petunya", "Şebboy", "Zambak")
demet2 = ("Begonya","Gül","Kardelen","Lavanta", "Sümbül")


#######################################
#             ALIŞTIRMA - 1           #
#######################################

# 1) demet değişkenin ilk elemanını yazdırınız -> demet[0]

# 2) demet değişkenin eleman sayısını yazdırınız -> len(demet)

# 3) demet değişkeninin 2.,3.,4. ve 5. inci elemanlarını yazdırınız demet[2:6:1]

# 4) demet değişkenini tersten yazdırınız. demet[::-1]

# 5) demet ve demet2 değişkenini `demet` değişkeni altında birleştiriniz. demet += demet2

# 6) demet değişkenin elemanlarını while döngüsü ile tersten yazdırınız

i = len(demet)-1
while i > -1:
     print(demet[i])
     i= i-1

# 7) `demet` değişkeninin birinci elemanını siliniz
temp = list(demet)
temp.pop(0)
demet = tuple(temp)
print(demet)" ""

# 8) `demet` değişkeninin birinci elemanı olarak "Kaktüs" ü ekleyiniz
temp = list(demet)
temp.insert(0,"Kaktüs")
demet = tuple(temp)
print(demet)"""