"""https://www.codewars.com/kata/53697be005f803751e0015aa"""

# The Vowel Code

def encode(st):
    encode_st = ""
    for elements in st:
        if elements == "a":
            encode_st += "1"
        elif elements == "e":
            encode_st += "2"
        elif elements == "i":
            encode_st += "3"
        elif elements == "o":
            encode_st += "4"
        elif elements == "u":
            encode_st += "5"
        else:
            encode_st += elements
    return encode_st
        
    
def decode(st):
    decode_st = ""
    for elements in st:
        if elements == "1":
            decode_st += "a"
        elif elements == "2":
            decode_st += "e"
        elif elements == "3":
            decode_st += "i"
        elif elements == "4":
            decode_st += "o"
        elif elements == "5":
            decode_st += "u"
        else:
            decode_st += elements
    return decode_st