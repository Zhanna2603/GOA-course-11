"""https://www.codewars.com/kata/5ab6538b379d20ad880000ab"""

# Area or Perimeter

def area_or_perimeter(l , w):
    if l == w:
        return l * w        # areaof a square
    else:
        return 2 *(l + w)   # perimeter