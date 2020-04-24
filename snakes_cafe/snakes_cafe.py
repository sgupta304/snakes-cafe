from textwrap import dedent

welcome_message = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""

order_message = """
***********************************
** What would you like to order? **
***********************************
"""

menu_items = {
    "appetizers": {
        "wings": 0,
        "cookies": 0,
        "spring rolls": 0
    },
    "entrees": {
        "salmon": 0,
        "steak": 0,
        "meat tornado": 0,
        "a literal garden": 0
    },
    "desserts": {
        "ice cream": 0,
        "cake": 0,
        "pie": 0
    },
    "drinks": {
        "coffee": 0,
        "tea": 0,
        "soda": 0,
        "chai": 0
    },
}


def print_menu_items():
    for category in menu_items:
        print(dedent(f"""
        {category.title()}
        ****************"""))
        for item, quantity in menu_items[category].items():
            print(item.title())


def handle_menu_option(user_input):
    for category in menu_items:
        current_category = menu_items[category]
        user_input = user_input.lower()
        if user_input in map(str.lower, current_category.keys()):
            quantity = current_category[user_input.lower()]
            quantity += 1
            current_category[user_input.lower()] = quantity
            print(f"Item ordered {user_input} with quantity {quantity}")
            return
    print(f"{user_input} does not exist on the menu. Please order a valid item from the menu.")


if __name__ == '__main__':
    print(dedent(welcome_message))
    print_menu_items()
    input_value = input(order_message)
    while input_value != "quit":
        handle_menu_option(input_value)
        input_value = input(order_message)