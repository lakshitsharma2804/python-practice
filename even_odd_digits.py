# Program to count even and odd digits

word = input("write a word = ")

even = 0
odd = 0

for ch in word:
    if ch.isdigit():
        if int(ch) % 2 == 0:
            even += 1
        else:
            odd += 1

print("Even Digits =", even)
print("Odd Digits =", odd)
