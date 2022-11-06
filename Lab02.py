# Simple Holiday Tracker to find where is the best place the user visited
# and the overall rating of the holiday

def happiness_scale(overall_rating: float):
    """Prints a comment based on overall rating"""

    if 8 <= overall_rating <= 10:
        print("Dek Depe bahagia karena pengalamannya menyenangkan.")
    elif 5 <= overall_rating:
        print("Dek Depe senang karena pengalamannya cukup baik.")
    else:
        print("Dek Depe sedih karena pengalamannya buruk.")


def get_highest_and_overall_rating(total_place: int):
    """Gets the place with the highest rating and gets the overall rating
    of the trip
    """
    
    i = 1
    total_rating = 0
    highest_rating = 0
    highest_rating_place = ''
    
    # Loop to find the place with the highest rating
    while i <= total_place:
        holiday_place = input(f'\nPerjalanan {i}: ')
        holiday_rating = int(input(f'Rating perjalanan kamu ke {holiday_place} (indeks 1-10): '))
        total_rating += holiday_rating

        if highest_rating <= holiday_rating:
            highest_rating = holiday_rating
            highest_rating_place = holiday_place
        
        i += 1
    
    overall_rating = round(total_rating / total_place, 2)
    return [highest_rating_place, overall_rating]


if __name__ == '__main__':
    print("Selamat datang ke Dek Depe Holiday Tracker!\n")
    
    # Validity test for number of place visited, cannot be negative or 0
    while True:
        total_places = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
        if total_places > 0:
            break
        print("Input tidak valid. Silahkan masukkan input kembali!")
    
    summary_list = get_highest_and_overall_rating(total_places)
    print("\n\n---Summary---")
    print(f'Perjalanan paling mengesankan adalah ketika pergi ke {summary_list[0]}.')
    print(f'Skala kebahagiaan Dek Depe adalah {summary_list[1]:.2f}')
    happiness_scale(summary_list[1])
    print("\nTerimakasih telah menggunakan Dek Depe Holiday Tracker!")
