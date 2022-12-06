#The BMI is calculated by dividing a person's weight by the square of their height
#the result should -round to the nearest whole number

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

result = float(weight) / (float(height) * float(height))
print(int(result))

#alt solution

result = int(weight)/float(height) ** 2
result_as_whole_number = int(result)
print(result_as_whole_number)

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are overweight.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")

