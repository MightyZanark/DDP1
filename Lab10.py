# TopicL GUI

import tkinter as tk
import tkinter.messagebox as tkmsg


class Data():
    """Data class to save the item data in KarungAjaib
    Data is set to be list
    """

    def __init__(self):
        self.__isi_karung = []
    
    def get_isi_karung(self):
        return self.__isi_karung
    
    def add_item(self, item):
        """Shows an error if item is already in isi_karung
        Adds the item and shows a successful message otherwise
        """

        if item in self.__isi_karung:
            return tkmsg.showerror('ItemHasFound',
                                  f'Item dengan nama {item} sudah ada di dalam KarungAjaib.\n'
                                  f'Item {item} tidak bisa dimasukkan lagi.')
       
        self.__isi_karung.append(item)
        return tkmsg.showinfo('Berhasil', f'Berhasil memasukkan item {item}')
    
    def rem_item(self, item):
        """Shows an error if item is not in isi_karung
        Removes the item and shows a successful message otherwise"""

        if item not in self.__isi_karung:
            return tkmsg.showerror('ItemNotFound', 
                                  f'Item dengan nama {item} tidak ditemukan dalam KarungAjaib')
        
        self.__isi_karung.remove(item)
        return tkmsg.showinfo('Berhasil!', f'Berhasil mengeluarkan item {item}')


class MainWindow(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Karung Ajaib")
        self.isi_karung = Data()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self,
            text="Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia"
        )

        self.btn_lihat_daftar_karung = tk.Button(
            self,
            text="LIHAT DAFTAR KARUNG",
            command=self.popup_lihat_karung
        )

        self.btn_masukkan_item = tk.Button(
            self,
            text="MASUKKAN ITEM",
            command=self.popup_add_item
        )

        self.btn_keluarkan_item = tk.Button(
            self,
            text="KELUARKAN ITEM",
            command=self.popup_keluarkan_item
        )

        self.btn_exit = tk.Button(
            self,
            text="EXIT",
            command=self.master.destroy
        )
    
        self.label.pack()
        self.btn_lihat_daftar_karung.pack()
        self.btn_masukkan_item.pack()
        self.btn_keluarkan_item.pack()
        self.btn_exit.pack()

    def popup_lihat_karung(self):
        PopupLihatKarung(self.isi_karung, self.master)
    
    def popup_add_item(self):
        PopupAddItem(self.isi_karung, self.master)

    def popup_keluarkan_item(self):
        PopupKeluarkanItem(self.isi_karung, self.master)


class PopupLihatKarung(tk.Toplevel):
    def __init__(self, isi_karung: Data, master = None):
        super().__init__(master)
        self.geometry("280x100")
        self.wm_title("Lihat Karung")
        self.isi_karung = isi_karung
        self.items = self.isi_karung.get_isi_karung()
        self.items.sort()
        
        # Initialize and set descriptor widget
        self.title = tk.Label(self, text="Daftar Karung Ajaib")
        self.nama = tk.Label(self, text="Nama Item")
        self.title.pack()
        self.nama.pack()

        for i in range(len(self.items)):
            # Initialize and sets all the item in KarungAjaib
            self.item_info = tk.Label(self, text=f'{i+1}. {self.items[i]}')
            self.item_info.pack()

        # Initialize and set exit button
        self.exit_button = tk.Button(self, text="EXIT", command=self.destroy)
        self.exit_button.pack()


class PopupAddItem(tk.Toplevel):
    def __init__(self, isi_karung: Data, master = None):
        super().__init__(master)
        self.geometry("280x100")
        self.wm_title("Masukkan Item")
        
        self.isi_karung = isi_karung
        self.add_item = tk.StringVar()
        
        # Sets the grid's row and column
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        # Initialize widgets
        self.title = tk.Label(self, text="Input Masukkan Item")
        self.nama = tk.Label(self, text="Nama Item")
        self.ent_nama = tk.Entry(self, textvariable=self.add_item)
        self.submit_button = tk.Button(self, text='Masukkan', command=self.masukkan_item)

        # Sets the widget
        self.title.grid(row=0, column=1)
        self.nama.grid(row=1, column=0)
        self.ent_nama.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=1)
    

    def masukkan_item(self):
        """Adds an item the user inputted"""

        self.isi_karung.add_item(self.add_item.get())
        self.destroy()


class PopupKeluarkanItem(tk.Toplevel):
    def __init__(self, isi_karung: Data, master = None):
        super().__init__(master)
        self.geometry("280x100")
        self.wm_title("Keluarkan Item")
        
        self.isi_karung = isi_karung
        self.rem_item = tk.StringVar()
        
        # Sets the grid's row and column
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Initialize widgets
        self.title = tk.Label(self, text="Input Keluarkan Item")
        self.nama = tk.Label(self, text="Nama Item")
        self.ent_item = tk.Entry(self, textvariable=self.rem_item)
        self.submit_button = tk.Button(self, text='Ambil', command=self.keluarkan_item)

        # Sets the widgets
        self.title.grid(row=0, column=1)
        self.nama.grid(row=1, column=0)
        self.ent_item.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=1)


    def keluarkan_item(self):
        """Removes an item the user inputted"""

        self.isi_karung.rem_item(self.rem_item.get())
        self.destroy()


if __name__ == '__main__':
    mainapp = MainWindow()
    mainapp.master.mainloop()
