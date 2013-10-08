
# abstract class for Beverage
class BeverageBase(object):
    def get_description(self):
        raise 0, "Must be implemented"

    def get_cost(self):
        raise 0, "Must be implemented"

# Concrete Beverage
class Beverage(BeverageBase):
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend"
        self.cost = 0.89

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast"
        self.cost = 0.99

class Decafe(Beverage):
    def __init__(self):
        self.description = "Decafe"
        self.cost = 1.05

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
        self.cost = 1.99

# Decorator
class CondimentDecorator(BeverageBase):
    def __init__(self, beverage):
        self.beverage = beverage
     
    def get_description(self):
        return self.description + " " + self.beverage.get_description()
    
    def get_cost(self):
        return self.cost + self.beverage.get_cost()

class Milk(CondimentDecorator):
    def __init__(self, beverage):
        CondimentDecorator.__init__(self, beverage);
        self.description = "Milk"
        self.cost = 0.1

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = "Mocha"
        self.cost = 0.2

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = "Whip"
        self.cost = 0.10

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = "Soy"
        self.cost = 0.15

if __name__ == '__main__':
    
    def print_order(order):
        print "Your order is;"
        print "  description:", order.get_description()
        print "  cost:", order.get_cost()
        print ""

    # House Blend
    print_order(HouseBlend())

    # House Blend with Milk and Mocha
    print_order(Mocha(Milk(HouseBlend())))

    # Dark Roast with double Mocha and Whip
    print_order(Whip(Mocha(Mocha(DarkRoast()))))

    # House Blend with Soy, Mocha and Whip
    print_order(Whip(Soy(Mocha(HouseBlend()))))
    
