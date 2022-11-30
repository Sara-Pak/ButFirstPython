#if the bill was $150. split bwtn 5 people with 12% tip
#each person should pay (150.00/5) * 1.12 = 33.6
#round the result to 2 decimal places = 33.60

import prettytable as pt
print("Welcome to my tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
guests = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_with_tip = bill * tip_as_percent
total_bill_with_tip = bill + total_with_tip
each_person_pay = total_bill_with_tip / guests
final_amount = round(each_person_pay, 2)
print(f"each person pays ${final_amount}")

#width = 300
#table = pt.PrettyTable()

#table.field_names = ['Each person is responsible for: ']
#[table.add_row(([final_amount]))]

#print(table)
