# Regular = 2.07
# MidGrade = 2.17
# Premium = 2.29


def gas_description():
    '''list[str,int,float]

    >>> gas()
    [['Regular', 5000, 2.07], ['Mid-Grade', 2000, 2.17], ['Premium', 3500, 2.29]]
    '''
    gas = []
    with open('treystravel_description.txt', 'r') as file:
        for lines in file:
            split_string = lines.split(',')
            gas.append(([split_string[0]), int(split_string[1]), float(split_string[2]])
    return gas 



def gas_price(gas):
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

def treys_travel(gas, price, amount_of_gal):
    gasname = get_gas_name(gas)
    return '\nYou have purchased {} gallons of {} gas. Your total will be ${:.2f}'.format(amount_of_gal, gasname, price * amount_of_gal)