# Topic: Lists, Tuples, Sets, Dictionaries

def get_input():
    """Gets students' identities from the user and returns it
    in a dictionary format
    """
    
    data = {}
    print("Masukkan identitas mahasiswa:")
    identity = input()
    while identity != "STOP":
        parts = identity.split()   # Splits the input string by whitespace
        name = parts[0]            # The student's name is the 1st item
        npm = parts[1]             # The student's number is the 2nd item
        birth_month = parts[4]     # The student's birth month is the 5th item

        # Checks if the month already exists
        if birth_month not in data:
            data[birth_month] = {'name': set(), 'npm': set()}
        
        # Checks if the student's name already exist, case insenstive
        if name.lower() not in data[birth_month]['name']:
            data[birth_month]['name'].add(name.lower())
        
        # Checks if the student's number already exist
        if npm not in data[birth_month]['npm']:
            data[birth_month]['npm'].add(npm)

        identity = input()
    
    return data


def get_student(data: dict):
    """Prints the students' name and number to the console
    if it matches the birth month the user inputted
    Does not return anything
    """

    month = input("\nCari mahasiswa berdasarkan bulan: ")
    while month != "STOP":
        print("================= Hasil ================")
        if month in data:
            name_lst = [name for name in data[month]['name']]
            npm_lst = [npm for npm in data[month]['npm']]

            print(f'Terdapat {len(name_lst)} nama yang lahir di bulan {month}:')
            for name in name_lst:
                print(f'- {name.capitalize()}')
            print()
            
            print(f'Terdapat {len(npm_lst)} NPM yang lahir di bulan {month}:')
            for npm in npm_lst:
                print(f'- {npm}')
            print()
            
        elif month != "STOP":
            print(f'Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {month}\n')
        
        month = input("Cari mahasiswa berdasarkan bulan: ")
    

if __name__ == '__main__':
    print("Selamat datang di program Mengenal Angkatan!\n"
          f"{'=' * 43}")
    data = get_input()
    get_student(data)

    print("\nTerima kasih telah menggunakan program ini, semangat PMB-nya!")