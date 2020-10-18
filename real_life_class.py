class Animal:

    def __init__(self, species, name, weight):
        self.species = species
        self.name = name
        self. weight = weight

    def speak(self):
        print("Grunt")


zephyr = Animal("Cat", "Zephyr", "14.5 lbs")
henry = Animal("Cat", "Henry", "9 lbs")

zephyr.speak()
