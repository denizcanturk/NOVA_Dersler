# import turtle
# turtle.shape("turtle")
# turtle.speed(5)
# angle = int(input("Kenar sayısını girin"))
# size = int(input("Kenar uzunluğunu girin"))
# color = input("Rengi girin")
# turtle.color(color)
# if angle < 3:
#     print("Kenar sayısı üçten az olamaz")
# elif angle == 3:
#     turtle.forward(size)
#     turtle.left(120)
#     turtle.forward(size)
#     turtle.left(120)
#     turtle.forward(size)
# elif angle == 4:
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)

import turtle
turtle.shape("turtle")
turtle.speed(100)
turtle.color("black")
for i in range(50):
    turtle.circle(2*i)
    turtle.left(30)

turtle.mainloop()