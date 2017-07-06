import treystravel_core


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

    gasname = 'Regular' or 'Mid-Grade' or 'Premium'
    price = '2.07' or '2.17' or '2.29'
    gas = ''
    while gas != "Q".upper():
        gas = input(message)
        if gas == '87' or gas == '89' or gas == '92':
            a = float(input('\nOur {} gas is ${} per gallon. How many gallons would you like?\n'.format(gasname, price)))
            msg = treystravel_core.treys_travel(gas, treystravel_core.gas_price(gas), a)
            print(msg)
            with open('log.txt', 'a') as history:
                history.write(msg)
            break
            
        elif gas == 'Q':
            print('Program Abandoned.')
            break
    
       
         


if __name__ == '__main__':
    main()