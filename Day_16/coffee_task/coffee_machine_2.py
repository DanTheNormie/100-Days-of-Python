from Day_16.coffee_task.menu import Menu, MenuItem
from Day_16.coffee_task.coffee_maker import CoffeeMaker
from Day_16.coffee_task.money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True
while should_continue:
    print("Welcome to my coffee shop.")

    print(menu.get_items())

    ui = input("Please choose a beverage of your choice.")

    if ui == "off":
        print("Turning off...")
        break
    elif ui == "report":
        coffee_maker.report()
        money_machine.report()
    else:

        drink = menu.find_drink(ui)

        if not (drink is None) and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    if input("would you like another drink? type y/n : ") == "n":
        should_continue = False
