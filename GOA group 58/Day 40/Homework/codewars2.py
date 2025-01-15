"""https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python"""

# Sort Numbers

def solution(nums):
    if nums is None or len(nums) == 0:
        return[]
    return sorted(nums)