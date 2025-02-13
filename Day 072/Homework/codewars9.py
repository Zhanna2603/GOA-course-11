"""https://www.codewars.com/kata/5583d268479559400d000064/train/python"""

# Binary to Text (ASCII) Conversion

def binary_to_string(binary):
    if not binary:
        return ""
    
    text = ""
    for i in range(0, len(binary), 8):
        chunk = binary[i:i+8]
        ascii_code = int(chunk, 2)
        character = chr(ascii_code)
        text += character
    return text