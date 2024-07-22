import time as t
class SinifAdi:
   'Sınıf dokümantasyon metni...'
   #Sinif Elemanları / Class Members


print ("SinifAdi.__doc__:", SinifAdi.__doc__)
print ("SinifAdi.__name__:", SinifAdi.__name__)
print ("SinifAdi.__module__:", SinifAdi.__module__)
print ("SinifAdi.__bases__:", SinifAdi.__bases__)

#-------------------------------------------

class Calisan:
   'Calisan personel için genel sınıf'
   #private Example to be provided...
   calisanSayisi = 0

   def __init__(self, adi, maasi):
      self.adi = adi
      self.maasi = maasi
      Calisan.calisanSayisi += 1
   
   def __del__(self):
      print("Yok Edici Çalıştı! Nesne hafızadan silindi...")

   def kacCalisanVar(self):
     print("Toplam Calisan Sayisi {}".format(Calisan.calisanSayisi))

   def calisanBilgileri(self):
      print("adi : ", self.adi,  ", maasi: ", self.maasi)
      print(Calisan.calisanSayisi)



patron = Calisan("Aydan", 40000)
isci = Calisan("Deniz", 4000)
patron.calisanBilgileri()
isci.calisanBilgileri()

#-------------------------------------------
