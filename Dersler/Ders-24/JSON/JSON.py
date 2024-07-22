import json

myDict = {"adi":"Ajda", "yasi":None, "hayatta":True,  "evli": False , "sevdiğiMeyveler":["Elma", "Armut"]}
#values2 = dict(adi="Ahmet", soyadi="Bilmem kim", arac="Anadol")

for key,detay in myDict.items():
    print(key, detay, end=" ")
print()

print(myDict)

jsonDumps = json.dumps(myDict, indent=4, sort_keys=True)

print(jsonDumps)
print(type(jsonDumps))

#Calısmaz!!! JSON String değil... Sonra Try-Except ile dene...
myJsonStr = '{"adi":"Ajda", "yasi":None, "hayatta":True,  "evli": False , "sevdiğiMeyveler":["Elma", "Armut"]}'
newData = json.loads(myJsonStr)

# JSON String donusum kurallarına uyması gerek...
# None -> null
# False -> false
# True -> true

try:
    myJsonStr = '{"adi":"Ajda", "yasi":None, "hayatta":True,  "evli": False , "sevdiğiMeyveler":["Elma", "Armut"]}'
    newData = json.loads(myJsonStr)
except:  # noqa: E722
    print("Dönüştürme İşlemi başarısız...")
else:
    print(newData)

#--------------------------------------------------
#File Ops

path = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-23/some.json"
newPath = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-23/some2.json"
with open(path) as jFile :
    try:
        data = json.load(jFile)
    except Exception as e:
        print(str(e))
    else:
        print(data)
        print(type(data))

for item,value in data.items():
    print(item, value)


#---------------------------------------------------

data["Yasi"] = 75
data["pets"] = "Cat","Dog","Bird"
data["cars"][0]["model"] = "Mercedes"



with open(newPath, "w") as file:
    json.dump(data, file, indent=4)



import requests  # noqa: E402
# https://jsonbin.io/quick-store

url1= "http://ip.jsontest.com/"
url2="https://api.jsonbin.io/v3/qs/666722bcacd3cb34a8557e8b"
response = requests.get(url1)
data = json.dumps(response.json(),indent=4)
print(type(data))
print(data)

#------------------------------------
#     IKINCI VERSIYON
#------------------------------------

# print(json.dumps(data, indent=2))

from urllib.request import urlopen

with urlopen(url1) as response:
    source = response.read()

data = json.loads(source)
print(data)