from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

done_making_drink = False
drink = {}
profit = 0
m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

while not done_making_drink:
    choice = input(f"What would you like? {m.get_items()}: ")
    if choice == "off":
        done_making_drink = True
    elif choice == "report":
        print(cm.report())
        print(mm.report())
    else:
        drink = m.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            mm.make_payment(drink.cost)
            cm.make_coffee(drink)


