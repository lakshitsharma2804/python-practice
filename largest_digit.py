# Program to find largest digit

word = input("write a word = ")
largest = 0

for ch in word:
    if ch.isdigit():
        if int(ch) > largest:
            largest = int(ch)

print(largest)
