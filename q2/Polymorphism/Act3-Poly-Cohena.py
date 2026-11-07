class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")


class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")


class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")


def perform_move(character):
    character.special_move()


if __name__ == "__main__":
    characters = [
        Warrior(),
        Mage(),
        Archer()
    ]

    for char in characters:
        perform_move(char)