# Use coffee machine documentation to learn how each class works
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:


    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ").lower()

    # TODO: 2. Turn off the coffee machine by entering "off" to the prompt
    if user_input == "off":
        machine_on = False

    # TODO: 3. Print report of all coffee machine resources
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)

        # TODO: 4. Check if there are enough resources to make the user's drink
        sufficient_resources = coffee_machine.is_resource_sufficient(drink)

        if sufficient_resources:
            # TODO: 5. Process the coins the user puts into the machine
            # TODO: 6. Check whether the transaction was successful
            payment_accepted = money_machine.make_payment(drink.cost)
            if payment_accepted:
                # TODO: 7. Make coffee if enough resources and transaction successful
                coffee_machine.make_coffee(drink)
