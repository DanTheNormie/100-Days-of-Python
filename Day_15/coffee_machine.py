from Day_15.machine_data import *
from Day_15.art import logo
import os


def print_report():
    print(f"""
-------------- Report --------------
    Water  : {resources["water"]}ml
    Milk   : {resources["milk"]}ml
    Coffee : {resources["coffee"]}g
    Money  : ${resources["money"]}
------------ Report End ------------
    """)


def check_if_res_are_sufficient(beverage):
    stocks_req = []
    for ingredient in menu[beverage]["ingredients"]:
        ingredient_amt = menu[beverage]["ingredients"][ingredient]
        stock_rep = {
            "ingredient": f"{ingredient}",
            "required": ingredient_amt
        }
        if resources.get(ingredient) is None:
            stock_rep["available"] = False
            stock_rep["is_sufficient"] = False
            stock_rep["present"] = 0
        else:
            stock_rep["available"] = True
            stock_rep["present"] = resources[ingredient]
            stock_rep["is_sufficient"] = (resources[ingredient] >= menu[beverage]["ingredients"][ingredient])

        stocks_req.append(stock_rep)

    result = True
    for item in stocks_req:
        if not (item["is_sufficient"] and item["available"]):
            ingredient = item["ingredient"]
            req_amt = item["required"]
            stk_amt = item["present"]
            print(f"Sorry, There is not enough {ingredient} \nwe need {req_amt - stk_amt} more")
            result = False

    return result


def ask_for_money(price):
    print("Please insert coins.\n")

    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))

    money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

    if money > price:
        print(f"Here is ${(money - price):.2f} in change.")
    else:
        print("Sorry, That's not enough money.\nMoney refunded.")

    return money >= price


def serve_and_update_report(beverage):
    print(f"Here is your {beverage}. Enjoy!!!")

    for ingredient in menu[beverage]["ingredients"]:
        resources[ingredient] -= menu[beverage]["ingredients"][ingredient]


def serve_beverage_to_user(beverage):
    cost = menu[beverage]["cost"]
    if ask_for_money(cost):
        serve_and_update_report(beverage)


def is_user_input_valid(u_input):
    for item in menu:
        if u_input == item:
            return True
    print("please enter a valid beverage name.")
    return False


should_continue = True
while should_continue:
    os.system('cls')
    print("Welcome to my coby machine")
    print(logo)

    u_input = input(f"""
    Please select a beverage of your choice
    1. Espresso    ${menu["espresso"]["cost"]}
    2. Latte       ${menu["latte"]["cost"]}
    3. Cappuccino  ${menu["cappuccino"]["cost"]}
    """)

    if u_input == "report":
        print_report()
    elif u_input == "off":
        print("Turning off.....")
        break
    else:
        if is_user_input_valid(u_input):
            if check_if_res_are_sufficient(u_input):
                serve_beverage_to_user(u_input)

    if not (input("Do you want another beverage? type y/n : ") == "y"):
        should_continue = False
