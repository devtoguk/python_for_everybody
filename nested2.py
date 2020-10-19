def dog():

    def speak():
        return "woof woof!"

    return speak


woof = dog()

text = woof()

print(text)
