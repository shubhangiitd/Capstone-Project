'''
Enter a number and have the program generate the Fibonacci sequence to the Nth number.
'''

def fibonacci(n):
    sequence = [1,1]
    for term in range(2,n):
        sequence.append(sequence[term-2]+sequence[term-1])

    return sequence

if __name__ == '__main__':
    
    number = '0'
    while number.isdigit():
        
        number = input("Please enter the number of digits (>1) you want in the Fibonacci sequence: ")
        
        try:
            print(fibonacci(int(number)))
            break
        except:
            print('Please enter a digit')
            number = '0'
            
            
