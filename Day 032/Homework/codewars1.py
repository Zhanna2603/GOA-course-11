"""https://www.codewars.com/kata/5266fba01283974e720000fa/train/python"""

# Calculate Variance

def variance(numbers): 
    overage = sum(numbers)/len(numbers)
    result = 0
    for i in numbers:
        result += (i-overage)**2
    return result/len(numbers)