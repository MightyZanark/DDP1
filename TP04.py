import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msgbox
from random import randint


class Menu():
    """Parent class of all menu types object"""

    def __init__(self, code: str, name: str, price: int):
        self.__code = code
        self.__name = name
        self.__price = price

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_item(self, index: int):
        """Gets an item by their index
        0: code
        1: name
        2: price
        """
        
        if index == 0:
            return self.get_code()

        if index == 1:
            return self.get_name()

        if index == 2:
            return self.get_price()

        return None

    def __str__(self):
        return f'Debug: {self.__class__} - {self.__code} - {self.__name}'


class Meals(Menu):
    """Meals menu type, have a new "savory" attribute"""

    def __init__(self, code: str, name: str, price: int, savory_lvl: int):
        super().__init__(code, name, price)
        self.__savory_lvl = savory_lvl

    def get_savory_lvl(self):
        return self.__savory_lvl

    def get_item(self, index: int):
        """Gets an item by their index
        0: code
        1: name
        2: price
        3: savory_lvl
        """
        
        if index == 3:
            return self.get_savory_lvl()

        return super().get_item(index)


class Drinks(Menu):
    """Drinks menu type, have a new "sweet" attribute"""

    def __init__(self, code: str, name: str, price: int, sweet_lvl: int):
        super().__init__(code, name, price)
        self.__sweet_lvl = sweet_lvl

    def get_sweet_lvl(self):
        return self.__sweet_lvl

    def get_item(self, index: int):
        """Gets an item by their index
        0: code
        1: name
        2: price
        3: sweet_lvl
        """
        if index == 3:
            return self.get_sweet_lvl()

        return super().get_item(index)


class Sides(Menu):
    """Sides menu type, have a new "viral" attribute"""

    def __init__(self, code: str, name: str, price: int, viral_lvl: int):
        super().__init__(code, name, price)
        self.__viral_lvl = viral_lvl

    def get_viral_lvl(self):
        return self.__viral_lvl

    def get_item(self, index: int):
        """Gets an item by their index
        0: code
        1: name
        2: price
        3: viral_lvl
        """

        if index == 3:
            return self.get_viral_lvl()

        return super().get_item(index)


class Table():
    """Table class used to store table information and create a
    menu box/table based on said information and 'menu'
    """
    
    def __init__(self, menu: dict):
        self.__table_info = {i: {} for i in range(10)}
        self.__menu = menu

    def get_table_info(self):
        return self.__table_info

    def generate_menu_table(
            self, 
            root=None, 
            finish: bool = False, 
            str_var: dict = None, 
            cbbox_data: dict = None, 
            func: list = None, 
            order: dict = None):
        """Creates a menu table and places said table on 'root'
        Args:
        root = The window where the table will be placed on
        finish = Checks if the table created is for info only 
                 or have a ttk.Combobox to set values
        str_var = A dictionary of tk.StringVar to save the value 
                  from Combobox. The dictionary is split according
                  to the total menu types
        cbbox_data = A dictionary to save the created Comboboxes
                     so it can be accessed later
        func = A list of 2 function used for Comboboxes and tracing
               tk.StringVar so it updates on write
        order = A dictionary of the current order which are used
                when 'finish' is set to True
        """

        cur_row = 0
        extra_info = {
            "MEALS": "Kegurihan",
            "DRINKS": "Kemanisan",
            "SIDES": "Keviralan"
        }

        table_box = tk.Frame(master=root)
        for menu_type in self.__menu:
            lbl_type = tk.Label(table_box, text=menu_type)

            ent_code = tk.Entry(table_box, width=20)
            ent_code.insert(tk.END, 'Kode')
            ent_code['state'] = 'readonly'

            ent_name = tk.Entry(table_box, width=20)
            ent_name.insert(tk.END, 'Nama')
            ent_name['state'] = 'readonly'

            ent_price = tk.Entry(table_box, width=20)
            ent_price.insert(tk.END, 'Harga')
            ent_price['state'] = 'readonly'

            ent_extra_info = tk.Entry(table_box, width=20)
            ent_extra_info.insert(tk.END, extra_info[menu_type])
            ent_extra_info['state'] = 'readonly'

            ent_amount = tk.Entry(table_box, width=20)
            ent_amount.insert(tk.END, 'Jumlah')
            ent_amount['state'] = 'readonly'

            lbl_type.grid(row=cur_row, column=0)
            cur_row += 1
            ent_code.grid(row=cur_row, column=0)
            ent_name.grid(row=cur_row, column=1)
            ent_price.grid(row=cur_row, column=2)
            ent_extra_info.grid(row=cur_row, column=3)
            ent_amount.grid(row=cur_row, column=4)
            cur_row += 1

            menu_list = self.__menu[menu_type]
            total_row = len(menu_list)
            for i in range(total_row):
                for j in range(4):
                    ent = tk.Entry(table_box, width=20)
                    ent.insert(tk.END, str(menu_list[i].get_item(j)))
                    ent['state'] = 'readonly'
                    ent.grid(row=i+cur_row, column=j)

                if not finish:
                    default_opt = [opt for opt in range(11)]
                    cur_str_var = str_var[menu_type][i]
                    cbbox = ttk.Combobox(
                        table_box, 
                        textvariable=str_var[menu_type][i], 
                        values=default_opt
                    )

                    cbbox.set(0)
                    cbbox_data[menu_type] = cbbox_data.get(menu_type, []) + [cbbox]
                    cur_str_var.trace_add(
                        'write', 
                        lambda var, index, mode, idx=i, menu_type=menu_type: 
                            func[0](var, index, mode, idx, menu_type)
                    ) # lambda to pass arguments to the function

                    cbbox.bind(
                        "<<ComboboxSelected>>", 
                        lambda event, x=i, menu_type=menu_type: 
                            func[1](event, x, menu_type)
                    ) 

                    cbbox.grid(row=i+cur_row, column=4)

                else:
                    ent = tk.Entry(table_box, width=20)
                    order_amt = order.get(menu_list[i].get_item(1), 0)
                    ent.insert(tk.END, order_amt)
                    ent['state'] = 'readonly'
                    ent.grid(row=i+cur_row, column=4)

            cur_row += total_row

        table_box.grid(row=1, column=0, columnspan=5, padx=(25, 0))


class Main(tk.Frame):
    def __init__(self, menu: dict, table: Table, master=None):
        super().__init__(master)
        self.__menu = menu
        self.__table = table
        self.master.title('Kafe Daun-Daun Pacilkom v2.0 🌿')
        self.master.geometry('400x200')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn_create_order = tk.Button(
            self, 
            text="Buat Pesanan", 
            bg="#4472C4", fg="white", 
            command=self.create_order
        )

        self.btn_finish = tk.Button(
            self, 
            text="Selesai Gunakan Meja", 
            bg="#4472C4", fg="white", 
            command=self.finish
        )

        self.btn_create_order.grid(row=0, column=0, padx=10, pady=40)
        self.btn_finish.grid(row=1, column=0)

    def create_order(self):
        NameScreen(self.__menu, self.__table, self.master)

    def finish(self):
        ChooseTableScreen(
            self.__menu, 
            self.__table,
            finish=True, 
            master=self.master
        )


class NameScreen(tk.Toplevel):
    """Window to ask for the customer's name while also checking if
    the tables are full or not
    """
    
    def __init__(self, menu: dict, table: Table, master=None):
        super().__init__(master)
        self.geometry('400x200')
        self.__name = tk.StringVar()
        self.__table = table
        self.__table_info = self.__table.get_table_info()
        self.__menu = menu
        self.lbl_question = tk.Label(self, text="Siapa nama Anda?")
        self.ent_name = tk.Entry(self, textvariable=self.__name)
        self.btn_back = tk.Button(
            self, 
            text="Kembali", 
            width=20, 
            bg="#4472C4", fg="white", 
            command=self.destroy
        )

        self.btn_next = tk.Button(
            self, 
            text="Lanjut", 
            width=20, 
            bg="#4472C4", fg="white", 
            command=self.next_page
        )

        self.lbl_question.grid(row=0, column=0, padx=(40, 0), pady=(80, 0))
        self.ent_name.grid(row=0, column=1, padx=(0, 40), pady=(80, 0))
        self.btn_back.grid(row=1, column=0, padx=(40, 5), pady=(50, 0))
        self.btn_next.grid(row=1, column=1, padx=(5, 40), pady=(50, 0))

    def next_page(self):
        name = self.__name.get()
        full_counter = 0
        for num in self.__table_info:
            if name == self.__table_info[num].get('name'):
                # Customer names according to the requirements
                # are said to be unique which I assume mean that
                # names can't be the same even if the table are
                # different
                msgbox.showerror("Name Unavailable",
                                 "That name has been taken")
                return

            if name == '':
                msgbox.showerror("Name Unavailable", "Name can't be empty")
                return

            if len(self.__table_info[num]) != 0:
                full_counter += 1

        if full_counter == 10:
            msgbox.showerror("Cafe Full",
                             "There are currently no empty tables. "
                             "Please come back at another time")

            self.destroy()
            return

        self.destroy()
        OrderScreen(self.__menu, self.__table, name, master=self.master)


class OrderScreen(tk.Toplevel):
    """Window for the customer to make orders"""

    def __init__(
            self, 
            menu: dict, 
            table: Table, 
            name: str, 
            table_num=None, 
            master=None):

        super().__init__(master)
        self.geometry('700x400')
        self.__menu = menu
        self.__cust_name = name
        self.__table = table
        self.__table_info = self.__table.get_table_info()
        if table_num == None:
            self.__table_num = randint(0, 9)
            while len(self.__table_info[self.__table_num]) != 0:
                self.__table_num = randint(0, 9)
        else:
            self.__table_num = table_num

        self.__str_var = {
            "MEALS": [tk.StringVar() for _ in range(len(self.__menu["MEALS"]))],
            "DRINKS": [tk.StringVar() for _ in range(len(self.__menu["DRINKS"]))],
            "SIDES": [tk.StringVar() for _ in range(len(self.__menu["SIDES"]))]
        }

        self.__cbbox_data = {}
        self.__cur_order = {}
        self.protocol('WM_DELETE_WINDOW', self.back_button)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_name = tk.Label(
            self, 
            text=f'Nama pemesan: {self.__cust_name}'
        )

        self.lbl_name.grid(row=0, column=0, padx=(20, 0), pady=(0, 40))

        self.__table.generate_menu_table(
            root=self, 
            str_var=self.__str_var, 
            cbbox_data=self.__cbbox_data, 
            func=[self.update_cbbox_val, self.update_order]
        )

        self.lbl_tab_num = tk.Label(self, text=f'No Meja: {self.__table_num}')
        self.btn_change_table = tk.Button(
            self, text="Ubah", command=self.change_table)

        self.lbl_tab_num.grid(row=0, column=2, padx=(140, 0), pady=(0, 40))
        self.btn_change_table.grid(row=0, column=3, padx=(0, 80), pady=(0, 40))

        self.total_price = 0
        self.lbl_total_price = tk.Label(
            self, 
            text=f'Total harga: {self.total_price}', 
            font=('Segoe UI', '12', 'bold'),
            justify=tk.LEFT
        )

        self.btn_back = tk.Button(
            self, text="Kembali", 
            width=20,
            bg="#4472C4", fg="white", 
            command=self.back_button
        )

        self.btn_ok = tk.Button(
            self, 
            text="Ok", 
            width=20,
            bg="#4472C4", fg="white", 
            command=self.ok_button
        )

        self.lbl_total_price.grid(sticky=tk.W, row=2, column=3, pady=(0, 45))
        self.btn_back.grid(row=2, column=1, pady=(40, 0))
        self.btn_ok.grid(row=2, column=2, pady=(40, 0))

    def update_order(self, event, idx: int, menu_type: str):
        """Updates the current order according to changes made
        to the Combobox in the menu table
        """
        
        cbbox = self.__cbbox_data[menu_type][idx]
        menu = self.__menu[menu_type][idx]
        menu_name = menu.get_name()
        menu_price = menu.get_price()
        amount = cbbox.get()
        amount = int(amount) if amount.isdigit() else 0

        cur_order_amt = self.__cur_order.get(menu_name, 0)
        added_amt = amount - cur_order_amt
        self.total_price += menu_price * added_amt
        self.__cur_order[menu_name] = amount

        # Updates the total price dynamically
        print(self.__dir__())
        self.lbl_total_price['text'] = f'Total harga: {self.total_price}'

    def update_cbbox_val(self, var, index, mode, idx: int, menu_type: str):
        """Updates the Combobox so that it can take the customer's own input
        that is not the default values (0-10)
        """
        
        cbbox = self.__cbbox_data[menu_type][idx]
        str_var = self.__str_var[menu_type][idx]
        cbbox['values'] += (str_var.get(),)
        self.update_order(None, idx, menu_type)

    def back_button(self):
        self.destroy()
        NameScreen(self.__menu, self.__table, self.master)

    def ok_button(self):
        self.cur_table = self.__table_info[self.__table_num]
        if len(self.__cur_order) != 0:
            # Updates the table if the customer ordered 
            # at least 1 item
            self.cur_table['name'] = self.__cust_name
            self.cur_table['order'] = self.__cur_order
            self.cur_table['total'] = self.total_price

        # print(self.__table_info)
        self.destroy()

    def change_table(self):
        ChooseTableScreen(self.__menu, self.__table,
                          self.__cust_name, self.__table_num, master=self)


class ChooseTableScreen(tk.Toplevel):
    def __init__(
            self, 
            menu: dict, 
            table: Table, 
            name: str = None, 
            table_num: int = None, 
            finish: bool = False, 
            master=None):

        super().__init__(master)
        self.geometry("300x400")
        self.__menu = menu
        self.__table = table
        self.__table_info = self.__table.get_table_info()
        self.__cust_name = name
        self.__cur_table_num = table_num
        self.__finish = finish
        self.create_widgets()

    def create_widgets(self):
        cur_row = 0
        BTN_OPT = {
            'empty': ['gray', 'normal' if not self.__finish else 'disabled'],
            'filled': ['red', 'disabled' if not self.__finish else 'normal'],
            'own': ['#4472C4', 'disabled']
        }

        prompt_text = "Silahkan klik meja kosong yang diinginkan:"
        if self.__finish:
            prompt_text = "Silahkan klik meja yang selesai digunakan:"

        self.lbl_prompt = tk.Label(self, text=prompt_text)
        self.lbl_prompt.grid(row=0, column=0, columnspan=2, padx=30)

        self.btn_frame = tk.Frame(self)
        for num in self.__table_info:
            btn_color, btn_state = BTN_OPT['empty']
            if (not self.__finish and 
                    num == self.__cur_table_num):
                    
                btn_color, btn_state = BTN_OPT['own']
                
            elif len(self.__table_info[num]) != 0:
                btn_color, btn_state = BTN_OPT['filled']

            btn_table = tk.Button(
                self.btn_frame,
                text=num,
                width=8,
                bg=btn_color, fg="white",
                state=btn_state,
                command=lambda table_num=num: self.set_table_num(table_num)
            )

            if num < 5:
                btn_table.grid(row=cur_row, column=0, padx=(0, 5), pady=10)

            else:
                btn_table.grid(row=cur_row-5, column=1, padx=(5, 0), pady=10)
            
            cur_row += 1

        self.btn_frame.grid(row=1, column=0, columnspan=2)

        self.lbl_info = tk.Label(
            self, 
            text="Info", 
            font=('Segoe UI', '10', 'bold'), 
            justify=tk.LEFT
        )

        self.lbl_filled = tk.Label(
            self, 
            text="Merah: Terisi", 
            justify=tk.LEFT
        )
        
        self.lbl_empty = tk.Label(
            self, 
            text="Abu-abu: Kosong", 
            justify=tk.LEFT
        )

        self.lbl_info.grid(sticky=tk.W, row=3, column=0, padx=(20, 0))
        self.lbl_filled.grid(sticky=tk.W, row=4, column=0, padx=(20, 0))
        self.lbl_empty.grid(sticky=tk.W, row=5, column=0, padx=(20, 0))

        if not self.__finish:
            self.lbl_own = tk.Label(
                self, 
                text="Biru: Meja Anda", 
                justify=tk.LEFT
            )
            self.lbl_own.grid(sticky=tk.W, row=6, column=0, padx=(20, 0))

        self.btn_back = tk.Button(
            self, 
            text="Kembali", 
            width=20, 
            bg="#4472C4", fg="white", 
            command=self.destroy
        )
        self.btn_back.grid(row=7, column=0, columnspan=2, pady=(25, 0))

    def set_table_num(self, table_num: int):
        if not self.__finish:
            self.__table_info[self.__cur_table_num] = {}
            OrderScreen(self.__menu, self.__table, self.__cust_name, table_num)
            self.master.destroy()
        
        else:
            FinishTableScreen(self.__menu, self.__table, table_num)
            self.destroy()


class FinishTableScreen(tk.Toplevel):
    def __init__(self, menu: dict, table: Table, table_num: int, master=None):
        super().__init__(master)
        self.__menu = menu
        self.__table = table
        self.__table_info = self.__table.get_table_info()
        self.__cur_table_num = table_num
        self.__cust_name = self.__table_info[self.__cur_table_num]['name']
        self.__cur_order = self.__table_info[self.__cur_table_num]['order']
        self.__total = self.__table_info[self.__cur_table_num]['total']

        self.geometry('700x400')
        self.protocol('WM_DELETE_WINDOW', self.back_button)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_name = tk.Label(
            self, 
            text=f'Nama pemesan: {self.__cust_name}'
        )
        self.lbl_name.grid(row=0, column=0, padx=(20, 0), pady=(0, 40))

        self.__table.generate_menu_table(
            root=self, 
            finish=True, 
            order=self.__cur_order
        )

        self.lbl_tab_num = tk.Label(
            self, 
            text=f'No Meja: {self.__cur_table_num}'
        )
        self.lbl_tab_num.grid(row=0, column=2, padx=(140, 0), pady=(0, 40))

        self.lbl_total_price = tk.Label(
            self, 
            text=f'Total harga: {self.__total}', 
            font=('Segoe UI', '12', 'bold'),
            justify=tk.LEFT
        )

        self.btn_back = tk.Button(
            self, 
            text="Kembali", 
            width=20, bg="#4472C4", fg="white", 
            command=self.back_button
        )

        self.btn_finish = tk.Button(
            self, 
            text="Selesai Gunakan Meja",
            width=20, 
            bg="#4472C4", fg="white", 
            command=self.finish_button
        )

        self.lbl_total_price.grid(sticky=tk.W, row=2, column=3, pady=(0, 45))
        self.btn_back.grid(row=2, column=1, pady=(40, 0))
        self.btn_finish.grid(row=2, column=2, pady=(40, 0))

    def back_button(self):
        self.destroy()
        ChooseTableScreen(self.__menu, self.__table,
                          finish=True, master=self.master)

    def finish_button(self):
        self.__table_info[self.__cur_table_num] = {}
        self.destroy()
        ChooseTableScreen(self.__menu, self.__table,
                          finish=True, master=self.master)


if __name__ == '__main__':
    menu = {
        'MEALS': [],
        'DRINKS': [],
        'SIDES': []
    }

    try:
        with open('menu.txt') as f:
            """menu.txt:
                ===MEALS
                M01;Thai Beef Salad;52000;1
                M02;Beef Korean Noodle;56000;3
                ===DRINKS
                D01;Green Smoothies;25000;2
                D02;Golden Glow;30000;4
                ===SIDES
                T01;Soft Boiled Egg;10000;1
                T02;Edamame;10000;3
            """
            cur_type = ''
            for line in f:
                if line.startswith('==='):
                    cur_type = line.strip()[3:]

                elif line.strip() != '':
                    code, name, price, extra_info = line.strip().split(';')
                    if cur_type == "MEALS":
                        menu['MEALS'].append(
                            Meals(code, name, int(price), int(extra_info)))

                    elif cur_type == "DRINKS":
                        menu['DRINKS'].append(
                            Drinks(code, name, int(price), int(extra_info)))

                    else:
                        menu['SIDES'].append(
                            Sides(code, name, int(price), int(extra_info)))

        table = Table(menu)
        app = Main(menu, table)
        app.master.mainloop()
    
    except FileNotFoundError:
        print("menu.txt not found!")
