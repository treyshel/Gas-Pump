import treystravel_core

def treys_travel(gas, price):
    amount = input('Our {} gas is ${} per gallon. How many gallons would you like?\n'.format(gas, price))
    print('You have purchased', amount, '{}. Your total will be $' + int(pay_after(gallons, gas_price)))
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
    while gas != "Q".upper():
        gas = input(message)
        if gas == '87':



if __name__ == '__main__':
    main()