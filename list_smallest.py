# Program to find smallest number in a list

nums = [10, 20, 30, 40, 50]

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print("Smallest =", smallest)
