import treystravel_core

def test_valid_type():
    #assert treystravel_core.get_gas_name(gas, inventory) == inventory
    assert treystravel_core.get_gas_name('87', 'Regular') == 'Regular'
    assert treystravel_core.get_gas_name('89', 'Mid-Grade') == 'Mid-Grade'
    assert treystravel_core.get_gas_name('92', 'Premium') == 'Premium'
    assert treystravel_core.get_gas_name('60', 'Diesel') == 'Diesel'

def test_valid_gallons():
    #assert treystravel_core.is_valid_gallons(inventory, gas, gallons)
    d = {'92': {'type': 'Premium', 'amount_in_tank': 5000.0, 'price': 2.29, 'code': '92'}, '89': {'type': 'Mid-Grade', 'amount_in_tank': 5000.0, 'price': 2.17, 'code': '89'}}
    assert treystravel_core.is_valid_gallons(d, '89', 30) == True
    assert treystravel_core.is_valid_gallons(d, '89', 600000) == False