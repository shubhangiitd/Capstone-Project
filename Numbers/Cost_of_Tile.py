'''
Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.
'''
from decimal import Decimal

def cost_of_tile (tile_length, tile_breadth, floor_length, floor_breadth, cost_per_tile):
    number_of_tiles = (floor_length * floor_breadth)/(tile_length * tile_breadth)
    
    return number_of_tiles * cost_per_tile
    

if __name__ == '__main__':
    
    number = '0'
    while number.isdigit():
        try:
            tile_length = int(input("Please enter tile length: "))
            tile_breadth = int(input("Please enter tile breadth: "))
            floor_length = int(input("Please enter floor length: "))
            floor_breadth = int(input("Please enter floor breadth: "))
            cost_per_tile = int(input("Please enter cost of tile: "))
            print('\n\n')
            cost = cost_of_tile (tile_length, tile_breadth, floor_length, floor_breadth, cost_per_tile)
            print(f'Cost of flooring  = {cost}')
            print('\n\n')
            break
            
        except:
            print('\n')
            print('Please enter an integer')
            print('\n')
            number = '0'
