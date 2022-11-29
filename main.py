#day 1 - python print function
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#find the length of the user's string input
str = input("What is your name? ")
print(len(str))

#program to swap two input variables
a = input("a: ")
b = input("b: ")
a,b = b,a
print("a =", a)
print("b =", b)

#manipulating strings.
print("hello" + " " + "Yoofee")
#input() will get user's input in consol, then print() will print the word "hello" and the user's input
print("hello " + input("What's your name?"))

#count the length of the string and print the output.
name = input("what is yo name?")
length = len(name)
print(length)

#data types:basic-> string, integer, float, boolean
# string
print("Hello"[0]) #output-> H

#adding input's double digits ie: 25 = 2+5 = 7
two_digit_number = input("Type a two digit number:")
print(type(two_digit_number)) #str

#subscript the str id
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit) #convert str to int
print(result)

#round up numbers to whole number
print(round(8/3)) #2
print(round(8/3, 2)) #,2 move 2 decimal places (2.67)

print(8//3)
result = 4/2 #2
resuly /= 2
print(result) #1

score = 0
#user scores a point
score += 1
print(score) # equals 1

#f-string
f"your score is {score}" #converts automatically


