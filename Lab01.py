# Name: Juan Maxwell Tanaya
# NPM : 2206820352

import math as m

# Constants
PAPER_PRICE_PER_CENTIMETER_SQUARED = 0.40

# Functions to make calculate area of several shapes and total price
def area_half_circle(radius: float):
    radius /= 2
    area = (m.pi * radius * radius)/2
    return area

def area_square(length: float):
    length *= length
    return length

def area_trapezoid(bot_length: float, top_length: float):
    top_plus_bot = bot_length + top_length
    height = top_length
    area = (top_plus_bot * height)/2
    return area

def area_triangle(height: float):
    bot_length = height
    area = (bot_length * height)/2
    return area

def price(total_area: float):
    total_price = m.ceil((total_area * PAPER_PRICE_PER_CENTIMETER_SQUARED)/1000) * 1000
    return total_price

# Only run the script if the file is run directly
if __name__ == "__main__":
    while True:
        name = input("Name: ")
        square_length = input("Square length in centimeters: ")
        trapezoid_length = input("Trapezoid length in centimeters: ")
        nametag_amount = input("Nametag amount: ")

        try:
            name = str(name)
            square_length = float(square_length)
            trapezoid_length = float(trapezoid_length)
            nametag_amount = int(nametag_amount)
        
        except ValueError:
            print("Incorrect value!\nPlease make sure you enter the correct value for each question.\n\n")
        
        else:
            if square_length <= 0 or trapezoid_length <= 0 or nametag_amount <= 0:
                print("Please make sure the number you input is not zero.\n\n")
            
            else:
                single_area = area_half_circle(square_length) + area_square(square_length) \
                            + area_trapezoid(trapezoid_length, square_length) + area_triangle(square_length)

                total_area = nametag_amount * single_area
                
                print(f'\n\nHello, {name}! Here are the information regarding your nametag:\n')
                print(f'Area of 1 nametag: {round(single_area, 2)} cm^2')
                print(f'Total area of all nametag: {round(total_area, 2)} cm^2')
                print(f'Money needed: Rp{price(total_area)}')
                