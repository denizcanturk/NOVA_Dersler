"""

foreGround = 0
backGround = 0
for method in dir(list):
    if not "__" in method:
        foreGround+=1
        print(foreGround , ":", method)
    else:
        backGround+=1
        
print("Görünürde   :", foreGround , \
      "Arka Planda :", backGround)


"""

gunler = ["ptesi", "sali", "çarş"]

print(gunler[0::2])
gunler.append(1)
print(gunler)

#--------------------------------------

# 1: .append(obj)

print()
gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
print(gunler)
gunler.append("Cuma")
print(gunler)
gunler.append(1)
gunler.append(2.3)
print(gunler)

#--------------------------------------

# 2: .insert(idx, obj)

print()
gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
print(gunler)
gunler.insert(0,1) #1 sayısını listenin ilk elemanı olarak ekler
print(gunler)
gunler.insert(0,"Gun")
print(gunler)
gunler.insert(len(gunler), "Cuma")
print(gunler)

#--------------------------------------

# 3: .remove(obj)

print()
gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
print(gunler)
gunler.remove("Salı")
print(gunler)
gunler.remove("Perşembe")
print(gunler)

#--------------------------------------

# 4: .extend(<iterable>)

print()
gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
renkler = ["Mor", "Beyaz", "Kırmızı", "Mavi","Sarı"]
print(gunler)
gunler.append(renkler)
print(gunler)
gunler.extend(renkler)
print(gunler)
gunler.extend("Al")
print(gunler)

#--------------------------------------

# 5: .sort()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
renkler = ["Mor", "Beyaz", "Kırmızı", "Mavi","Sarı"]
gunler.sort()
renkler.sort(reverse=True)
print(gunler)
print(renkler)

print()

#--------------------------------------

# 6: .reverse()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
gunler.reverse()
print(gunler)

print()

#--------------------------------------

# 7: .index()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
print(gunler.index("Salı"))
print(gunler.index("Cuma"))

print()

#--------------------------------------

# 8: .clear()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
print(gunler)
gunler.clear()
print(gunler)

print()

#--------------------------------------

# 9: .copy()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
days = gunler
days.sort()
print(gunler)
days = gunler.copy()
days.reverse()
print(gunler)
print(days)

print()

#--------------------------------------

# 10: .count()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
print(gunler.count("Salı"))
print(gunler.count("Cuma"))

print()

#--------------------------------------

# 11: .pop()

print()

gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe"]
gunler.pop(1)
print(gunler)
