# Largest, Smallest and Sum in a List

nums = [12, 45, 7, 89, 23]

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print("Largest Number =", largest)

print("Smallest Number =", smallest)

print("Sum =", sum(nums))
