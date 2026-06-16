# Program to find largest number in a list

nums = [10, 20, 30, 40, 50]

largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest =", largest)
