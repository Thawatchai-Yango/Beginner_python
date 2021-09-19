height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi

bmi = weight/(height*height)

print("Your BMI is: {0} and you are: ".format(round(bmi,2)), end='')

#conditions
if ( bmi < 16):
   print("severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Normal")

elif ( bmi >= 25 and bmi < 30):
   print("overweight")

elif ( bmi >=30):
   print("severely overweight")
print()

#*************************************************************************
height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi

bmi1 = weight/(height*height)

print("Your BMI is: {0} and you are: ".format(round(bmi1,2)), end='')

#conditions
if ( bmi1 < 16):
   print("severely underweight")

elif ( bmi1 >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi1 >= 18.5 and bmi < 25):
   print("Normal")

elif ( bmi1 >= 25 and bmi < 30):
   print("overweight")

elif ( bmi1 >=30):
   print("severely overweight")
print()

#AVG
BMI_avg = (bmi+bmi1)/2
print("The average BMI for 2 people", round(BMI_avg,2))