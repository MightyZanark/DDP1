import re
import locale
import os
from time import strftime, localtime, sleep

locale.setlocale(locale.LC_ALL, 'id')

def get_menu(filepath: str):
    """Gets all of the items of a menu from a .txt file
    Also checks the .txt file format and the content
    If the format and content are valid, then returns the menu
    Else raises a ValueError which stops the program

    Returns a total of 3 types of the menu, all of them as a dict
    menu         : Used for printing the menu
    menu_by_name : Used for checking the availability of a menu by their name
    menu_by_code : Used for checking the availability of a menu by their code
    """
    
    # Checks if file exist and if its empty
    if not os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
        raise ValueError

    menu = {}
    menu_by_name = {}
    menu_by_code = {}
    name_code_set = set()
    with open(filepath) as f:
        cur_type = ''
        for lines in f:
            if re.search('^===\w+?$', lines, re.ASCII):
                menu_type = lines.strip().split('===')[-1]
                if menu_type not in menu:
                    menu[menu_type] = {}
                cur_type = menu_type

            elif re.search('^\w(\w|\s)+?;(\w|\s)*?;[0-9]+?', lines, re.ASCII):
                menu_code, menu_name, menu_price = lines.strip().split(';')
                if menu_name in name_code_set or menu_code in name_code_set:
                    raise ValueError
                
                menu[cur_type][(menu_name, menu_code)] = int(menu_price)
                
                menu_by_name[menu_name] = {
                    'code': menu_code, 
                    'price': int(menu_price)
                }
                
                menu_by_code[menu_code] = {
                    'name': menu_name, 
                    'price': int(menu_price)
                }
                
                name_code_set.add(menu_name)
                name_code_set.add(menu_code)

            elif lines.strip() == '':
                continue

            else:
                raise ValueError

    return menu, menu_by_name, menu_by_code


def is_menu_name_valid(menu_name: str, menu_by_name: dict, menu_by_code: dict):
    """Checks if the menu_name is valid or not"""

    if menu_name in menu_by_name or menu_name in menu_by_code:
        return True

    return print(f'Menu {menu_name} tidak ditemukan! ', end='')


def is_order_valid(menu_name: str, orders: dict, menu_by_name: dict, menu_by_code: dict):
    """Checks if the menu_name is valid and is in orders"""

    if is_menu_name_valid(menu_name, menu_by_name, menu_by_code):
        menu_name = convert_menu_name(menu_name, menu_by_code)
        if menu_name in orders:
            return True

    return print(f'Menu {menu_name} tidak Anda pesan sebelumnya! ', end='')


def is_table_valid(table: dict, table_number: str):
    """Checks if the table_number is valid and exists"""

    if table_number.isdecimal() and int(table_number) in table:
        return True
        
    return print("Nomor meja kosong atau tidak sesuai!")


def convert_menu_name(menu_name: str, menu_by_type: dict):
    """Normalize menu_name from code to name or vice versa"""

    if menu_name in menu_by_type:
        try:
            menu_name = menu_by_type[menu_name]['name']
        except KeyError:
            menu_name = menu_by_type[menu_name]['code']

    return menu_name


def localize_price(price: int):
    """Gets a localized version of price (thousands separated)
    Ex: 10000 (int) is converted to 10.000 (str)
    """
    
    return locale.format_string('%d', price, grouping=True)


def print_menu(menu: dict):
    """Prints the menu for the customer to see"""

    print("\nBerikut ini adalah menu yang kami sediakan:")
    for menu_type in menu:
        print(f'{menu_type}:')
        for name, code in menu[menu_type]:
            price = localize_price(menu[menu_type][(name, code)])
            print(f'{code} {name}, Rp{price}')


def print_cur_order(orders: dict, menu_by_name: dict, total: bool = False):
    """Prints the customer's current order
    Total price is not printed by default, but can be printed if needed by
    specifying the total parameter to True
    """

    total_price = 0
    for order in orders:
        price = menu_by_name[order]['price']
        amount = orders[order]
        total_price += price * amount
        price_str = localize_price(price * amount)
        print(f'{order} {amount} buah, total Rp{price_str}')
    
    if total:
        total_price = localize_price(total_price)
        print(f'\nTotal pesanan: Rp{total_price}')


def create_order(menu: dict, menu_by_name: dict, menu_by_code: dict, table: dict):
    """Creates an order and puts said order and the customer's name in the table dict"""

    if len(table) == 10:
        return print("Mohon maaf meja sudah penuh, silahkan kembali lagi nanti.")
    
    name = input("Siapa nama Anda? ")
    while name.strip() == "":
        print("Nama tidak boleh kosong!")
        name = input("Siapa nama Anda? ")

    print_menu(menu)

    orders = {}
    order = input("\nMasukkan menu yang ingin Anda pesan: ")
    while order != "SELESAI":
        if is_menu_name_valid(order, menu_by_name, menu_by_code):
            order = convert_menu_name(order, menu_by_code)
            orders[order] = orders.get(order, 0) + 1
            print(f'Berhasil memesan {order}. ', end='')

        order = input("Masukkan menu yang ingin Anda pesan: ")

    print("\nBerikut adalah pesanan Anda:")
    print_cur_order(orders, menu_by_name, total=True)

    for i in range(1, 11):
        if i not in table:
            table[i] = {'name': name, 'orders': orders}
            print(f'Pesanan akan kami proses, Anda bisa menggunakan meja nomor {i}. '
                   'Terima kasih.')
            sleep(1)
            return


def change_order(menu: dict, menu_by_name: dict, menu_by_code: dict, table: dict):
    """Changes the customer's order by changing the amount of an order, deleting it,
    or adding to it, depending on which option the customer picks
    """
    
    table_number = input("Nomor meja berapa? ")
    if not is_table_valid(table, table_number):
        return

    table_number = int(table_number)
    orders = table[table_number]['orders']
    print_menu(menu)
    print("\nBerikut adalah pesanan Anda:")
    print_cur_order(orders, menu_by_name)

    cmd = input("\nApakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
    while cmd != "SELESAI":
        if cmd == "GANTI JUMLAH":
            # Changes the customer's order amount to a new amount that
            # the customer specified
            menu_name = input("Menu apa yang ingin Anda ganti jumlahnya: ")
            if is_order_valid(menu_name, orders, menu_by_name, menu_by_code):
                new_amt = input("Masukkan jumlah pesanan yang baru: ")
                if not new_amt.isdecimal() or int(new_amt) <= 0:
                    print("Jumlah harus bilangan positif. ", end='')
                else:
                    menu_name = convert_menu_name(menu_name, menu_by_code)
                    orders[menu_name] = int(new_amt)

        elif cmd == "HAPUS":
            # Removes an order the customer specified
            menu_name = input("Menu apa yang ingin Anda hapus dari pesanan: ")
            if is_order_valid(menu_name, orders, menu_by_name, menu_by_code):
                menu_name = convert_menu_name(menu_name, menu_by_code)
                amt = orders[menu_name]
                print(f'{amt} buah {menu_name} dihapus dari pesanan. ', end='')
                del orders[menu_name]

        elif cmd == "TAMBAH PESANAN":
            # Adds an order the customer specified
            menu_name = input("Menu apa yang ingin Anda pesan: ")
            if is_menu_name_valid(menu_name, menu_by_name, menu_by_code):
                menu_name = convert_menu_name(menu_name, menu_by_code)
                orders[menu_name] = orders.get(menu_name, 0) + 1
                print(f'Berhasil memesan {menu_name}. ', end='')

        else:
            print(f'Fitur {cmd} tidak tersedia. ', end='')

        cmd = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

    print("\nBerikut adalah pesanan terbaru Anda:")
    print_cur_order(orders, menu_by_name, total=True)
    sleep(1)


def finish_order(table: dict, menu_by_name: dict):
    """Function used when the customer is done using the table
    
    If the customer ordered at least 1 item, writes the orders 
    details and total price on a receipt .txt file and then frees 
    the table for other customers to use
    Else no receipt is generated
    """

    table_number = input("Nomor meja berapa? ")
    if not is_table_valid(table, table_number):
        return

    table_number = int(table_number)
    cust_name = table[table_number]['name']
    orders = table[table_number]['orders']
    
    if len(orders) != 0:
        print(f'Pelanggan atas nama {cust_name} selesai menggunakan meja {table_number}.')
        cur_time = strftime('%d-%m-%Y_%H-%M-%S', localtime())
        with open(f'receipt_{cust_name}_{cur_time}.txt', 'w') as r:
            total_price = 0
            for order in orders:
                menu_code = convert_menu_name(order, menu_by_name)
                price = menu_by_name[order]['price']
                amt = orders[order]
                total_price += price * amt
                r.write(f'{menu_code};{order};{amt};{price};{price * amt}\n')
            r.write(f'\nTotal {total_price}')

    else:
        print(f'Pelanggan atas nama {cust_name} tidak jadi makan.')

    del table[table_number]
    sleep(1)


def main():
    try:
        menu, menu_by_name, menu_by_code = get_menu('menu.txt')
        """menu.txt:
            ===MEALS
            M01;Thai Beef Salad;52000
            M02;Beef Korean Noodle;56000
            ===DRINKS
            D01;Green Smoothies;25000
            D02;Golden Glow;30000
            ===SIDES
            T01;Soft Boiled Egg;10000
            T02;Edamame;10000
        """
        
        print("Selamat datang di Kafe Daun Daun Pacilkom")
        cmd = input("Apa yang ingin Anda lakukan? ")
        table = {}
        while cmd != "SELESAI":
            if cmd == 'BUAT PESANAN':
                create_order(menu, menu_by_name, menu_by_code, table)
            
            elif cmd == 'UBAH PESANAN':
                change_order(menu, menu_by_name, menu_by_code, table)
            
            elif cmd == 'SELESAI MENGGUNAKAN MEJA':
                finish_order(table, menu_by_name)
            
            else:
                print(f'Fitur {cmd} tidak tersedia.')
                sleep(0.2)

            print('\n---')
            print("Selamat datang di Kafe Daun Daun Pacilkom")
            cmd = input("Apa yang ingin Anda lakukan? ")

    except ValueError:
        print("Daftar menu tidak valid, cek kembali menu.txt!")

    except Exception as e:
        print(f"Unexpected exception: {e}")

if __name__ == '__main__':
    main()