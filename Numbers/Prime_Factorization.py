'''
Have the user enter a number and find all Prime Factors (if there are any) and display them.
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
            
def prime_factor(n):
    prime = 2
    prime_factors =[]

    while prime <= n:

        if n % prime == 0:
            prime_factors.append(prime)
            while n % prime == 0:
                n /= prime

        prime = next_prime(prime)

    return prime_factors
            
            
if __name__ == '__main__':
    
    number = '0'
    while number.isdigit():
        try:
            number = int(input("Please enter the number for which you want to find prime factors: "))
            print('\n\n')
            
            prime_factor = prime_factor(number)
            print(f'The prime factors of (number) are: {prime_factor}')
            print('\n\n')
            break
            
        except:
            print('\n')
            print('Please enter an integer')
            print('\n')
            number = '0'
