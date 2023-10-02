def remove_duplicates(nums) -> int:
    if not nums:
        return 0

    unique = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique]:
            unique += 1
            nums[unique] = nums[i]

    return unique + 1

# Example usage:
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
unique_count = remove_duplicates(nums)
print(unique_count)