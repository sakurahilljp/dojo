# -*- coding: utf-8 -*-

import sys

def message(msg):
    print msg
    sys.stdout.flush()


class Recipe(object):
    def brew(self): 
        raise NotImplementedError('this method must be provided.')
    def decorate(self):
        raise NotImplementedError('this method must be provided.')
    
class DrinkMaker(object):
    def __init__(self, recipe):
        self.recipe = recipe
        
    def prepare(self):
        message('Starts to prepare a drink for you....')
        self.__boil_water()
        self.__pour_drink()
        message('Here you are!!\n')

    def __boil_water(self):
        message('* Boil water.')
        self.recipe.brew()
        
    def __pour_drink(self):
        message('* Pour drink to a cup.')
        self.recipe.decorate()

class CoffeeRecipe(Recipe):
    def brew(self):
        message('* Drip coffee with filter.')
    def decorate(self):
        message('Do you want milk ? [y/n]')
        if raw_input('>').upper().startswith('Y'):
            message('* Milk is added.')

class TeaRecipe(Recipe):
    def brew(self):
        message('* Put tea pack into boiled water.')
    def decorate(self):
        message('Do you want lemon ? [y/n]')
        if raw_input('>').upper().startswith('Y'):
            message('* Sliced lemon is added.')
        
if __name__ == '__main__':

    DrinkMaker(CoffeeRecipe()).prepare()
    DrinkMaker(TeaRecipe()).prepare()
    DrinkMaker('Cocoa').prepare()
