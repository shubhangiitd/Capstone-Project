'''
The sieve of Eratosthenes is one of the most efficient ways 
to find all of the smaller primes (below 10 million or so).

'''


def sieve_of_eratosthenes(number):
    number = int(number)
    
    # Position in number_list is the number, True/False determines prime/non-prime number
    number_list = [True]*(number+1)
    
    # Mark 0 and 1 as non-prime
    number_list[0] = False
    number_list[1] = False
    
    prime_number = []
    
    for index, prime in enumerate(number_list):
        if index in [0,1]:
            continue
            
        elif prime:
            prime_number.append(index)
            
            for num in range(index,len(number_list),index):
                number_list[num] = False
    
    return prime_number

if __name__ == '__main__':
    
    while True:
        choice = input('Please enter a number upto which you want to generate prime nos.: ')
        
        if choice.isdigit():
            print(sieve_of_eratosthenes(choice))
            break
        else:
            print('Enter a valid integer')
    
