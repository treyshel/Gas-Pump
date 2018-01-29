# Regular = 2.07
# MidGrade = 2.17
# Premium = 2.29
import disk


def make_message(inventory):
    """ [[str, str, float, float]] -> str """
    message = '\n         Welcome to TREY\'S TRAVEL GAS STATION!\n\nWe are pleased to be your provider for the best gas around.\n\nPlease choose the type of gas\nyou would like to use today:\n\n'
    for item in inventory.values():
        message += '{}. {} (${:0.2f})\n'.format(
            item.get('code', ''), item.get('type', ''), item.get('price', ''))
    message += '\nPush "Q" to quit.\n'
    return message


def get_gas_price(gas, inventory):
    '''(str) -> (float)'''
    return inventory.get(gas).get('price')


def get_gas_name(gas, inventory):
    """str -> str"""
    if gas == '87':
        return 'Regular'
    elif gas == '89':
        return 'Mid-Grade'
    elif gas == '92':
        return 'Premium'
    elif gas == '60':
        return 'Diesel'


def get_amount_message(gasname, price):
    return '\nOur {} gas is ${} per gallon. How many gallons would you like?\n'.format(
        gasname, price)


def treys_travel(gas, price, amount_of_gal, gasname):
    total = price * amount_of_gal
    return '\nYou have purchased {} gallons of {} gas. Your total will be ${:.2f}'.format(
        amount_of_gal, gasname, total)


def tank_take_away(inventory, gas, amount):
    """ Item, str, float -> bool """
    take_away = disk.tank_take_away(inventory, gas, amount)
    return take_away


def store_revenue():
    ''' returns a float that stands for how much
    revenue the store is making after every purchase'''
    use_log = disk.in_log()
    price = 0
    for item in use_log:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price


def is_valid_gallons(inventory, gas, gallons):
    ''' {{'code': str, 'type':str, 'amount_of gallons': float, 'price': float}}, str, float -> bool 
    >>> d = {'92': {'type': 'Premium', 'amount_in_tank': 5000.0, 'price': 2.29, 'code': '92'}, '89': {'type': 'Mid-Grade', 'amount_in_tank': 5000.0, 'price': 2.17, 'code': '89'}}
    >>> is_valid_gallons(d, '89', 30)
    True
    >>> is_valid_gallons(d, '89', 600000)
    False
    '''
    return inventory.get(gas).get('amount_in_tank', -1) >= gallons


def init_tank():
    with open('tank.txt', 'w') as file:
        file.write("""code, type, amount_in_tank, price
 87, Regular, 5000, 1.99
 89, Mid-Grade, 5000, 2.09
 92, Premium, 5000, 2.29
 60, Diesel, 5000, 2.50""")
