import treystravel_core

def treys_travel(gas, price):
    amount = input('\nOur {} gas is ${} per gallon. How many gallons would you like?\n'.format(gas, price))
    print('You have purchased', amount, 'gallons. Your total will be ${}'.format(treystravel_core.gas_price(gas, amount)))
def main():
    message = '''
    Welcome to TREY\'S TRAVEL GAS STATION!

We are pleased to be your provider for the best gas around.

Please choose the type of gas\nyou would like to use today:\n
    87. Regular ($2.07)
    89. Mid-Grade ($2.17)
    92. Premium ($2.29)
    
Push "Q" to quit.
'''
    gas = ''
    total_amount = 0
    while gas != "Q".upper():
        gas = input(message)
        if gas == '87':
            treys_travel('Regular', 2.07)
            break
        elif gas == '89':
            treys_travel('Mid-Grade', 2.17)
            break
        elif gas == '92':
            treys_travel('Premium', 2.29)
            break
        elif gas == 'Q':
            total_amount += treystravel_core.gas_price(gas, amount)
            print('Your total cost is $' + str(total_amount))


if __name__ == '__main__':
    main()