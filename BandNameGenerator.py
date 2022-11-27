#1 create a greeting for everyone
#2 ask the user for the city that they grew up
#3 ask the user for the name of a pet
#4 combine the name of their city + pet, then display the new band name
#5 make sure the cursor shows on the new line.

import prettytable as pt
print("Welcome to the Bane-Name Generator!") #1
city = input("What's name of the city you grew up in? ") #2
pet = input("What's the name of your pet? ") #3

width = 26

t = pt.PrettyTable()

t.field_names = ['Here is the result of your Band-Name!']
[t.add_row([city +" "+pet[i:i + width]]) for i in range(0, len(city + pet), width,)]#4

print(t)
print ("\n") #5
