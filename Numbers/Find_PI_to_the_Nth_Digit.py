'''
Calculating Pi using 'Chudnovsky algorithm'

https://en.wikipedia.org/wiki/Chudnovsky_algorithm

'''
from decimal import Decimal

def qth_term(q):
    #Computes qth terms
    
    
    #Computes factorial of n
    def factorial(n):
        fact = 1
        for num in range(1,n+1):
            fact *= num
        return fact
    
    numerator = ((-1)**q) * factorial(6*q) * (545140134*q + 13591409)
    denominator = factorial(3*q) * (factorial(q)**3) * ((640320)**(3*q + 3/2))
    
    return Decimal(12*numerator/denominator)

def pi(n):
    # Number of decimal places n that user wants to input
    # Assumed that series would have to run with n terms to generate n decimals accurately
    
    sum = 0
    for q in range(n+1):
        sum = Decimal(sum + qth_term(q))
    
    pi = Decimal(1/sum)
    
    return round(pi,n)


if __name__ == '__main__':
    
    number = '0'
    while number.isdigit():
        try:
            number = int(input("Please enter the number of decimal places you want for pi: "))
            print('\n\n')
            
            print(f'Pi = {pi(number)}')
            print('\n\n')
            break
            
        except:
            print('\n')
            print('Please enter an integer')
            print('\n')
            number = '0'
