print("      ==== Welcome to BMI calculater ====")
print()
print("       Find the average BMI of 5 women")
w1_height = float(input("Enter 1st Woman height in meters = "))
w1_weight = float(input("Enter 1st Woman weight in kilogram = "))
print("---->1st Woman BMI is =  ", round(w1_weight / (w1_height * w1_height), 2))
print()

w2_height = float(input("Enter 2nd Woman height in meters = "))
w2_weight = float(input("Enter 2nd Woman weight in kilogram = "))
print("---->2nd Woman BMI is =  ", round(w2_weight / (w2_height * w2_height), 2))
print()

w3_height = float(input("Enter 3rd Woman height in meters = "))
w3_weight = float(input("Enter 3rd Woman weight in kilogram = "))
print("---->3rd Woman BMI is =  ", round(w3_weight / (w3_height * w3_height), 2))
print()

w4_height = float(input("Enter 4th Woman height in meters = "))
w4_weight = float(input("Enter 4th Woman weight in kilogram = "))
print("---->4th Woman BMI is =  ", round(w4_weight / (w4_height * w4_height), 2))
print()

w5_height = float(input("Enter 5th Woman height in meters = "))
w5_weight = float(input("Enter 5th Woman weight in kilogram = "))
print("---->5th Woman BMI is =  ", round( w5_weight / (w5_height * w5_height), 2))
print()

print("*****The average BMI of 5 women is  =  ", (round(w1_weight / (w1_height * w1_height), 2) +
                                                  round(w2_weight / (w2_height * w2_height), 2) +
                                                  round(w3_weight / (w3_height * w3_height), 2) +
                                                  round(w4_weight / (w4_height * w4_height), 2) +
                                                  round(w5_weight / (w5_height * w5_height), 2)) / 5)
print()
print("       Find the average BMI of 5 men")
m1_height = float(input("Enter 1st man height in meters = "))
m1_weight = float(input("Enter 1st man weight in kilogram = "))
print("---->1st man BMI is =  ", round(m1_weight / (m1_height * m1_height), 2))
print()

m2_height = float(input("Enter 2nd man height in meters = "))
m2_weight = float(input("Enter 2nd man weight in kilogram = "))
print("---->2nd man BMI is =  ", round(m2_weight / (m2_height * m2_height), 2))
print()

m3_height = float(input("Enter 3rd man height in meters = "))
m3_weight = float(input("Enter 3rd man weight in kilogram = "))
print("---->3rd man BMI is =  ", round(m3_weight / (m3_height * m3_height), 2))
print()

m4_height = float(input("Enter 4th man height in meters = "))
m4_weight = float(input("Enter 4th man weight in kilogram = "))
print("---->4th man BMI is =  ", round(m4_weight / (m4_height * m4_height), 2))
print()

m5_height = float(input("Enter 5th man height in meters = "))
m5_weight = float(input("Enter 5th man weight in kilogram = "))
print("---->5th man BMI is =  ", round( m5_weight / (m5_height * m5_height), 2))
print()

print("*****The average BMI of 5 men is  =  ", (round(m1_weight / (m1_height * m1_height), 2) +
                                                round(m2_weight / (m2_height * m2_height), 2) +
                                                round(m3_weight / (m3_height * m3_height), 2) +
                                                round(m4_weight / (m4_height * m4_height), 2) +
                                                round(m5_weight / (m5_height * m5_height), 2)) / 5)
print()
print("*****The average BMI of all women and mem is = ",(round(w1_weight / (w1_height * w1_height), 2) +
                                                         round(w2_weight / (w2_height * w2_height), 2) +
                                                         round(w3_weight / (w3_height * w3_height), 2) +
                                                         round(w4_weight / (w4_height * w4_height), 2) +
                                                         round(w5_weight / (w5_height * w5_height), 2) +
                                                         round(m1_weight / (m1_height * m1_height), 2) +
                                                         round(m2_weight / (m2_height * m2_height), 2) +
                                                         round(m3_weight / (m3_height * m3_height), 2) +
                                                         round(m4_weight / (m4_height * m4_height), 2) +
                                                         round(m5_weight / (m5_height * m5_height), 2)) / 10)



