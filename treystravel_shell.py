import treystravel_core


def main():
    inventory = treystravel_core.open_tank()
    message = treystravel_core.make_message(inventory)

    gas = input(message)
    while True:
        if gas in ['87', '89', '92']:
            gasname = treystravel_core.get_gas_name(gas)
            price = treystravel_core.get_gas_price(gas)             
            gallons = float(input(treystravel_core.get_amount_message(gasname, price)))

            while not treystravel_core.is_valid_gallons(inventory, gas, gallons):
                gallons = input('\nI\'m sorry but we don\'t have that much in our tank. Try another amount or enter Q to quit.\n')
                if gallons.lower() == 'q':
                    return None
                gallons = float(gallons.strip())
            msg = treystravel_core.treys_travel(gas, treystravel_core.get_gas_price(gas), gallons)
            print(msg)
            if treystravel_core.tank_take_away(inventory, gas, gallons, msg):
                print('Successful Sale')
            break
        elif gas == 'Q':
            print('\nProgram Abandoned.')
            break
        gas = input('\nInvalid choice. Choose a gas number or type "Refill" to generate 5000 gallons of gas into the tank.\n')
        if gas == 'Refill':
            treystravel_core.refill_tank()
            print('Tank is now refilled.')
            break 
            

    
       
         


if __name__ == '__main__':
    main()