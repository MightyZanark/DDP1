# Name: Juan Maxwell Tanaya
# NPM : 2206820352

if __name__ == '__main__':
    print("Selamat datang di Pacil Mart!")
    filename = input("\nMasukkan nama file input: ")

    try:
        # Try opening the file and throws a FileNotFoundError if
        # said file does not exist
        with open(filename) as f:
            if not f.read().strip(): # Checks if file is empty
                print("\nFile input kosong")
            
            else:
                # Reset file reading to the beginning of the file
                # Otherwise there will be no output
                f.seek(0)

                # Formats the printed string
                # < means left aligned, > means right aligned
                # The number after those symbols are the amount of space
                # the words before the semicolon (:) reserve
                print("\nBerikut adalah daftar belanjaanmu:\n\n" +
                     f"{'Nama Barang':<12}|{'Jumlah':>8}|{'Kembalian':>10}\n" +
                      "---------------------------------")
                
                for lines in f:
                    # Tokenize the lines read and sets them to a variable
                    parts = lines.strip().split()
                    item_name = parts[0]
                    alloc_money = int(parts[1])
                    cost_per_item = int(parts[2])
                    
                    # Item amount is the amount of items that can be bought
                    # with the allocated money
                    # Spare money is the amount of money left after buying
                    # item_amount of said item
                    item_amount = alloc_money // cost_per_item
                    spare_money = alloc_money - cost_per_item * item_amount
                    
                    print(f'{item_name:<12}|{item_amount:>8}|{spare_money:>10}')
            
                print("\nTerima kasih sudah belanja di Pacil Mart!")
    
    # Tells the user that the file doesn't exist and exits the program
    except FileNotFoundError:
        print("File tidak tersedia")
