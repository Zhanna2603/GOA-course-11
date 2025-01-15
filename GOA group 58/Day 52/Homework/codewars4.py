"""https://www.codewars.com/kata/511f11d355fe575d2c000001"""

# Two Oldest Ages

def two_oldest_ages(ages):
    sorted_ages = sorted(ages)
    return [sorted_ages[-2], sorted_ages[-1]]