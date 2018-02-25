class Animals():
    color = "Black"
    size = "Large"
    noise = "Grunts"
    def makes_noise(self):
        return self.noise
class Dog(Animals):
    name = "Champ"
    color = "Golden"
    noise = "Barks"
    def makes_noise(self):
        return self.noise

an = Animals()
print(an.color)
print(an.size)
print(an.noise)
print(an.makes_noise())

dog = Dog()
print(dog.name)
print(dog.color)
print(dog.noise)
print(dog.makes_noise())

