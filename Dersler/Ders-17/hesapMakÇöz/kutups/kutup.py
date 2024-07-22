# + Toplama
# + Çıkarma
# + Çarpma
# + Bölme
# + Karakök Alma
# + Kuvvetini alma
# + Bölümden kalanı bulma

# işlemlerini yerine getirecek bir hesap makinesi 

from math import pow

def toplama(num1:int, num2: int) -> int:
    return num1 + num2

def cikarma(num1, num2):
    return num1 - num2

def carpma(*num1):
    result = 1
    for i in num1:
        result*=i
    return result

def bolme(num1, num2):
    # if num2== 0:
    #     return "Bölen 0 olamaz"
    # else:
    #     return num1/num2
    
    try:
        num3= num1 / num2
    except ZeroDivisionError:
        print("0 a bölüm hatası...")
    else:
        print("Bu oldu gibi")
        return num3
    finally:
        print("Hrpsi bitti...")
        
    

def kokAlma(num1, num2):
    return pow(num1, 1/num2)

def kuvvetiniAlma(num1, num2):
    return pow(num1, num2)

def bolumdenKalaniniBulma(num1, num2):
    return num1 % num2

def islemSecimi():
    secim = input("Bir işlem seçiniz:\n"
                  "1. Toplama\n"
                  "2. Çıkarma\n"
                  "3. Çarpma\n"
                  "4. Bölme\n"
                  "5. Kök Alma\n"
                  "6. Kuvvetini Alma\n"
                  "7. Kalanı Bulma\n"
                  "8. Çıkış\n"
                  "Seçim: ")

    if not secim.isdigit():
        return None
    secim = int(secim)
    if secim not in range(1, 9):
        return None
    return secim

def sayiGir():
        number_1 = int(input("Birinci Sayı: "))
        number_2 = int(input("İkinci Sayı: "))
        return number_1, number_2


def main():
    try:
        secim = islemSecimi()
        # if secim is None:
        #     print("Geçersiz seçim!")
        #     return

        if secim == 8:
            exit()

        num_1, num_2 = sayiGir()
        if num_1 is None or num_2 is None:
            print("Geçersiz sayı girişi!")
            return

        if secim == 1:
            sonuc = toplama(num_1, num_2)
        elif secim == 2:
            sonuc = cikarma(num_1, num_2)
        elif secim == 3:
            sonuc = carpma(num_1, num_2)
        elif secim == 4:
            sonuc = bolme(num_1, num_2)
        elif secim == 5:
            sonuc = kokAlma(num_1, num_2)
        elif secim == 6:
            sonuc = kuvvetiniAlma(num_1, num_2)
        elif secim == 7:
            sonuc = bolumdenKalaniniBulma(num_1, num_2)

        print("İşlem Sonucu:", sonuc)
    except ValueError as e:
        print(str(e))
    except Exception as e:
         print("Bir hata oluştu:", e)

