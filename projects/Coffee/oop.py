# object is when you call a class into an object that you can use
# class is the blueprint for an object
# create an object with a class (general form)
# attributes are not callable. They are pieces of an object that you can access and modify with =

# import turtle
#
# Turt = turtle.Turtle()
# print(Turt)
# turtle.shape('turtle') # make it a turtle icon
# turtle.color('DeepPink4')
# turtle.fd(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight) #same as pd -- access attributes with .xyz syntax
# my_screen.exitonclick()

# method is a function that is associated with an object (ie. front_is_clear in Karel)

# from prettytable import PrettyTable
# # parenthesis constructs the object
# # commdP for parameters
# table = PrettyTable()
# table.add_column('Poke Name',['Pikachu','Charmander','Squirtle'])
# table.add_column('Type',['Electric','Water','Fire'])
#
# table.align = 'l'
# print(table)

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()

coffee_maker = CoffeeMaker()
coffee_maker.report()
#coffee_maker.is_resource_sufficient(coffee)

menu = Menu()

while True:
    options = menu.get_items()
    coffee = input(f'What would you like: {options}').lower().strip()
    if coffee in ('report'):
        coffee_maker.report()
        money_machine.report()
    if coffee in ('off'):
        print('Goodbye')
        quit()
    else:
        drink = menu.find_drink(coffee)
        ingredients_check = coffee_maker.is_resource_sufficient(drink)
        payment_check = money_machine.make_payment(drink.cost)
        if ingredients_check and payment_check:
            coffee_maker.make_coffee(drink)