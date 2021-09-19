print("****************PART.2 CALCULATE FOR THE DEDUCTIBLE***********************")

print("\n2.1 Personal allowance =: 60,000")
Personal_Al = 60000

print("\n2.2 Child allowance")
Child_no = int(input("How many children do you have? =: "))
print("(The deductible is 30,000 baht per person.)")
Child_De = Child_no * 30000
print("Child allowance =:", Child_De)

print("\n2.3 Adopted child allowance not more than 3 ")
Adt_child_no = int(input("How many Adopted children do you have? =: "))
print("(The deductible is 30,000 baht per person.)")
if Adt_child_no > 3:
    print("!!More than 3 person")
    print("Adopted child allowance can be only =: 90000")
    Adt_child_De = 90000
else:
    Adt_child_De = Adt_child_no * 30000
    print("Adopted child allowance =:", Adt_child_De)

print("\n2.4 Parent allowance not more than 2")
Parent_no = int(input("How many parents do you still have? =: "))
print("(The deductible is 30,000 baht per person.)")
if Parent_no > 2:
    print("!!More than 2 person ")
    print("Adopted child allowance can be only =: 60000")
    Parent_De = 60000
else:
    Parent_De = Parent_no * 30000
    print("Parents allowance =:", Parent_De)

print("\n2.5 Spouse deduction")
Spouse_bool = str(input("Do you have spouse? (y/n)"))
if Spouse_bool == "y":
    print("Spouse deduction is =: 60000")
    Spouse_de = 60000
else:
    print("!!No Spouse deduction")
    Spouse_de = 0

print("\n2.6 Antenatal and childbirth fees")
print("(Can deduct no more than 60,000 baht)")
Alter_childbirth = int(input("Enter amount =: "))
if Alter_childbirth > 60000:
    print("!!More than 60,000 baht")
    print("Antenatal and childbirth fees can deduct only 60000")
    Alter_childbirth = 60000
else:
    print("Antenatal and childbirth fees =:", Alter_childbirth)

print("\n2.7 Health insurance, father - mother")
print("(Can deduct no more than 15,000 baht)")
Health_Insurance_Parent = int(input("Enter amount =: "))
if Health_Insurance_Parent > 15000:
    print("!!More than 15,000 baht")
    print("Health insurance, father - mother can deduct only 15000")
    Health_Insurance_Parent = 15000
else:
    print("Health insurance, father - mother deduction =:", Health_Insurance_Parent)

print("\n2.8 Your health insurance payments")
print("(Can deduct no more than 15,000 baht)")
Health_Insurance = int(input("Enter amount =: "))
if Health_Insurance > 15000:
    print("!!More than 15,000 baht")
    print("Your health insurance payments can deduct only 15000")
    Health_Insurance = 15000
else:
    print("Your health insurance payments deduction =:", Health_Insurance)

print("\n2.9 Your Life insurance money")
print("(Can deduct no more than 100,000(Health + Life insurance) baht ")
Life_Insurance = int(input("Enter amount =: "))
dLife_Insurance = Life_Insurance + Health_Insurance
if dLife_Insurance > 100000:
    print("!!(Health + Life insurance)More than 100,000 baht")
    print("Your health insurance payments can deduct only =:", 100000 - Health_Insurance)
    Life_Insurance = 100000 - Health_Insurance
else:
    print("Your Life insurance money deduction =:", Life_Insurance)

print("\n2.10 Provident fund contribution =: 10000")
Provident_Fund = 10000

Total_Deductible = Personal_Al + Child_De + Adt_child_De + Parent_De + Spouse_de + Alter_childbirth + Health_Insurance_Parent + Health_Insurance + Life_Insurance + Provident_Fund
print("\n####Total deductible =:", Total_Deductible)
