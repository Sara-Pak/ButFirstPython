#The BMI is calculated by dividing a person's weight by the square of their height
#the result should -round to the nearest whole number

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

result = float(weight) / (float(height) * float(height))
print(int(result))
