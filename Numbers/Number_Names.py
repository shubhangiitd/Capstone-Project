'''
Show how to spell out a number in English. 
You can use a preexisting implementation or roll your own, 
but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). 
Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).
'''

# Converts 3 digit number in word
def three_digit_word(number):
    if number == '000':
        return ''
    
    word = []
    number_word = {'01':'one', '02':'two','03':'three','04':'four','05':'five','06':'six','07':'seven','08':'eight',
                   '09':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fiveteen',
                   '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty',
                  '30':'thirty','40':'fourty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}
     
    if number[1] in ['0','1']:
        word.append(number_word[number[1:]])
        
    else:
        word.append(number_word[number[1]+'0'])
        word.append(' ')
        word.append(number_word['0'+ number[2]])
    
    if number[0] != '0':
        word = [number_word['0'+ number[0]]]+ [' hundered and '] + word
    
    number_in_word =''
    for item in word:
        number_in_word += item 
     
    return number_in_word.lower()
def num_name(number):
    number = float(number)
    #Splits decimal and integer part of the number
    number_split = str(number).split('.')
    
    integer_part = number_split[0]
    decimal_part = number_split[1]
    
    denomination = ['', ' thousand ', ' million ', ' billion ', ' trillion ']
    
    
    for zero in range(3-(len(str(integer_part))%3)):
        integer_part = '0'+ integer_part

    if integer_part[0:3] == '000':
        integer_part = integer_part[3:]
    
        
    triplets = int(len(integer_part) / 3)
    denomination_rev = denomination[0:triplets]                 
    denomination_rev.reverse()                 
                      
    word_srt =''
    counter = 0
    for num in range(0,len(integer_part), 3):
        word_srt += three_digit_word(integer_part[num]+integer_part[num+1]+integer_part[num+2]) + denomination_rev[counter]
        counter += 1 
    
    if decimal_part != '0':
        
        word_srt += ' point '
        for digit in decimal_part:
            word_srt += three_digit_word('00'+digit)+' '
        
    
    return word_srt[0].upper() + word_srt[1::]
            
    
if __name__ == '__main__':
    
    while True:
        try:
            number = float(input("Please enter the number: "))
            print(num_name(number))
            break
            
        except:
            print('Please type valid number')
            
