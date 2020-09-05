'''
A happy number is defined by the following process. 
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. 
Display an example of your output here. Find first 8 happy numbers
'''

def happy_number(number):
    n = str(number)
    
    while len(n) > 1:
        new_n = 0
        for digit in n:
            new_n += int(digit)**2
        
        n = str(new_n)
    
    if n == '1':
        return "Happy number"
    else:
        return "Not so happy"
    
    
def find_happy_number(counter):
    count = 0
    number = 1
    happy_number_list = []
    while count < counter:
        if happy_number(number) == "Happy number":
            happy_number_list.append(number)
            count += 1
        number += 1
    
    return happy_number_list

def main():
    print(find_happy_number(8))
    

if __name__ == '__main__':
    main()
    
    
    
