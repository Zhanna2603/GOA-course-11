"""https://www.codewars.com/kata/55b42574ff091733d900002f"""

# Friend or Foe?

def friend(x):
    result = []
    for name in x:
        if len(name) == 4 and name.isalpha():
            result.append(name)
    return result