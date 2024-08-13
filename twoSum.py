# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
def two_sum(numbers, target):
    # iterate over the array to check pairs of numbers 
    for i, val1 in enumerate(numbers):
        for j, val2 in enumerate(numbers):
            if i !=j and val1 + val2 == target: 
                return i, j
        

"""
def two_sum(numbers, target):
    seen = {}
    for i, val in enumerate(numbers):
        remaining = target - val
        if remaining in seen:
            return seen[remaining], i
        seen[val] = i
"""

print(two_sum([1, 2, 3], 4))