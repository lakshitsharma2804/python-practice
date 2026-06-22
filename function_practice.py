# Function Practice

# 1. Welcome Function
def welcome():
    print("Welcome Lakshit")

welcome()


# 2. Square Function with User Input
def square():
    num = int(input("Enter a number = "))
    print("Square =", num * num)

square()


# 3. Cube Function with User Input
def cube():
    num = int(input("Enter a number = "))
    print("Cube =", num * num * num)

cube()


# 4. Even Odd Function with User Input
def check_even_odd():
    num = int(input("Enter a number = "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd()


# 5. Function with Parameter
def greet(name):
    print("Hello", name)

greet("Lakshit")


# 6. Add Function using Parameters
def add(a, b):
    print(a + b)

add(10, 20)


# 7. Square Function using Parameter
def find_square(num):
    print(num * num)

find_square(5)


# 8. Even Odd using Parameter
def check_even_odd_parameter(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd_parameter(8)


# 9. Add Function using Return
def add_return(a, b):
    return a + b

result = add_return(10, 20)
print(result)


# 10. Square Function using Return
def square_return(num):
    return num * num

result = square_return(5)
print(result)


# 11. Cube Function using Return
def cube_return(num):
    return num * num * num

result = cube_return(3)
print(result)


# 12. Boolean Function
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = is_even(6)
print(result)