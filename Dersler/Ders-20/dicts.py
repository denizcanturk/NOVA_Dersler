arabam =	{
                "brand": "Ford",
                "model": "Mustang",
                "year" : 1964,
                "color": "white"
            }

#Constructor ile kullanım.
# arabam2 = dict(brand="Doğan", model="SLX",year=1995 )

# print(arabam)
# print(arabam2)

# print(len(arabam))

# #Elemanlara Erişim

# brand = arabam["brand"]
# brand2 = arabam2.get("brand")
# print(brand, brand2)

#Dict in anahtar kelimelerini listeleme:
# print(arabam.keys())
# print(arabam.values())

#Anahtarın Değerini değiştirme
# arabam["brand"] = "Ferrari"
# arabam["color"] = "Red"


a = arabam.items()
print(a)

#Anahtar değeri mevcut mu
# if "brand" in arabam:
#     print("Mevcut")

# arabam.update({"Jant":25})
# arabam.update(dict(type="sedan"))
# arabam["Cam Filmi"] = "Mevcut"
# print(arabam)

#removing item
# arabam.pop("Cam Filmi")
# print(arabam)

#Dict in son elemanını siler
# arabam.popitem()

#del kullanarak silme
# del arabam["Jant"]

#clear içini boşaltır
# arabam.clear()
# print(arabam)

#Loop Through a Dictionary

#Anahtarları yazdırma
# for x in arabam:
#     print(x)

#Değerleri yazdırma
# for x in arabam:
#     print(arabam[x])

#Değerleri yazdırma
# for x in arabam.values():
#     print(x)

#Anahtar ve Değerleri yazdırmak için:
# for anahtar, deger in arabam.items():
#     print(anahtar+" "+ deger)


#dict kopyalama
# kopyasi = arabam.copy()
# ikinciKopyasi = dict(arabam)

#İç içe Dict yapısı
ailem = {
    "Annem" : {
      "Adı" : "Nebahat",
       "DT" : 1964
    },
    "Babam": {
      "Adı":"Şemsi",
       "DT": 1950
    },
    "Kardes" : {
        "Adi":"Emre",
         "DT": 1995
    }
}

for anahtar, degerler in ailem.items():
    print(anahtar)

    for deger in degerler:
        print(deger, ":", degerler[deger])
