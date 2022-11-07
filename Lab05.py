from math import pi

PRICE_PER_VOLUME = 700


def cuboid_volume(length: float, width: float, height: float):
    """Calculates and returns the cuboid volume from a given lenght,
    width, and height

    Args:
    length -- Guaranteed to be a positive value
    width  -- Guaranteed to be a positive value
    height -- Guaranteed to be a positive value

    Returns:
    volume -- length * width * height
    """

    return (length * width * height)


def cone_volume(radius: float, height: float):
    """Calculates and returns the cone volume from a given radius and height

    Args:
    radius -- Guaranteed to be a positive value
    height -- Guaranteed to be a positive value

    Returns:
    volume -- (math.pi * radius * radius * height)/3
    """

    return ((pi * radius * radius * height)/3)


def get_cuboid_size():
    """Gets the cuboid size from the user

    length -- The lenght of the cuboid, guaranteed to be
              a positive value
    width  -- The width of the cuboid, guaranteed to be
              a positive value
    height -- The height of the cuboid, guaranteed to be
              a positive value
    """

    length = float(input("Masukkan panjang balok: "))
    width = float(input("Masukkan lebar balok: "))
    height = float(input("Masukkan tinggi balok: "))
    print()
    return length, width, height


def get_cone_size():
    """Gets the cone size from the user

    radius -- The radius of the cone, guaranteed to be
              a positive value
    height -- The height of the cone, guaranteed to be
              a positive value
    """

    radius = float(input("Masukkan jari-jari kerucut: "))
    height = float(input("Masukkan tinggi kerucut: "))
    print()
    return radius, height


def main():
    """Main program that consists of getting user inputs
    regarding the gallon's shape (BALOK or KERUCUT) or the
    sentinel value STOP to stop the program
    Balok = Cuboid
    Kerucut = Cone
    """

    print("\nSelamat datang di Depot Minuman Dek Depe!\n"
          f"{'=' * 42}")

    stop = False
    total_volume = 0
    total_price = 0

    # While loop to ask for the gallon's shape until stopped with
    # sentinel value "STOP"
    while not stop:
        gallon_shape = input("Masukkan bentuk galon yang diinginkan "
                             "(STOP untuk berhenti): ")
        gallon_shape = gallon_shape.strip()

        # While loop to validate the input
        while gallon_shape != "BALOK" and gallon_shape != "KERUCUT" \
                and gallon_shape != "STOP":
            print("Input tidak benar, masukkan kembali\n")

            gallon_shape = input("Masukkan bentuk galon yang diinginkan "
                                 "(STOP untuk berhenti): ")
            gallon_shape = gallon_shape.strip()

        if gallon_shape == "BALOK":
            length, width, height = get_cuboid_size()
            volume = cuboid_volume(length, width, height)
            total_volume += volume
            total_price += volume * PRICE_PER_VOLUME

        elif gallon_shape == "KERUCUT":
            radius, height = get_cone_size()
            volume = cone_volume(radius, height)
            total_volume += volume
            total_price += volume * PRICE_PER_VOLUME

        else:
            stop = True

    if total_volume != 0:
        print(f"\n\n{'=' * 52}\n"
              f"Total volume air yang dikeluarkan adalah: {total_volume:.2f}\n"
              f"Total harga yang harus dibayar adalah: Rp{total_price:.2f}\n"
              f"{'=' * 52}")

        print("\nTerima kasih telah menggunakan Depot Air Minum Dek Depe")

    else:
        print(f"\n\n{'=' * 52}\n"
              "Anda tidak memasukkan input satupun :(\n"
              "Terima kasih telah menggunakan Depot Air Minum Dek Depe\n"
              f"{'=' * 52}")


if __name__ == '__main__':
    main()
