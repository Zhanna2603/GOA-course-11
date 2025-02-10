"""https://www.codewars.com/kata/54da539698b8a2ad76000228"""

# Take a Ten Minutes Walk

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north_south = 0
    east_west = 0
    
    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'e':
            east_west += 1
        elif direction == 'w':
            east_west -= 1
    return north_south == 0 and east_west == 0