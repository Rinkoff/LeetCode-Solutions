"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum(nums,target):
    indices = {}

    for i,num in enumerate(nums):
        needed = target - num

        if needed in indices:
            return [indices[needed],i]

        indices[num] = i

    return []

nums = [2, 7, 11, 15]
target = 19
result = two_sum(nums, target)
if result == []:
    print("There no matches")
else:
    print(result)
