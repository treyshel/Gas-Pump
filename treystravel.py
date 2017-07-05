# day 8....6/12

#gas price for regular- $2.07
#gas price for mid-grade- $2.17
#gas price for premium- $2.29
import time 
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


#gas pump program 
print('Welcome to Trey\'s Travel Gas Station!\n\n')
#user selects if they want regular, mid-grade, or premium
print('We are pleased to be your provider  for\nunbeatable, competitive gas prices!')
#decision betweeen prepay or postpay
decision = input('To prepay, press 1. To pay after, press 2.\n\n')
if decision == '1':
    grade = input('\nWhat grade type will you be needing today? If Regular Grade, press 1.\nIf Mid-Grade, press 2. If Premium Grade, press 3.\n\n')

#decision 1:

#grade 1 = regular
    if grade == ('1'):
        gas_price = 2.07
        print('\nOur regular gas price is $2.07 per gallon. Would you like to proceed?')
        yes = input('Yes or No.\n\n')
        if yes == ('Yes') or yes == ('yes'):
            money = float(input('\nHow much money will you be spending today?\n\n$'))
            print('\npumping...')
            time.sleep(1.5)
            print('\nYou will recieve',pay_before(money, gas_price), 'gallons.\n')
        else:
            print('You have cancelled your request.')
        print('Thank you and have a great day!')

#grade 2 = mid-grade
    elif grade == '2':
        gas_price = 2.17
        print('\nOur mid-grade gas price is $2.17 per gallon. Would you\nlike to proceed?\n')
        yes = input('Yes or No.\n\n')
        if yes == ('Yes') or yes == ('yes'):
            money = float(input('\nHow much money will you be spending today?\n\n$'))
            print('\npumping...')
            time.sleep(1.5)
            print('\nYou will recieve',pay_before(money, gas_price), 'gallons.\n\n')
        else:
            print('You have cancelled your request.')
        print('Thank you and have a great day!')

#grade 3 = premium 
    elif grade == '3':
        gas_price = 2.29
        print('\nOur mid-grade gas price is $2.29 per gallon. Would you\nlike to proceed?\n')
        yes = input('Yes or No.\n\n')
        if yes == ('Yes') or yes == ('yes'):
            money = float(input('\nHow much money will you be spending today?\n\n$'))
            print('\npumping...')
            time.sleep(1.5)
            print('\nYou will recieve',pay_before(money, gas_price), 'gallons.\n')
        else:
            print('You have cancelled your request.')
        print('Thank you and have a great day!')


#decision 2:
elif decision == '2':
    grade = input('\nWhat grade type will you be needing today? If Regular Grade, press 1.\nIf Mid-Grade, press 2. If Premium Grade, press 3.\n\n')

    if grade == ('1'):
        gas_price = 2.07
        print('\nOur regular gas price is $2.07 per gallon. Would you like to proceed?')
        yes = input('Yes or No.\n\n')
        if yes == ('Yes') or yes == ('yes'):
            gallons = float(input('\nHow many gallons will you be needing today?\n\n'))
            print('\npumping...')
            time.sleep(1.5)
            print('\nThe total cost for you will be $',pay_after(gallons, gas_price), sep='')
        else:
            print('You have cancelled your request.')
        print('Thank you and have a great day!')

    elif grade == '2':
        gas_price = 2.17
        print('\nOur mid-grade gas price is $2.17 per gallon. Would you\nlike to proceed?\n')
        yes = input('Yes or No.\n\n')
        if yes == ('Yes') or yes == ('yes'):
            gallons = float(input('\nHow many gallons will you be needing today?\n\n'))
            print('\npumping...')
            time.sleep(1.5)
            print('\nThe total cost for you will be $',pay_after(gallons, gas_price), sep='')  
        else:
            print('You have cancelled your request.')
        print('Thank you and have a great day!')

#line 123 is an example of another way to put '$' by total cost
    elif grade == '3':
        gas_price = 2.29
        print('\nOur mid-grade gas price is $2.29 per gallon. Would you\nlike to proceed?\n')
        yes = input('Yes or No.\n\n')
        if yes == ('Yes') or yes == ('yes'):
            gallons = float(input('\nHow many gallons will you be needing today?\n\n'))
            print('\npumping...')
            time.sleep(1.5)
            message = '\nThe total cost for you will be $' + str(pay_after(gallons, gas_price))
            print(message)
        else:
            print('You have cancelled your request.')
        print('Thank you and have a great day!') 

#pay after fill option
#user inputs the num
#user inputs the amount of money to pay
#computer displays the number of gallons paid for 

#CONSIDER:
#clean code 
#have a nice interface and customer experience
#use your functions well
#make it personalized to you 
 
 #regular = 2.07
 #mid-grade = 2.17
 #premium = 2.29

