# Simple Dec to Octal converter

if __name__ == '__main__':
    print("Selamat Datang di Bunker Hacker!\n")

    # Gets how many conversion the user wants
    conversion_amount = int(input("Masukkan berapa kali konversi "
                                  "yang ingin dilakukan: "))

    for i in range(conversion_amount):

        # Gets the number the user wants to convert to Octal
        the_number = int(input(f'\nMasukkan angka ke-{i+1} yang ingin dikonversikan '
                                '(dalam desimal): '))
        conversion_result = ''
        
        # Conversion is done by using the modulus operator on the number
        # All of the modulus results is then concatenated to a result variable
        # and the current number is updated by floor divisioning it by 8
        while the_number != 0:
            conversion_result += str(the_number % 8)
            the_number //= 8

        # Conversion result is reversed first so its correct and then printed 
        # to stdout
        print(f'Hasil konversi desimal ke basis 8: {conversion_result[::-1]}')

    print("\nTerimakasih telah menggunakan Bunker Hacker!")
