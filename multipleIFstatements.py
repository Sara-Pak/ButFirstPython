print("Welcome to the rollercoaster ride!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?" ))
    if age < 12:
        print("Child tickets are $5!")
        bill = 5
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7!")
    else:
        bill = 12
        print("Adult tickets are $12!")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo =="Y":
        bill += 3
        # is the same as 'bill = bill + 3'
        # add $3 to their bil

        print(f"Your final bill is {bill}")
else:
    print("Sorry, maybe next year you'll be tall enough to ride.")
