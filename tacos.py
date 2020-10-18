class Food:
    # Class Interface 
    def __init__(self, starting_quantity=0, total_uncooked=10, sellable=10):
        self.starting_quantity = starting_quantity
        self.total_uncooked = total_uncooked
        self.sellable = sellable
 
    def eat(self):
        raise NotImplementedError
 
    def cook(self):
        raise NotImplementedError
 
    def sell(self):
        raise NotImplementedError
 
 
class FastFood(Food):
    # Subclass
    def eat(self):
        self.starting_quantity = self.starting_quantity - 1 
        return self.starting_quantity
 
    def cook(self):
        self.total_uncooked = self.total_uncooked - 1
        return self.total_uncooked
 
    def sell(self):
        self.sellable = self.sellable - 1 
        return self.sellable
 
class Taco(FastFood):
    # Subclass of a sublcass
    def eat(self):
        super().eat()
        super().eat()
        return self.starting_quantity
 
taco = Taco(starting_quantity=50, total_uncooked=20, sellable=20)         
taco.eat() # <- What does this return?