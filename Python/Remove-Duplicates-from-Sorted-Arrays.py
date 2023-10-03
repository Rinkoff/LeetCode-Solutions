"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
"""

def remove_duplicates(nums) -> int:
    if not nums:
        return 0

    unique = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique]:
            unique += 1
            nums[unique] = nums[i]

    return unique + 1

nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
unique_count = remove_duplicates(nums)
print(unique_count)
