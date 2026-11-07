class HealthPotion:
    def use(self):
        print("You regain 50 HP!")


class ManaPotion:
    def use(self):
        print("You restore 30 MP!")


class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")


def apply_item(item):
    item.use()


if __name__ == "__main__":
    potions = [
        HealthPotion(),
        ManaPotion(),
        SpeedBoost()
    ]

    for item in potions:
        apply_item(item)
