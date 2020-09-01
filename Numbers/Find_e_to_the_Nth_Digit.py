'''
Just like the previous problem, but with e instead of PI. 
Enter a number and have the program generate e up to that many decimal places. 

e = sum (1/k!) from k =1 to infinite
'''

from decimal import Decimal

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    
    return fact
        

def euler(number):
    #Computes euler's constant with 50 terms 
    
    e = 0
    for i in range(50):
        e = Decimal(e + Decimal(factorial(i)**(-1)))
        
    return round(e,number)

if __name__ == '__main__':
    
    number = '0'
    while number.isdigit():
        try:
            number = int(input("Please enter the number of decimal places you want for e: "))
            print('\n\n')
            
            print(f'Value of e = {euler(number)}')
            print('\n\n')
            break
            
        except:
            print('\n')
            print('Please enter an integer')
            print('\n')
            number = '0'
