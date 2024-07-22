import os
from cryptography.fernet import Fernet

filePath = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-19/sifreYonetici/sifre.txt"
keyPath = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-19/sifreYonetici/key.data"

def anahtarOku():
    if not os.path.exists(keyPath):
        anahtarOlustur()
    with open(keyPath, "rb") as file:
        key = file.read()
        return key
    
def anahtarOlustur():
    key = Fernet.generate_key()
    with open(keyPath,"wb") as file:
        file.write(key)
        
key = anahtarOku()
anahtar = Fernet(key)

def dosyaMevcutMu(filePath):
    return os.path.exists(filePath)

def tumunuGoruntule(filePath):
    if dosyaMevcutMu(filePath):
        with open(filePath, "r") as dosya:
            for line in dosya:
                kullanici, sifre = line.replace("\n","").split(":")
                sifre = anahtar.decrypt(sifre.encode()).decode()
                print(f"Kullanıcı Adı: {kullanici}\t Sifre: {sifre}")
    else:
        print("Belirtilen konumda dosya mevcut değil...")

def yeniEkle():
    kullanici = input("Kullanıcı Adi Giriniz: ")
    sifre = input("Sifre Giriniz: ")
    with open(filePath, "a") as dosya:
        dosya.write(kullanici + ":" + anahtar.encrypt(sifre.encode()).decode() + "\n")

def sifreDegistir():
    kullanici = input("Kullanici : ")
    if not dosyaMevcutMu(filePath):
        print("Belirtilen konumda dosya mevcut değil...")
        return

    with open(filePath, "r") as dosya:
        satirlar = dosya.readlines()
    
    for i, satir in enumerate(satirlar):
        if kullanici in satir:
            yeniSifre = input("Yeni Sifre : ")
            satirlar[i] = kullanici + ":" + anahtar.encrypt(yeniSifre.encode()).decode() + "\n"
            break
    else:
        print("Kullanıcı mevcut değil!!!")
        return

    with open(filePath, "w") as dosya:
        dosya.writelines(satirlar)

def kullaniciSil():
    kullanici = input("Kullanici Adı Giriniz : ")
    if not dosyaMevcutMu(filePath):
        print("Belirtilen konumda dosya mevcut değil...")
        return

    with open(filePath, "r") as dosya:
        satirlar = dosya.readlines()

    satirlar = [satir for satir in satirlar if kullanici not in satir]

    with open(filePath, "w") as dosya:
        dosya.writelines(satirlar)

def main():
    while True:
        secim = input("Yapmak istediğiniz işlemi seçiniz : \n" + \
                    "1. Kullanıcı ve Şifre Görüntüleme \n" + \
                    "2. Kullanıcı Ekleme\n" + \
                    "3. Kullanıcı Silme\n" + \
                    "4. Şifre Değiştirme\n"+ \
                    "5. Çıkış\n" + \
                    "Seçiminiz : ")
        if secim == "1":
            tumunuGoruntule(filePath)
        elif secim == "2":
            yeniEkle()
        elif secim == "3":
            kullaniciSil()
        elif secim == "4":
            sifreDegistir()
        elif secim == "5":
            print("Bizi seçtiğiniz için teşekkür ederiz.")
            exit()
        else:
            print("Geçersiz seçim yaptınız!")

if __name__ == "__main__":
     main()
