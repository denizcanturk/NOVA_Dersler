import tkinter as tk
from tkinter import messagebox
import csv
from tkcalendar import DateEntry
import datetime as dt

def add_data():
    data = [
        entry_sira.get(),
        entry_stok_kodu.get(),
        entry_malzeme_adi.get(),
        entry_miktar.get(),
        entry_birim.get(),
        entry_giris_tarihi.get(),
        entry_uretim_tarihi.get(),
        entry_lot_numarasi.get(),
        entry_son_kullanma_tarihi.get(),
        entry_uretime_verilis_tarihi.get(),
        entry_cikti_miktari.get(),
        entry_cikti_lot_numarasi.get()
    ]

    if any(not field for field in data):
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
        return

    with open('malzeme_listesi.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    messagebox.showinfo("Başarılı", "Veri başarıyla eklendi.")
    clear_entries()

def clear_entries():
    try:
        entry_sira.delete(0, tk.END)
        entry_stok_kodu.delete(0, tk.END)
        entry_malzeme_adi.delete(0, tk.END)
        entry_miktar.delete(0, tk.END)
        entry_birim.delete(0, tk.END)
        entry_giris_tarihi.set_date(dt.datetime.today())
        entry_uretim_tarihi.set_date(dt.datetime.today())
        entry_lot_numarasi.delete(0, tk.END)
        entry_son_kullanma_tarihi.set_date(dt.datetime.today())
        entry_uretime_verilis_tarihi.set_date(dt.datetime.today())
        entry_cikti_miktari.delete(0, tk.END)
        entry_cikti_lot_numarasi.delete(0, tk.END)
    except:
        print("Temizlenecek veri bulunamadı...")

# Tkinter GUI
root = tk.Tk()
root.title("Malzeme Bilgisi Girişi")

labels = [
    "Sıra No", "Malzeme Stok Kodu", "Malzeme Adı", "Miktar", "Birim", 
    "Giriş Tarihi", "Malzemenin Üretim Tarihi", "Lot Numarası", 
    "Malzemenin Son Kullanma Tarihi", "Üretime Veriliş Tarihi", 
    "Çıktı Miktarı", "Çıktı Lot Numarası"
]

entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    if "Tarih" in label:
        entry = DateEntry(root, date_pattern='dd-mm-yyyy')
    else:
        entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

entry_sira, entry_stok_kodu, entry_malzeme_adi, entry_miktar, entry_birim, entry_giris_tarihi, entry_uretim_tarihi, entry_lot_numarasi, entry_son_kullanma_tarihi, entry_uretime_verilis_tarihi, entry_cikti_miktari, entry_cikti_lot_numarasi = entries

tk.Button(root, text="Veri Ekle", command=add_data).grid(row=len(labels), column=0, pady=10)
tk.Button(root, text="Temizle", command=clear_entries).grid(row=len(labels), column=1, pady=10)

root.mainloop()
