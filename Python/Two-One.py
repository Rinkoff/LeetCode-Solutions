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