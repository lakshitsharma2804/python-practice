# Program to find smallest digit

word = input("write a word = ")
smallest = 10

for ch in word:
    if ch.isdigit():
        if int(ch) < smallest:
            smallest = int(ch)

print(smallest)
