import tkinter as tk
import pyttsx3 as p

konusucu = p.init()

def oku():
    konusucu.say(giris.get())
    konusucu.runAndWait()
    konusucu.stop()

root = tk.Tk()
root.title("Merhaba Python")
root.geometry("300x50")

etiket = tk.Label(root, text="Metin", font=30)
etiket.pack(side=tk.LEFT, padx=5)

giris = tk.Entry(root,width=15, bd=0)
giris.pack(side=tk.LEFT, padx=5)

btn = tk.Button(root, text="Oku", bg="red", fg="white", command=oku)
btn.pack(side=tk.LEFT, padx=5)

root.mainloop()