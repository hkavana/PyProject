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
an.color
an.size
an.noise
an.makes_noise()

dog = Dog()
dog.name
dog.color
dog.noise
dog.makes_noise()
:
