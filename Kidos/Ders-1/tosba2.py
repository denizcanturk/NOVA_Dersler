"""
BUGÜN NELER ÖĞRENDİK : 

Bu derste tosba mızı kullanarak şekil çizmeyi,
şekilde çizerken pencerenin adını, arka plan rengini değiştirmeyi
ve hatta çiziğimiz kalem rengini değiştirmeyi. Belirli noktalar
arasında çizgi çizmeden ilerlemeyi öğrendik.

Ev çizmeleri için verilen görevde çocuklarımızın kendi başlarına
sorun çözme becerileri, ekip arkadaşları ile birlikte hareket 
ederek çözüme ulaşma becerileri ağırlıklı pratik çalışmalarımız
oldu.

"""

import turtle as tosba
#Penceremizi oluşturuyoruz ve boyutlarını belirliyoruz
pencere=tosba.Screen()
pencere.setup(width=500,height=500)

#Penceremizin bağlığını belirliyoruz
pencere.title("Arkadaşım Tosbik")
#Penceremizin arka planını belirliyoruz
pencere.bgcolor("white")

#Tosbik imizi oluşturuyoruz ve hızını belirliyoruz
tosbik = tosba.Turtle()
tosbik.speed(10)

#Çizim için kalem rengimizi belirliyoruz
tosbik.pencolor("black")

#İleri 100 pixel
tosbik.forward(100)
#sağa 90 derece
tosbik.right(90)
tosbik.forward(100)
tosbik.right(90)
tosbik.forward(100)
tosbik.right(90)
tosbik.forward(100)

#Çatı için kalem rengimizi değiştiriyoruz.
tosbik.pencolor("red")
tosbik.right(30)
tosbik.forward(100)
tosbik.right(120)
tosbik.forward(100)

#Diğer evi çizmeye başlayacağımız noktaya ilerlemek için 
#kalemi havaya kaldırıyoruz.
tosbik.penup()

tosbik.right(90)
tosbik.forward(200)

#Artık çizmeye başlayabiliriz
tosbik.pencolor("black")
tosbik.pendown()
tosbik.right(30)
tosbik.forward(100)
tosbik.right(90)
tosbik.forward(100)
tosbik.right(90)
tosbik.forward(100)
tosbik.right(90)
tosbik.forward(100)

#Çatıya siz devam edin... :)




#Her zaman en sonda olmalı
pencere.mainloop()


