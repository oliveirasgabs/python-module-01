class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._days_age = days_age if days_age >= 0 else 0
        print(f"Plant created: {self._name}: {round(self._height, 1)}cm, "
              f"{self._days_age} days old")

    def show(self) -> None:
        print(f"Current state: {self._name}: {round(self._height, 1)}cm, "
              f"{self._days_age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days_age = new_age
            print(f"Age updated: {self._days_age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_age


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("")
    rose.set_height(25.0)
    rose.set_age(30)
    print("")
    rose.set_height(-5.0)
    rose.set_age(-10)
    print("")
    rose.show()


if __name__ == "__main__":
    main()
