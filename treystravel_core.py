Regular = 2.07
MidGrade = 2.17
Premium = 2.29


def gas_description():
    '''list[str, float]

    >>> gas()
    [['regular, 2.07], [mid-grade, 2.17], [premium, 2.29]]
    '''
    gas = []
    with open('treystravel_description.txt', 'r') as file:
        for lines in file:
            split_string = lines.split(',')
            gas.append([split_string[0], float(split_string[1])])
    return gas 



def gas_price(gas, amount):
    '''(str) -> (float)'''
    if gas == '87':
        return float(amount) * 2.07
    elif gas == '89':
        return float(amount) * 2.17
    elif gas == '92':
        return float(amount) * 2.29
