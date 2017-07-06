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
    gas = ''
    while gas != "Q".upper():
        gas = input(message)
        if gas == '87' or gas == '89' or gas == '92':
            print(treystravel_core.treys_travel(gas, treystravel_core.gas_price(gas))) 
            break
        elif gas == 'Q':
            print('Program Abandoned.')
            break
    with open('log.txt', 'a') in history:
        history.write('\n'treystravel_core.treys_travel(gas, treystravel_core.gas_price(gas)))
         


if __name__ == '__main__':
    main()