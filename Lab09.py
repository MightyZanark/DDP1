# Topic: Classes, Objects, and Inheritance

from random import randint


class Entity():
    def __init__(self, name: str, hp: int, atk: int):
        self.__name = name
        self.__hp = hp
        self.__atk = atk

    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp: int):
        self.__hp = hp

    def attack(self, other):
        damage = other.take_damage(self.get_atk())
        return damage

    def take_damage(self, damage: int):
        hp = self.get_hp()
        self.set_hp(hp - damage)
        return damage

    def is_alive(self):
        return self.__hp > 0

    def __str__(self):
        return self.get_name()


class Player(Entity):
    def __init__(self, name: str, hp: int, atk: int, defense: int):
        super().__init__(name, hp, atk)
        self.__defense = defense

    def get_defense(self):
        return self.__defense

    def take_damage(self, damage: int):
        """Takes damage depending on player's defense stat"""

        defense = self.get_defense()
        hp = self.get_hp()
        if damage > defense:
            damage -= defense
            self.set_hp(hp - damage)
            return damage
        return 0


class Boss(Entity):
    def __init__(self, name: str, hp: int, atk: int):
        super().__init__(name, hp, atk)

    def attack(self, other):
        """Attacks another Entity while ignoring their defense stat"""

        damage = self.get_atk()
        other_hp = other.get_hp()
        other.set_hp(other_hp - damage)
        return damage


def main():
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))
    depram = Player("Depram", 100, atk, defense)
    enemies = [
        Entity(f'Enemy {i}', randint(20, 100), randint(10, 30))
        for i in range(randint(0, 1))
    ]
    enemies.append(Boss("Ohio Final Boss", randint(20, 100), randint(10, 30)))

    print(f'Terdapat {len(enemies)} musuh yang menghadang Depram!\n'
          '------------')

    for enemy in enemies:
        print(f'{enemy} muncul!\n\n'
              '---Status---\n'
              f'{enemy.get_name():20} HP: {enemy.get_hp():<3}\n'
              f'{depram.get_name():20} HP: {depram.get_hp():<3}\n'
              '------------')
        
        while enemy.is_alive() and depram.is_alive():
            damage = depram.attack(enemy)
            print(f'{depram.get_name()} menyerang {enemy.get_name()} dengan {damage} ATK')

            # Quick check if the enemy is alive after the player's attack
            # If the enemy is dead, break out of the loop and continue to
            # the next enemy (if there's any)
            if enemy.is_alive():
                damage = enemy.attack(depram)
                print(f'{enemy.get_name()} menyerang {depram.get_name()} dengan {damage} ATK')
            
            # print(f'Current status:\n'
            #       f'{enemy.get_name():20} HP: {enemy.get_hp()}\n'
            #       f'{depram.get_name():20} HP: {depram.get_hp()}\n'
            #        '------------')

        if not depram.is_alive():
            print("------------\n\n"
                  "Tidak! Depram telah dikalahkan oleh musuhnya :(")
            return
        else:
            print(f'{enemy} telah kalah!')

        print("------------\n")

    print("Selamat! Semua musuh Depram telah kalah!")


if __name__ == '__main__':
    main()
