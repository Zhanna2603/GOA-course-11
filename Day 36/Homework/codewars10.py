"""https://www.codewars.com/kata/545cedaa9943f7fe7b000048"""

# Detect Pangram

def is_pangram(st):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    st = st.upper()
    
    for i in alphabet:
        if i not in st:
            return False
    return True