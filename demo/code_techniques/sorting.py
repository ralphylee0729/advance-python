"""sorting"""

from random import randint


nums = [randint(0, 10) for _ in range(10)]

# sorts in-place, mutating the original list
nums.sort()

# creates a new list of sorted numbers, not mutating the original list
sorted_nums = sorted(nums)

print(nums)
print(sorted_nums)


nums = [randint(0, 10) for _ in range(10)]

reverse_sorted_nums = reversed(sorted(nums))

print(reverse_sorted_nums)

print(list(reverse_sorted_nums))