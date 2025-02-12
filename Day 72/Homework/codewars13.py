"""https://www.codewars.com/kata/589273272fab865136000108/train/python"""

# Piano Kata, Part 1

def black_or_white_key(key_press_count):
    normalized_key = key_press_count % 88
    if normalized_key == 0:
        normalized_key = 88
    
    position_in_octave = normalized_key % 12
    if position_in_octave == 0:
        position_in_octave = 12
    
    if position_in_octave in {2, 5, 7, 10, 12}:
        return "black"
    else:
        return "white"