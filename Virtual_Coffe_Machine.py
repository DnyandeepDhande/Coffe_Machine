
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def print_report():
    """Print the current resource values."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(coffee):
    """Returns True when the order can be made, False if ingredients are insufficient."""
    for item in coffee['ingredients']:
        if coffee['ingredients'][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def check_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_name, coffee):
    """Deduct the required ingredients from the resources."""
    for item in coffee['ingredients']:
        resources[item] -= coffee['ingredients'][item]
    print(f"Here is your {coffee_name} ☕. Enjoy!")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        else:
            drink = MENU.get(choice)
            if drink:
                if check_resources(drink):
                    payment = process_coins()
                    if check_transaction_successful(payment, drink["cost"]):
                        make_coffee(choice, drink)
            else:
                print("Invalid choice. Please select again.")

coffee_machine()
