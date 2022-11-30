#if the bill was $150. split bwtn 5 people with 12% tip
#each person should pay (150.00/5) * 1.12 = 33.6
#round the result to 2 decimal places = 33.60

import prettytable as pt
print("Welcome to my tip calculator")
total_bill_cost = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
how_many_guests = int(input("How many people to split the bill? "))

each_person_pay = (total_bill_cost / how_many_guests) * tip_percentage

width = 300
table = pt.PrettyTable()

table.field_names = ['Each person is responsible for: ']
[table.add_row([each_person_pay])]

print(table)
