class Plant:
	def __init__(self, name: str, height: float, days_age: int) -> None:
		self._name = name
		self._height = height
		self._days_age = days_age

	def grow(self, growth_rate: int) -> None:
		self._height += growth_rate

	def age(self) -> None:
		self._days_age += 1

	def show(self) -> None:
		print(f"{self._name}: {round(self._height, 1)}cm, "
			  f"{self._days_age} days old")


class Flower(Plant):
	def __init__(self, name: str, height: float, days_age: int,
				 color: str) -> None:
		super().__init__(name, height, days_age)
		self._color = color
		self._is_blooming = False

	def bloom(self) -> None:
		self._is_blooming = True

	def show(self) -> None:
		super().show()
		print(f"Color: {self._color}")
		if self._is_blooming:
			print(f"{self._name} is blooming beautifully!")
		else:
			print(f"{self._name} has not bloomed yet.")


class Tree(Plant):
	def __init__(self, name: str, height: float, days_age: int,
				 trunk_diameter: float) -> None:
		super().__init__(name, height, days_age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self) -> None:
		print(f"{self._name} now produces a shade of "
			  f"{round(self._height, 1)}cm long and "
			  f"{round(self.trunk_diameter, 1)}cm wide."
			  )

	def show(self) -> None:
		super().show()
		print(f"Trunk Diameter: {self.trunk_diameter, 1}cm")


class Vegetable(plant):
	def __init__(self, name: str, height: float, days_age: int,
				 harvest_season: str) -> None:
		super().__init__(name, height, days_age)
		self.harvest_season = harvest_season
		self.nutritional_value = 0

	def harvest(self) -> None:
		if self._is_edible:
			print(f"{self._name} is ready to be harvested!")
		else:
			print(f"{self._name} is not edible and cannot be harvested.")
