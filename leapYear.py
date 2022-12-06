# every 4 years is a leap year
# divisible by 4 evenly
# except every year is evenly divisible by 100
# unless it is also evenly divisible by 400
year = int(input("Which year do you want to check?"))
if year % 4 == 0: #zero remainder
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("not a leap year.")
    else:
        print("leap year.")
else:
    print("not a leap year")