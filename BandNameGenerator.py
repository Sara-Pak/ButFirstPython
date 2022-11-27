#1 create a greeting for everyone
#2 ask the user for the city that they grew up
#3 ask the user for the name of a pet
#4 combine the name of their city + pet, then display the new band name
#5 make sure the cursor shows on the new line.

import prettytable as pt

sentence = "Easy Band Name Generator!" #1
width = 26


t = pt.PrettyTable()

t.field_names = ['output']
[t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]

print(t)