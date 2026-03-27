class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, days_age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._days_age: int = 0
        self.set_height(height)
        self.set_age(days_age)
        self._stats: Plant.Stats = Plant.Stats()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_age

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = value
        else:
            print("Height cannot be negative.")

    def set_age(self, value: int) -> None:
        if value >= 0:
            self._days_age = value
        else:
            print("Age cannot be negative.")

    def grow(self, growth_rate: int) -> None:
        new_height: float = self._height + growth_rate
        self.set_height(new_height)
        self._stats.increment_grow()

    def age(self, days: int) -> None:
        self.set_age(self._days_age + days)
        self._stats.increment_age()

    def show(self) -> None:
        self._stats.increment_show()
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._days_age} days old")

    @staticmethod
    def is_greater_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, days_age: int,
                 color: str) -> None:
        super().__init__(name, height, days_age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.get_name()} is blooming beautifully!")
        else:
            print(f"{self.get_name()} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, days_age: int,
                 color: str) -> None:
        super().__init__(name, height, days_age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls: int = 0

        def increment_produce_shade(self) -> None:
            self._produce_shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._produce_shade_calls} shade")

    def __init__(self, name: str, height: float, days_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days_age)
        self.trunk_diameter: float = trunk_diameter
        self._stats: Tree.TreeStats = Tree.TreeStats()

    def produce_shade(self) -> None:
        self._stats.increment_produce_shade()
        print(f"Tree {self.get_name()} now produces a shade of "
              f"{round(self.get_height(), 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant._stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_greater_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_greater_than_a_year(400)}")

    print("\n=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous: Plant = Plant.create_anonymous_plant()
    anonymous.show()
    display_plant_stats(anonymous)


if __name__ == "__main__":
    main()
