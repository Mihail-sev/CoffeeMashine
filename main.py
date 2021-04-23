MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def start_menu():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.0,
    }

    def main_menu():
        nonlocal resources
        user_drink = input("What did you like? (espresso/ latte/ cappuccino)\n").lower()

        def coin_accept():
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            accept_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            return accept_money


        def check_resources():
            for i in MENU[user_drink]["ingredients"]:
                if resources[i] < MENU[user_drink]["ingredients"][i]:
                    print("Sorry is not enough {i}")
                    return False
                else:
                    return True

        def change_resources():
            nonlocal resources
            for i in MENU[user_drink]["ingredients"]:
                resources[i] -= MENU[user_drink]["ingredients"][i]
            resources["money"] += MENU[user_drink]["cost"]

        if user_drink == "off":
            print("")
        elif user_drink == "report":
            print(f"""
            Water: {resources["water"]} ml
            Milk: {resources["milk"]} ml
            Coffee: {resources["coffee"]} ml
            Money: ${resources["money"]}
            """)
            main_menu()
        elif user_drink == "espresso" or user_drink == "latte" or user_drink == "cappuccino":
            print("In first, give me money, only real metal, only $ coins")
            accept_money = coin_accept()
            if accept_money < MENU[user_drink]["cost"]:
                print("Нищеброд")
            else:
                if check_resources():
                    change = round(accept_money - MENU[user_drink]["cost"], 2)
                    change_resources()
                    print(f"Here is {change} in change")
                    print(f"Enjoy you ☕")
                    return main_menu()
                else:
                    return main_menu()
        else:
            print("Incorrect name. Input again")
            main_menu()
    main_menu()


start_menu()
