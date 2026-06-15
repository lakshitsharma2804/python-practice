# Program to find sum of digits

word = input("write a word = ")
sum_digit = 0

for ch in word:
    if ch.isdigit():
        sum_digit += int(ch)

print(sum_digit)
