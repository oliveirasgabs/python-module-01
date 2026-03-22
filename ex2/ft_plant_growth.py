class Plant:
    def __init__(self, name, height, age, growth_size):
        self.name = name
        self.height = height
        self.age = age
        self.growth_size = growth_size

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += self.growth_size

    def age(self):
        self.age += 1

def main():

