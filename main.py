# day 1 - python print function
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# find the length of the user's string input
str = input("What is your name? ")
print(len(str))

# program to swap two input variables
a = input("a: ")
b = input("b: ")
a, b = b, a
print("a =", a)
print("b =", b)

# manipulating strings.
print("hello" + " " + "Yoofee")
# input() will get user's input in consol, then print() will print the word "hello" and the user's input
print("hello " + input("What's your name?"))

# count the length of the string and print the output.
name = input("what is yo name?")
length = len(name)
print(length)

# data types:basic-> string, integer, float, boolean
# string
print("Hello"[0])  # output-> H

# adding input's double digits ie: 25 = 2+5 = 7
two_digit_number = input("Type a two digit number:")
print(type(two_digit_number))  # str

# subscript the str id
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)  # convert str to int
print(result)

a = int("5") / int(2.7)
print(type(a))

# round up numbers to whole number
print(round(8 / 3))  # 2
print(round(8 / 3, 2))  # ,2 move 2 decimal places (2.67)

# // integer division
# % the remainder of a division
# ** exponentiation ie: 4*3 means 4*4*4
print(8 // 3)
result = 4 / 2  # 2
result /= 2
print(result)  # 1

score = 0
# user scores a point
score += 1
print(score)  # equals 1

# f-string
f"your score is {score}"  # converts automatically

# conditions
# if condition:
# do this
# else:
# do this

water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("welcome to the rollercoaster ride!")
height = int(input("what is your height?"))

if height >= 120:
    print("you can ride the rollcoaster")
else:
    print("Sorry, maybe next year!")

# while loops
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

# infinite loop - loops that keeps excuting / never stops.
while x % 2 == 0:
    x = x / 2
    # example:


def print_range(start, end):
    # loop through the numbers from start to end
    n = start
    while n <= end:
        n += 1
        print(n - 1)


print_range(1, 5)  # should print 1 2 3 4 5 (each number on its own line)

# example 2
# while true:
#   do_something_cool()
#  if user_requested_to_stop():
#     break # stop infnite loop

# for loop
for x in range(5):
    print(x)

# example
friends = ['taylor', 'alex', 'pat', 'eli']
for friends in friends:
    print("hi" + friends)

values = [23, 52, 59, 48]
sum = 0
length = 0
for values in values:
    sum += values
    length += 1

print("Total sum: " + str(sum) + " - average: " + str(sum / length))

# another loop example
product = 1
for n in range(1, 10):
    product = product * n

print(product)


# and another
def to_celcius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):  # range with 3 parameters
    print(x, to_celcius(x))

# nested loops
# for left in range(7):
# for right in range(left,7):
# print(""[" + str(left) + "|" str(right) + "]" end =" "")

print()

# another
teams = ['dragons', 'wolves', 'pandas', 'unicorns']
for home_team in teams:
    for away_teams in teams:
        if home_team != away_teams:
            print(home_team + " vs " + away_teams)

# ANOTHER
for x in 25:
    print(x)

for x in [25]:
    print(x)


# another
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


greet_friends(['taylor', 'lois', 'kenny'])


# recursion structure example

# def recursive_function(parameters):
#   if base_case_condition(parameters):
#      return base_case_value
# recursive_function(modified_parameters)


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return base, number

    # Recursive case: keep dividing number by base.
    return is_power_of(base, number)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False


