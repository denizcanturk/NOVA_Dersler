# Bilgisayar 1-100 arasında bir sayı üretir
# Kullanıcıya giriş yapması gereken aralık belirtilir
# Kullanıcı sayıyı buluncaya kadar yönlendirilir
# Örn.: Kullanıcı ilk iki tahmininde 15 ve 85 girdi ise:
# Sayı girmesi gereken aralık "15-85 arasında bir sayı giriniz:" şeklinde olmalıdır
# Kullanıcının yaptığı tahminler bir listede tutulur
# Kullanıcının yaptığı tahmin sayısı ve yaptığı tahminler
# oyun sonunda ekrana yazdırılır
# Oyuncu oyundan çıkmak için q harfi ile giriş yapmalıdır

from random import randint

min = 1
max = 100
bilgisayar = randint(1,100)

tahminlerim = []
while True:
    tahmin = input("{}-{} arası bir sayi giriniz: ".format(min,max))
    
    if tahmin == "q":
        break
    elif not tahmin.isdigit():
        print("Bir SAYI girin dedim.")
        continue
    
    tahmin = int(tahmin)

    tahminlerim.append(tahmin)
    

    if tahmin > bilgisayar:
        print("Daha Küçük")
        if not tahmin > max:
            max = tahmin
    
    if tahmin < bilgisayar:
        print("Daha büyük")
        if tahmin > min:
            min = tahmin

    if tahmin==bilgisayar:
        print("Kutlarıııııızz..")
        break

for i,item in enumerate(tahminlerim):
    print(i+1,".\ttahmin: ".expandtabs(3), item, sep="")
print("Oyun, {} adımda tamamlandı".format(len(tahminlerim)))

