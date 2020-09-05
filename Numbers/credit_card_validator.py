'''
Takes in a credit card number from a common credit card vendor 
(Visa, MasterCard, American Express, Discoverer) 
and validates it to make sure that it is a valid number 
(look into how credit cards use a checksum).

'''

def credit_card_validator(number):
    number = str(number)
    if len(number) not in [15,16] or not number.isdigit():
        return 'Please enter all (15 or 16) digits of the credit card'
    
    check_digit = number[-1]
    number_minus_check_digit = number[:len(number)-1]
    
    #Reverse the string and take all odd and even position numbers 
    num_at_odd_position = number_minus_check_digit[::-1][0::2]
    num_at_even_position = number_minus_check_digit[::-1][1::2]
    
    #Double odd position number and add all digits of number
    
    sum_odd = 0
    for num in num_at_odd_position:
        if len(str(int(num)*2)) == 1:
            sum_odd += int(num)*2
        else:
            sum_odd += 1 + (int(num)*2)%10
            
    sum_even = 0
    for num in num_at_even_position:
        sum_even += int(num)

        
    if 10 - ((sum_odd + sum_even) % 10) == int(check_digit):
        return 'Valid Card'
    
    else:
        return 'Invalid Card'
    
    
def main():
        choice = input("Please enter credit card number: ")
        print(credit_card_validator(choice))
