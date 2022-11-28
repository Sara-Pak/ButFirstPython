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
