class Plant:
    def __init__(self, name, height, days_age, growth_height):
        self.name = name
        self.height = height
        self.days_age = days_age
        self.growth_height = growth_height

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days_age} days old")

    def grow(self):
        self.height += self.growth_height

    def age(self):
        self.days_age += 1


def main():
    rose = Plant("Rose", 25.0, 30, 0.8)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()
    total_height = rose.height - initial_height
    print(f"Growth this week: {round(total_height)}cm")


if __name__ == "__main__":
    main()
