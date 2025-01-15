"""https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python"""

# V A P O R C O D E

def vaporcode(s):
    s = s.replace(" ","")
    result = list(s.upper())
    return "  ".join(result)