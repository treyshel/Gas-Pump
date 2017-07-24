import treystravel_core

def get_gas(inventory):
    message = treystravel_core.make_message(inventory)
    while True:
        gas = input(message)
        if gas in inventory.keys():
            return gas
        elif gas.lower() == 'q':
            print('\nProgram Abandoned.')
            exit()
        elif gas == 'Refill':
            treystravel_core.refill_tank()
            print('Tank is now refilled.')
            exit()
        else:
            print('sorry invalid choice')

def get_gallons(inventory, gas, gasname, price):
    msg = treystravel_core.get_amount_message(gasname, price)
    while True:
        gallons = float(input(msg))
        if treystravel_core.is_valid_gallons(inventory, gas, gallons):
            return gallons
        elif gas.lower() == 'q':
            print('\nProgram Abandoned.')
            exit()
        else:
            msg = '\nI\'m sorry but we don\'t have that much in our tank. Try another amount or enter Q to quit.\n'

def main():
    inventory = treystravel_core.open_tank()
    if not inventory:
        treystravel_core.init_tank()
        print('init inventory')
        exit()
    gas = get_gas(inventory)
    gasname, price = treystravel_core.get_gas_name(gas, inventory), treystravel_core.get_gas_price(gas, inventory)
    gallons = get_gallons(inventory, gas, gasname, price)
    print(treystravel_core.treys_travel(gas, price, gallons, gasname))
    if treystravel_core.tank_take_away(inventory, gas, gallons):
        print('Successful Sale')

if __name__ == '__main__':
    main()