class PizzaStore(object):
    def order_pizza(self, name):
        print '==> You ordered "%s" pizza' % name
        pizza = self._create_pizza(name)
        if pizza is None:
            return None

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    def _create_pizza(self, name):
        raise 0, 'Must be implemented.'

class Pizza(object):
    def prepare(self):
        print self.name, ' is being prapared...'
        print 'Kneading dough ...', self.dough
        print 'Adding saurce ...', self.saurce
        print 'Adding toppings ...'
        for topping in self.toppings:
            print ' - %s' % ( topping )
    def bake(self):
        print 'Barning at 350 degree for 25 minutes....'
    def cut(self):
        print 'Cutting pizza into fan-like shapes...'
    def box(self):
        print 'Putting the whole pizza into PizzaStore official box...'

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = 'New York style Saurce and Cheeze Pizza'
        self.dough = 'Thin Crust Dough'
        self.saurce = 'Marinara Saurce'
        self.toppings = [ 'Reggiano Cheeze' ]

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'New York style Pepperoni Pizza'
        self.dough = 'Thin Crust Dough'
        self.saurce = 'Marinara Saurce'
        self.toppings = [ 'Reggiano Cheeze',
                          'Mashrooms',
                          'Onion',
                          'Red Pepper',
                          'Pepperoni' ]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = 'Chicago style Deep-Dish Cheeze Pizza'
        self.dough = 'Thick Cruft Dough'
        self.saurce = 'Plum Tomato Saurce'
        self.toppings = [ 'Cut Mozzarella Cheeze' ]
    def cut(self):
        print 'Cutting into square shapes...'

class NYPizzaStore(PizzaStore):
    def _create_pizza(self, name):
        if name == 'Cheeze':
            return NYStyleCheesePizza()
        if name == 'Pepperoni':
            return NYStylePepperoniPizza()
        return None

class ChicagoPizzaStore(PizzaStore):
    def _create_pizza(self, name):
        if name == 'Cheeze':
            return ChicagoStyleCheesePizza()
        return None



if __name__ == '__main__':
    def serve_pizza(pizza):
        if pizza is not None:
            print '==> Thank you !! Your order is ready;', pizza.name
        else:
            print '==> Your order is not available;'
        print ''

    print '------------------------------------------------------------'
    print ' Welcome to NY Pizza Store !!'
    print '------------------------------------------------------------'
    store = NYPizzaStore()
    for name in [ 'Cheeze', 'Pepperoni' ]:
        pizza = store.order_pizza(name)
        serve_pizza(pizza)

    print '------------------------------------------------------------'
    print ' Welcome to Chicago Pizza Store !!'
    print '------------------------------------------------------------'
    store = ChicagoPizzaStore()
    for name in [ 'Cheeze', 'Pepperoni' ]:
        pizza = store.order_pizza(name)
        serve_pizza(pizza)

