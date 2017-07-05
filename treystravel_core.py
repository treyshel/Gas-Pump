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



#pay_before:
    #gallons = money / gas_price
def pay_before(money, gas_price):
    '''(float, float) -> (float)
    
    returns amount of gallons
    
    >>> gallons(20, 2.07)
    9.66
    >>> gallons(10, 2.17)
    4.60
    >>> gallons(35, 2.29)
    15.28
    '''
    gallons = money / gas_price
    
    #round gallons 2 decimal places
    return round(gallons, 2)

#pay after:
    #total_cost = gallons * gas_price
def pay_after(gallons, gas_price):
    '''(float, float) -> (float)
    
    returns total cost of gas
    24.839999999999996
    >>> total_cost(12, 2.07)
    24
    >>> total_cost(10, 2.17)
    21.70
    >>> total_cost(7, 2.29)
    16.03
    '''
    cost = gallons * gas_price
    return round(cost, 2)