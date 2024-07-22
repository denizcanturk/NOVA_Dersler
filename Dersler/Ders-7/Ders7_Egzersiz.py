isim = "Deniz CANTÜRK"
uzunluk = len(isim)

for i in range(0,uzunluk):
    print(isim[i], end=".")
print()

#-------------------------------

print(isim[0])

#-------------------------------
for i in range(0,5):
    print(i)
    
#-------------------------------

a = "4.5"
print(type(a))
print(int(float(a)))

a = 13.949999999999999
#format(a, '.2f')
print(f"{a:.4f}")
print(a)

#-------------------------------

sequence = [1,2,8,100,200,'datacamp','tutorial']

for i in sequence:
    print(i)
    
for i in range(len(sequence)):
    print(sequence[i])

#-------------------------------
    
for i in range(4,100,5):
    print(i, end=" ")
print()


#-------------------------------

isim = 45852

for i in str(isim):
    print(i)

for i in str(isim):
    print(int(i)**2)

#-------------------------------


data = [5, 6, 12, 104, 204, "Python", "Dersim"]

sayac = 0

for i in range(len(data)):
	if data[i] % 2 == 0:
		sayac +=1

print(sayac)

#-------------------------------

for I in "Python":
	print(I) 

#-------------------------------

data = [5, 6, 12, 104, 204, "Python", "Dersim"]
for i in data:
	print(i)
 
#-------------------------------

a = 2.343454
print("Benim sayım {0} olarak yazılır ama sistemde {0:.2f} olarak saklanır".format(a,a))

#-------------------------------

while True:
    parola = input("Bir parola belirleyin: ")

    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) > 8 or len(parola) < 3:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

    else:
        print("Yeni parolanız", parola)
        break
 
 #-------------------------------

        
for i in range(10):
    parola = input(f"Bir parola belirleyin [{i+1}]: ")


    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) > 8 or len(parola) < 3:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

    else:
        print("Yeni parolanız", parola)
        break

    if i > 1:
        print("Max Deneme Sayısını geçtiniz..")
        break