'''
Develop a converter to convert a decimal number to binary 
or a binary number to its decimal equivalent.
'''


def binary_to_decimal(number):
    number = number[::-1]
    decimal = 0
    for power, digit in enumerate(number):
        decimal = decimal + int(digit)*(2**power)
    
    return decimal
        

    
def decimal_to_binary(number):
    return str(bin(number)[2:])
            

if __name__ == '__main__' :
    while True: 
        
        print("Choose b for Binary to Decimal conversion")
        print("Choose d for Decimal to Binary conversion/n")
        choice = input("Enter b or d")
            
        if choice.lower() not in ['b','d']:
            print('Please enter either b or d')
            continue
        
        
        if choice.lower() == 'b':
            try:
                number = input('Please enter binary number')
                print(binary_to_decimal(number))
                break
                
            except:
                print('Please enter a valid binary number')
                continue
                
        elif choice.lower() == 'd':
            try:
                number = input('Please enter a number')
                print(decimal_to_binary(int(number)))
                break
                
            except:
                print('Please enter a valid number')
                continue

        
