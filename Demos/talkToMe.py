import tkinter as t
import pyttsx3 as p

konusucu= p.init()

print(konusucu.getProperty("voices"))

def konus():
    konusucu.setProperty("rate",150)
    konusucu.say(metin.get())
    konusucu.save_to_file(metin.get(),"konus.mp3")
    konusucu.runAndWait()
    konusucu.stop()

anaPencere = t.Tk()

anaPencere.title("Merhaba Dünya")
anaPencere.geometry("300x50")

etiket = t.Label(anaPencere, text="Metin:",font=30)
etiket.pack(side=t.LEFT, padx=5)

metin = t.Entry(anaPencere, font=30, width=15, bd=0)
metin.pack(side=t.LEFT, padx=5)

dugme = t.Button(anaPencere, text="Konus", bg="black", fg="white", bd=0, command=konus)
dugme.pack(side=t.LEFT, padx=5)


anaPencere.mainloop()