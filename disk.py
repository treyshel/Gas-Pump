def open_tank():
    """ None -> [[str, str, float, float]] """
    gas = {}
    with open('tank.txt', 'r') as file:
        l = file.readline().strip().split(', ')
        lines = file.readlines()

    if len(l) < 4:
        init_tank()
    key_1, key_2, key_3, key_4 = l

    for line in lines:
        code, typegas, amount, price = line.strip().split(', ')
        gas[code] = {
            key_1: code,
            key_2: typegas,
            key_3: float(amount),
            key_4: float(price)
        }
    return gas


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
            gas.append([
                split_string[0].strip(),
                str(split_string[1].strip()),
                float(split_string[2].strip()),
                float(split_string[3].strip())
            ])
    return gas


def in_log():
    """ [[float, str, float]] -> bool """
    log = []
    with open('log.txt', 'r') as history:
        history.readline()
        readlines = history.readlines()
    for lines in readlines:
        split_string = lines.strip().split(',')
        log.append(
            [float(split_string[0]), split_string[1],
             float(split_string[2])])
    return log


def tank_take_away(inventory, gas, amount):
    """ Item, str, float -> bool """
    string_list = ['code, type, amount_in_tank, price']
    if not inventory.get(gas, False):
        return False
    inventory[gas][
        'amount_in_tank'] = inventory.get(gas).get('amount_in_tank') - amount
    transaction_message = '\n{}, {}, {}'.format(amount,
                                                inventory.get(gas).get(
                                                    'type', ''),
                                                inventory.get(gas).get(
                                                    'price', ''))
    with open('log.txt', 'a') as file:
        file.write(transaction_message)
    # key_1, key_2, key_3, key_4 = list(inventory.get(gas).keys())
    key_1, key_2, key_3, key_4 = 'code', 'type', 'amount_in_tank', 'price'
    new_file_body = '{}, {}, {}, {}'.format(key_1, key_2, key_3, key_4)
    for item in inventory.values():
        new_file_body += '\n{}, {}, {}, {}'.format(
            item.get(key_1), item.get(key_2), item.get(key_3), item.get(key_4))
    with open('tank.txt', 'w') as file:
        file.write(new_file_body)
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
