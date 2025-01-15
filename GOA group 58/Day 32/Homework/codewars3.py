"""https://www.codewars.com/kata/55f8a9c06c018a0d6e000132"""

# Regex validate PIN code

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        digits = "0123456789"
        
        for digit in pin:
            if digit not in digits:
                return False
        return True
    return False