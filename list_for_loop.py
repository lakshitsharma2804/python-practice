# Traversing List Using For Loop

nums = [10, 20, 30, 40, 50]

print("List Elements:")

for n in nums:
    print(n)

print()

print("Elements at Even Indexes:")

for index, value in enumerate(nums):
    if index % 2 == 0:
        print(value)
