class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name
        self.height = height
        self.days_age = days_age

    def grow(self, growth_rate: int) -> None:
        self.height += growth_rate

    def age(self, days: int) -> None:
        self.days_age += days

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.days_age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, days_age: int,
                 color: str) -> None:
        super().__init__(name, height, days_age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet.")


class Tree(Plant):
    def __init__(self, name: str, height: float, days_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide."
              )

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days_age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, days_age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def increase_nutritional(self, value: int) -> None:
        self.nutritional_value += value
        self.age(value)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.increase_nutritional(20)
    tomato.show()


if __name__ == "__main__":
    main()
