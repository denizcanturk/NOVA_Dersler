#https://www.amp-what.com/

import tkinter as tk
import random as rd
import time as t
root = tk.Tk()
root.title("Şanslı Zarlar")
root.geometry("600x400")
zar = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]

def zarAt(zar):
    
    rollingTime = rd.randint(1,100)
    rollingDelay = 1/rollingTime
    for i in range(rollingTime):
        lblZar.configure(text="{}{}".format(rd.choice(zar), rd.choice(zar)))
        lblZar.pack()
        root.update()
        t.sleep(rollingDelay)
        rollingDelay=((i+1)/rollingTime)/4


btnZar = tk.Button(root, text="Zarları At", font=30,bg="red",fg="white", width=50, height=2, command=lambda:zarAt(zar))
btnZar.pack(pady=10)

lblZar = tk.Label(root, text="", font=("Arial", 200))
lblZar.pack()
root.mainloop()
