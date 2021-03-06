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
    "money": 0,
}


while True:
# print report
# print(resources)
    while True:
        coffee = input('What would you like: espresso, cappuccino or latte?').lower().strip()
        if coffee in ('espresso','cappuccino','latte'):
            print(f"You chose: {coffee}\n")
            break
        if coffee in ('report'):
            print(f'Water: {resources["water"]}')
            print(f'Milk: {resources["milk"]}')
            print(f'Coffee: {resources["coffee"]}')
            print(f'Money: {resources["money"]}')

        if coffee in ('off'):
            print('Goodbye')
            quit()
        else:
            print("Enter a valid choice")
    # check sufficient resources

    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        print('Not enough water')
        quit()
    if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
        print('Not enough milk')
        quit()
    if MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        print('Not enough coffee')
        quit()

    # Process Coins
    while True:
        try:
            quarters = int(input('How many quarters:'))
            dimes = int(input('How many dimes:'))
            nickels = int(input('How many nickels:'))
            pennies = int(input('How many pennies:'))
            break
        except:
                print("Integers Only")
        # dimes = int(input('How many dimes:'))
        # nickels = int(input('How many nickels:'))
        # pennies = int(input('How many pennies:'))


    # get change
    payment = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    change = payment - MENU[coffee]["cost"]
    if MENU[coffee]["cost"] > payment:
        print('Money refunded, not enough $')

    if MENU[coffee]["cost"] == payment:
        print(f'Enjoy your {coffee}')

    if MENU[coffee]["cost"] < payment:
        print(f'Here is your change: ${change}')
        print(f'Enjoy your {coffee}')


    # rebalance values
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee]["cost"]

