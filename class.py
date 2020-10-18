class MyClassName:

    def __init__(self, name="Person", hobby="coding"):
        self.name = name
        self.hobby = hobby

    def say_hello(self):
        print("Hello to", self.name)

    def get_hobby(self):
        print(f"{self.name}'s hobby is {self.hobby}")


person = MyClassName(name="Henry", hobby="Being fed")

person.say_hello()

person.get_hobby()
