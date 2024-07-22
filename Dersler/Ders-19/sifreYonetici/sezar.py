metin = input("Şifrelenecek metni griin : ")
sifreliMetin=""
cozulmusMetin = ""
print("Sifreleniyor...\n")
for harf in metin:
    yeniHarf = chr(ord(harf) +3)
    sifreliMetin += "".join(yeniHarf)

print("Sezar Metodu ile Sifrelenmiş Metin :", sifreliMetin)
print("Çözülüyor...\n")

for harf in sifreliMetin:
    yeniHarf = chr(ord(harf)-3)
    cozulmusMetin += yeniHarf

print("Cozulmuş Metin : ", cozulmusMetin)
