"""https://www.codewars.com/kata/5881460c780e0dd207000084"""

# Spot the Differences

def spot_diff(s1, s2):
    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)
    return diff