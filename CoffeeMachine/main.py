MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# initialize supply values
water_supply = resources["water"]
milk_supply = resources["milk"]
coffee_supply = resources["coffee"]
money_supply = 0.00

machine_on = True

while machine_on:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the coffee machine by entering "off" to the prompt
    if user_input == "off":
        machine_on = False
    # TODO: 3. Print report of all coffee machine resources
    elif user_input == "report":
        print(f"Water: {water_supply} mL")
        print(f"Milk: {milk_supply} mL")
        print(f"Coffee: {coffee_supply} g")
        print(f"Money: ${"{:.2f}".format(money_supply)}")
    else:
        price = MENU[user_input]["cost"]
        water_amount = MENU[user_input]["ingredients"]["water"]
        coffee_amount = MENU[user_input]["ingredients"]["coffee"]
        milk_amount = MENU[user_input]["ingredients"]["milk"]

        # TODO: 4. Check if there are enough resources to make the user's drink
        if water_amount > water_supply:
            print("Sorry, there is not enough water.")
        elif coffee_amount > coffee_supply:
            print("Sorry, there is not enough coffee.")
        elif milk_amount > milk_supply:
            print("Sorry, there is not enough milk.")
        else:
            # TODO: 5. Process the coins the user puts into the machine
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            input_money_total = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
            # print(f"Input money total: ${"{:.2f}".format(input_money_total)}")

            # TODO: 6. Check whether the transaction was successful
            if input_money_total < price:
                print("Sorry that's not enough money. Money refunded.")
            else:
                # TODO: 7. Make coffee if enough resources and transaction successful
                water_supply -= water_amount
                coffee_supply -= coffee_amount
                milk_supply -= milk_amount
                money_supply += price
                change = input_money_total - price

                # check remaining supplies
                # print(f"Water: {water_supply} mL")
                # print(f"Milk: {milk_supply} mL")
                # print(f"Coffee: {coffee_supply} g")
                # print(f"Money: ${"{:.2f}".format(money_supply)}")

                if change > 0:
                    print(f"Here is your ${"{:.2f}".format(change)} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
