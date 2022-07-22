class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def Animal_details(self):
        print("The name is ", self.name, "The sound is ", self.sound)

class Dog(Animal):
    def __init__(self, name, sound, family):
        self.family = family
        super().__init__(name, sound)

    def Animal_details(self):
        print("The name is ", self.name, "The sound is ", self.sound, "The family is ", self.family )


class Sheep(Animal):
    def __init__(self, name, sound, color):
        self.color = color
        super().__init__(name, sound)
    def Animal_details(self):
        print("The name is ", self.name, "The sound is ", self.sound, "The color is ", self.color)


d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()     