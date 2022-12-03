#---- nested if / else statements ----
#if condition:
#if another condition:
#do this
# else:
#do this
#else:
#do this

print("Welcome to our rollercoaster ride!")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you're not tall enough for the ride. Maybe next year!")
