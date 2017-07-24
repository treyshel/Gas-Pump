import treystravel_core

def main():
    gas = input('Refill or Revenue: ')
    if gas.title() == 'Refill':
        treystravel_core.refill_tank()
        print('Tank is refilled.') 
    elif gas.capitalize() == 'Revenue':
        print('Your total store revenue, after the last purchase, is ${:.2f}'.format(treystravel_core.store_revenue()))
    return None 




if __name__ == '__main__':
    main()