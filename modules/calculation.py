# Module for calculating
# export function with from-import
import math

def calculate(operator):
    what_operator = ''

    match operator:
        case 'add':
            what_operator = 'Addition'
        case 'subtract':
            what_operator = 'Subtraction'
        case 'divide':
            what_operator = "Division"
        case 'multiply':
            what_operator = "Multiplication"

    print(f'You have chosen {what_operator}')


    first_number = input('Your first number: ')
    second_number = input('Your second number: ')
    convert_first_int = float(first_number)
    convert_second_int = float(second_number)
    
    match operator:
        case 'add':
            calc_sum = math.floor(convert_first_int + convert_second_int)
            print(f'Sum is: {calc_sum}')
        case 'subtract':
            calc_diff = math.floor(convert_first_int - convert_second_int)
            print(f'Difference is: {calc_diff}')
        case 'divide':
            calc_quo = math.floor(convert_first_int / convert_second_int)
            print(f'Quotient is: {calc_quo}')
        case 'multiply':
            calc_prod = math.floor(convert_first_int * convert_second_int)
            print(f'Product is: {calc_prod}')
        case _:
            print('Invalid operator used')
        

    

