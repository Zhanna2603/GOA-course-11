"""https://www.codewars.com/kata/5b6183066d0db7bfac0000bb/train/python"""

# Memesorting

def memesorting(meme):
    meme_lower = meme.lower()
    
    # Check for IT-bug
    def check_it(meme):
        i = 0
        for char in meme:
            if char == 'b' and i == 0:
                i += 1
            elif char == 'u' and i == 1:
                i += 1
            elif char == 'g' and i == 2:
                return True
        return False
    
    # Check for Chemistry-boom
    def check_chemistry(meme):
        i = 0
        for char in meme:
            if char == 'b' and i == 0:
                i += 1
            elif char == 'o' and i in [1, 2]:
                i += 1
            elif char == 'm' and i == 3:
                return True
        return False
    
    # Check for Design-edits
    def check_design(meme):
        i = 0
        for char in meme:
            if char == 'e' and i == 0:
                i += 1
            elif char == 'd' and i == 1:
                i += 1
            elif char == 'i' and i == 2:
                i += 1
            elif char == 't' and i == 3:
                i += 1
            elif char == 's' and i == 4:
                return True
        return False
    

