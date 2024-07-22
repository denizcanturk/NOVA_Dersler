import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

pencere = tk.Tk()
pencere.title("Hadi bakalım")
pencere.geometry(str(int(pencere.winfo_screenwidth()/3))+"x200")


labels = ["Sıra no", "Malzeme Stok No","Malzeme Adi", "Miktar", "Birim", "Giriş Tarihi", "Malzeme Üretim Tarihi", \
          "Lot Numarası", "Malzeme Son Kullanma Tarihi", "Üretime Veriliş Tarihi", "Çıktı Miktarı", "Çıktı Lot Numarası"]


for idx, label in enumerate(labels):
    tk.Label(pencere, text=label).grid(row=0, column=idx, padx=5,sticky="w")
    if "tarih" in label.lower():
        DateEntry(pencere, date_pattern="dd-mm-yy").grid(row=1, column=idx)
    else:
        tk.Entry(pencere, width=6).grid(row=1, column=idx, padx=5, sticky="w")

pencere.mainloop()



# ListBox : ComboBox ın açık hali olarak değerlendirilebilir
# İçerisindeki elemanlar alt alta listelenir. 

# listItems = ["Birinci Eleman", "İkinci Eleman", "Üçüncü Eleman"]

# listBox = tk.Listbox(pencere, height=len(listItems), relief=tk.RIDGE, bd=3, border=3)
# for idx, i in enumerate(listItems):
#     listBox.insert(idx, i)
# listBox.grid(row=3, column=1, rowspan=4)