def fonk():
    print("Merhabalar Efendim...")


demet = ("Gerbera", "Lilyum", "Orkide")
demet2 = ("Gerbera", "Lilyum", "Orkide", "Yasemin", "Nergiz")

print(type(demet))
print(len(demet))

print(demet[0:5:1]) #0-5 e kadar & 5 Dahil değil Rahime Hanım :)
print(demet[::-1]) #Tersten yazar
print(demet[-1])


temp = list(demet) #tuple tipindeki değişkeni list e çevirir
temp.append("lale") #list fonksiyonlarını kullanarak ekleme yapar
demet = tuple(temp) #list i tuple a çevirir
print(demet) #Burda da yazdırıyoruz Rahime Hanım :)

#CONDITIONS 
if "Gerbera" in demet:
    print("Evet aradığınız çiçek var")
else:
    print("Aradığınız çiçek mevcut değil")

#LOOPS
for eleman in demet :
    print(eleman)
#--------------------------------
for i in range(len(demet)):
    print(demet[i])
#--------------------------------
i=0
while i < len(demet):
    print(demet[i])
    i+=1

#TUPLE ÇOĞALTMA
buket = demet + demet2
celenk = demet*2 + demet2 * 2
print(buket)
print(celenk)


cicek1, cicek2, cicek3 = demet
ilkDegisken, *digerDegiskenlerinAlayi = demet

print(cicek1)
print(cicek2)
print(cicek3)
print(10*"-")
print(ilkDegisken)
print(digerDegiskenlerinAlayi)
print(type(digerDegiskenlerinAlayi))


liste = ["abc", "abd"]
for i in liste:
    liste.append(i.upper())
    print(liste)