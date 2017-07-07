# Regular = 2.07
# MidGrade = 2.17
# Premium = 2.29

def open_tank():
    """ None -> [[str, str, float, float]] """
    gas = []
    with open('tank.txt', 'r') as file:
        file.readline()
        for lines in file:
            split_string = lines.split(', ')
            gas.append([split_string[0], split_string[1], float(split_string[2]), float(split_string[3].strip())])
    return gas 

def make_message(inventory):
    """ [[str, str, float, float]] -> str """
    message = '\n         Welcome to TREY\'S TRAVEL GAS STATION!\n\nWe are pleased to be your provider for the best gas around.\n\nPlease choose the type of gas\nyou would like to use today:\n\n'
    for item in inventory:
        message += '{}. {} (${:0.2f})\n'.format(item[0], item[1], item[3])
    message += '\nPush "Q" to quit.\n'
    return message


def gas_description():
    '''list[str, int ,float]
    >>> gas_description()
    [[87, 'Regular', 5000.0, 2.07], [89, 'Mid-Grade', 2000.0, 2.17], [92, 'Premium', 3500.0, 2.29]]
    '''
    gas = []
    with open('tank.txt', 'r') as file:
        file.readline()
        for lines in file:
            split_string = lines.split(',')
            gas.append([int(split_string[0]), str(split_string[1]), float(split_string[2]), float(split_string[3])])
    return gas 

def get_gas_price(gas):
    '''(str) -> (float)'''
    if gas == '87':
        return 2.07
    elif gas == '89':
        return 2.17
    elif gas == '92':
        return 2.29

def get_gas_name(gas):
    """str -> str"""
    if gas == '87':
        return 'Regular'
    elif gas == '89':
        return 'Mid-Grade'
    elif gas == '92':
        return 'Premium'

def get_amount_message(gasname, price):
    return '\nOur {} gas is ${} per gallon. How many gallons would you like?\n'.format(gasname, price)

def treys_travel(gas, price, amount_of_gal):
    gasname = get_gas_name(gas)
    return '\nYou have purchased {} gallons of {} gas. Your total will be ${:.2f}'.format(amount_of_gal, gasname, price * amount_of_gal)

def tank_take_away(inventory, gas, amount, msg):
    """ [[str, str, float, float]], str, float, str -> bool """
    string_list = ['code, type, amount_in_tank, price']
    for item in inventory:
        if item[0] == gas:
            item[2] = item[2] - amount
        string_list.append('{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))
    message = '\n'.join(string_list)
    with open('tank.txt', 'w') as file:
        file.write(message)
    with open('log.txt', 'a') as history:
        history.write(msg)
    return True

def refill_tank():
    """ [[str, str, float, float]], str, float, str -> bool """
    string_list = ['code, type, amount_in_tank, price']
    left_in_tank = gas_description()
    for item in left_in_tank:
        if item[2] < 5000.0:
            item[2] = 5000.0
        item[0] = str(item[0])
        item[2] = str(item[2])
        item[3] = str(item[3])
        string_list.append(', '.join(item))
        message = '\n'.join(string_list)
    with open('tank.txt', 'w') as file:
        file.write(message)


        