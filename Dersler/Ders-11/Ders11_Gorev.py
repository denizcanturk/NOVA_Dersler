############################################
#           DERSTE YAPTIKLARIMIZ           #
############################################

isim, soyisim, yas = "Deniz", "CANTÜRK", 45

kullanıcı = isim,soyisim, yas

print("Kullanıcı Bilgileri :" , kullanıcı)
print(type(kullanıcı))



gunler = ["ptesi","salı","çarş", "perş", "cuma", "ctesi","pazar"]
print(type(gunler))
print(len(gunler))
print(gunler)

for gun in gunler:
    print(gun)
    
    
for i in range(2):
    print(gunler[i])

print(gunler[::-1])
print(gunler[-1])

print(gunler)


############################################
#               GÖREVLERİNİZ               #
############################################

meyveler = ["elma", "armut", "muz", "çilek", "portakal"]

#---------------------------------------
#    TİKAT TİKAT HATTA Bİ DAHA TİKAT

#NOT : Aşağıda yapılan her işlem sonucunda meyveler değişkenini print fonksiyonu ile yazdırınız.
#---------------------------------------
# meyveler list veri yapısı {

#   1) 3 üncü elemanı print fonksiyonu kullanarak yazdırınız. 

#   2) ...içinde yer alan "armut" meyvesini, "karpuz" ile değiştiriniz

#   3) ...na "kivi" meyvesini sona ekleyiniz

#   4) ...na "kivi" meyvesini "armut" dan sonra yer alacak şekilde ekleyiniz

#   5) ...ndan "çilek" meyvesini çıkarınız

#   6) ...nın son elemanını negatif index kullanarak yazdırınız.

#   7) ... elemanlarından 2.,3. ve 4. elemanları yazdıran indexleme (slicing) işlemini yapınız

#   8) ...nın kaç elemandan oluştuğunu yazdırınız

# }



isim = "Deniizi"
print(isim.count("a"))

