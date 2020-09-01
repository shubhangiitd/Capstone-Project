'''
Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

def isprime(n):
    # Returns True if the number is prime
    
    number = 1
    
    # Counts the numbers that give zero remainder when n is divided by the number
    # For a number to be prime, it should be divisible by 1 and the number itself
    count = 0 
    
    while number <= n:
        if n % number == 0:
            count += 1
            if count > 2:
                return False  
        number += 1 
  
    return True

def next_prime(n):
    # Finds the next prime number that is higher than the number n
    
    number = n+1
    while True:
        if isprime(number):
            return number
        else:
            number += 1
    
if __name__ == '__main__':
    
    number = '0'
    while number.isdigit():
        
        number = input("Please enter the number for which you want to find immediate next prime number: ")
        
        try:
            print('\n')
            print(f'The next prime number is: {next_prime(int(number))}')
            print('\n')
            
            response = input('Wanna enter another number? (Y or N): ')
            
            if response.lower() == 'y':
                number = '0'
                continue
                
            elif response.lower() == 'n':
                break
            
            else:
                print('\n')
                print('Please enter either y or n')
                print('\n')
                continue
             
        except:
            print('\n')
            print('Please enter an integer')
            print('\n')
            number = '0'
