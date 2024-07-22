import tkinter as tk
from tkinter import messagebox
import csv
from tkcalendar import DateEntry
import datetime as dt

class MalzemeForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Malzeme Bilgisi Girişi")
        self.create_widgets()
        
    def create_widgets(self):
        labels = [
            "Sıra No", "Malzeme Stok Kodu", "Malzeme Adı", "Miktar", "Birim", 
            "Giriş Tarihi", "Malzemenin Üretim Tarihi", "Lot Numarası", 
            "Malzemenin Son Kullanma Tarihi", "Üretime Veriliş Tarihi", 
            "Çıktı Miktarı", "Çıktı Lot Numarası"
        ]
        
        self.entries = []

        for i, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=i, column=0, sticky="w", pady=3)
            if "Tarih" in label:
                entry = DateEntry(self, date_pattern='dd-mm-yyyy')
            else:
                entry = tk.Entry(self)
            entry.grid(row=i, column=1, sticky="we", pady=3, padx=5)
            self.entries.append(entry)

        self.entry_sira, self.entry_stok_kodu, self.entry_malzeme_adi, self.entry_miktar, self.entry_birim, \
        self.entry_giris_tarihi, self.entry_uretim_tarihi, self.entry_lot_numarasi, \
        self.entry_son_kullanma_tarihi, self.entry_uretime_verilis_tarihi, \
        self.entry_cikti_miktari, self.entry_cikti_lot_numarasi = self.entries

        tk.Button(self, text="Veri Ekle", command=self.add_data).grid(row=len(labels), column=0, pady=10)
        tk.Button(self, text="Temizle", command=self.clear_entries).grid(row=len(labels), column=1, pady=10)

    def add_data(self):
        data = [
            self.entry_sira.get(),
            self.entry_stok_kodu.get(),
            self.entry_malzeme_adi.get(),
            self.entry_miktar.get(),
            self.entry_birim.get(),
            self.entry_giris_tarihi.get(),
            self.entry_uretim_tarihi.get(),
            self.entry_lot_numarasi.get(),
            self.entry_son_kullanma_tarihi.get(),
            self.entry_uretime_verilis_tarihi.get(),
            self.entry_cikti_miktari.get(),
            self.entry_cikti_lot_numarasi.get()
        ]

        if any(not field for field in data):
            messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
            return

        with open('malzeme_listesi.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        
        messagebox.showinfo("Başarılı", "Veri başarıyla eklendi.")
        self.clear_entries()

    def clear_entries(self):
        try:
            self.entry_sira.delete(0, tk.END)
            self.entry_stok_kodu.delete(0, tk.END)
            self.entry_malzeme_adi.delete(0, tk.END)
            self.entry_miktar.delete(0, tk.END)
            self.entry_birim.delete(0, tk.END)
            self.entry_giris_tarihi.set_date(dt.datetime.today())
            self.entry_uretim_tarihi.set_date(dt.datetime.today())
            self.entry_lot_numarasi.delete(0, tk.END)
            self.entry_son_kullanma_tarihi.set_date(dt.datetime.today())
            self.entry_uretime_verilis_tarihi.set_date(dt.datetime.today())
            self.entry_cikti_miktari.delete(0, tk.END)
            self.entry_cikti_lot_numarasi.delete(0, tk.END)
        except:
            print("Temizlenecek veri bulunamadı...")

if __name__ == "__main__":
    app = MalzemeForm()
    app.mainloop()
