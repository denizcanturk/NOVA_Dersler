import tkinter as tk

def hesapla():
    sonuc = eval(enGiris.get())
    enGiris.insert(tk.END, " = "+ str(sonuc))

anaPencere = tk.Tk()

anaPencere.title("Hesap Makinesi")
anaPencere.geometry("300x50")

lblIslem = tk.Label(anaPencere, text="İşlem", font=30)
lblIslem.pack(side=tk.LEFT, padx=5)

enGiris = tk.Entry(anaPencere, width=15, bd=0)
enGiris.pack(side=tk.LEFT, padx=5)

btnDugme = tk.Button(anaPencere, text="Hesapla", font=30, bg="red", fg="white", command=hesapla)
btnDugme.pack(side=tk.LEFT, padx=5)

anaPencere.mainloop()