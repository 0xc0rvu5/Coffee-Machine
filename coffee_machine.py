#Initialize global variables
MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}
RESOURCES = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}
PROFIT = 0
CONT = True


def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made, False if there are not enough ingredients available.'''
    for item in order_ingredients:
        if order_ingredients[item] >= RESOURCES[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def process_coins():
    '''Returns the total calculated from coins inserted.'''
    print('Please insert coins.')
    total = int(input('How many quarters?: ')) * .25
    total += int(input('How many dimes?: ')) * .1
    total += int(input('How many nickles?: ')) * .05
    total += int(input('How many pennies?: ')) * .01
    return total


def is_transaction_successful(money_received, drink_cost):
    '''Return True when the payment is accepted, or False if money is insufficient.'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global PROFIT
        PROFIT += drink_cost
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False


def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from RESOURCES.'''
    for item in order_ingredients:
        RESOURCES[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}😃')


#initiate coffee machine loop
try:
    while CONT:
        choice = input('What would you like? (expresso/latte/cappuccino): ')
        #two machine maintainer options else normal user option
        if choice == 'off':
            CONT = False
        elif choice == 'report':
            print(f'Water: {RESOURCES["water"]}')
            print(f'Milk: {RESOURCES["milk"]}')
            print(f'Coffee: {RESOURCES["coffee"]}')
            print(f'Money: ${PROFIT}')
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink['ingredients']):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])

except KeyboardInterrupt:
    print('\nSee you later.')