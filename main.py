# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# TODOS list
# TODO: 1. Print report.
# TODO: 2. Check if resources are sufficient.
# TODO: 3. User interface.

from data import MENU

resources = dict(milk=dict(qty=200, unit="ml"), water=dict(qty=300, unit="ml"), coffee=dict(qty=100, unit="gr"),
                 money=dict(qty=100, unit="$USD"))
str_coffee_machine_status = 'OFF'


def print_report(dict_resources) -> None:
    """Print the resources stock and money
    :rtype: None
    """
    print('Ingredients stock:')
    for item in dict_resources:
        int_qty = dict_resources[item]["qty"]
        str_unit = dict_resources[item]["unit"]
        print(f'\t{item}: {int_qty}{str_unit}')
    return


def turn_coffee_machine_on(status) -> str:
    """Turn the machine on."""
    print_report(resources)
    if status == 'OFF':
        return 'ON'
    elif status == 'MNT':
        return 'ON'
    else:
        print('INFO: machine is already on.')
        return 'ON'


def bol_check_ingredients_stock(str_coffee_to_check) -> bool:
    """Check if there is enough ingredients to serve the coffee ordered.
    :rtype: Boolean
    """
    int_qty_water_ordered = MENU[str_coffee_to_check]['ingredients']['water']
    if str_coffee_to_check == 'espresso':
        int_qty_milk_ordered = 0
    else:
        int_qty_milk_ordered = MENU[str_coffee_to_check]['ingredients']['milk']
    int_qty_coffee_ordered = MENU[str_coffee_to_check]['ingredients']['coffee']
    if int_qty_water_ordered > resources['water']['qty'] \
            or int_qty_milk_ordered > resources['water']['qty'] \
            or int_qty_coffee_ordered > resources['water']['qty']:
        print('Not enough ingredients to serve your coffee. Sorry!')
        return False
    else:
        return True


def serve_and_decrease_stock(str_coffee_to_serve) -> None:
    """Decrease the ingredients stock and deliver coffee."""
    global resources
    resources['water']['qty'] -= MENU[str_coffee_to_serve]['ingredients']['water']
    if str_coffee_to_serve != 'espresso':
        resources['milk']['qty'] -= MENU[str_coffee_to_serve]['ingredients']['milk']
    resources['coffee']['qty'] -= MENU[str_coffee_to_serve]['ingredients']['coffee']
    print(str_coffee_to_serve.capitalize() + ' delivered. Enjoy! ☕️')
    print_report(resources)
    return


def deliver_order(str_coffee_ordered) -> None:
    """Checks if there is enough ingredients and serve the coffee."""
    if bol_check_ingredients_stock(str_coffee_ordered):
        serve_and_decrease_stock(str_coffee_ordered)
    else:
        print('There is not enough ingredients to prepare your coffee.')
        print_report(resources)
    return


def bol_valid_order(str_coffee_ordered) -> bool:
    """Check if order is valid.
    :param str_coffee_ordered:
    :return:
    """
    if str_coffee_ordered in MENU.keys():
        return True
    else:
        return False


def coffee_machine() -> None:
    """Main program that runs all coffee machine functionalities"""
    global str_coffee_machine_status
    print('Coffee machine rebooting ....')
    str_coffee_machine_status = turn_coffee_machine_on(str_coffee_machine_status)
    while str_coffee_machine_status == 'ON':
        str_coffee_order = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if str_coffee_order == 'off':
            str_coffee_machine_status = 'OFF'
            print('Coffee machine shutdown...')
        elif bol_valid_order(str_coffee_order):
            deliver_order(str_coffee_order)
        else:
            print(f'{str_coffee_order} coffee type unknown! Order again.')
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coffee_machine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
