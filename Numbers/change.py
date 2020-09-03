'''
The user enters a cost and then the amount of money given. 
The program will figure out the change 
and the number of quarters, dimes, nickels, pennies needed for the change.

'''


def change(item_cost, cash_paid):
    coinnage = [('Quarter',25),('Dime',10), ('Nickle',5), ('Penny',1)]
    number_of_coins = []
    
    change = cash_paid - item_cost
    print (f"Here's your change for ${change}")
    print (f"Dollor = {int(change)}")
    change = round(change - int(change),2)*100 
    
    for coin_name,coin in coinnage:
        if int(change/coin) !=0:
            print (f"{coin_name} = {int(change/coin)}")
            change = change - int(change/coin)*coin
            
    print('Thanks for Shopping')
    
    

if __name__ == '__main__' :
    while True: 
        try:
            item_cost = float(input('Please enter cost of item: '))
            cash_paid = float(input('Please enter cash paid: '))
            
            if item_cost > cash_paid:
                print('Item cost is more than cost paid')
                continue
            
            elif item_cost == cash_paid:
                print('There is no change/nThanks for Shopping')
                break
                
            else:
                change(item_cost, cash_paid)
                break
                
            
        except:
            print('Please enter valid cost or cash')
        
