"""https://www.codewars.com/kata/598106cb34e205e074000031/train/python"""

# The Deaf Rats of Hamelin

def count_deaf_rats(town):
    town = town.replace(' ', '')
    piper_index = town.find('P')
    deaf_rats = 0

    i = 0
    while i < len(town):
        if i == piper_index:
            i += 1
        else:
            rat = town[i:i+2]
            if i < piper_index:
                if rat == 'O~':
                    deaf_rats += 1
            else:
                if rat == '~O':
                    deaf_rats += 1
            i += 2 
    return deaf_rats