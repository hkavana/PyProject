class Animals():
    color = "Black"
    size = "Large"
    noise = "Grunts"
    def get_color(self,color):
        return self.color + " " + color
    def makes_noise(self):
        return self.noise
class Dog(Animals):
    name = "Champ"
    color = "Golden"
    noise = "Barks"
    @property
    def makes_noise(self):
        return self.noise

an = Animals()
print(an.color)
print(an.size)
print(an.noise)
print(an.get_color("White"))
print(an.makes_noise())

dog = Dog()
print(dog.name)
print(dog.color)
print(dog.noise)
print(dog.get_color("Brown"))
print(dog.makes_noise))

