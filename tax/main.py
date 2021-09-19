print("-------------------------------------------------------------------------")
print("|\t\t\t\t\tWELCOME TO THAILAND TAX CALCULATION\t\t\t\t\t|")
print("|\t\t\t\t      PERSONAL INCOME TAX YEAR 2020\t\t\t\t\t    |")
print("-------------------------------------------------------------------------")
print("********Please Enter all values if none TYPE '0'(ZERO)*******************")
print("*********FOR ALL CALCULATIONS WILL BE IN 'THAI BAHT'*********************")
print("*** THERE ARE 3 PARTS IN THE PROGRAM")
print("*** PART.1 CALCULATE FOR NET INCOME ")
print("*** PART.2 CALCULATE FOR THE DEDUCTIBLE")
print("*** PART.3 CALCULATE FOR PAYABLE TAX\n")

print("******************PART.1 CALCULATE FOR NET INCOME************************")

# ใส่จำนวน เงินเดือนท้ังปี
Annual_salary = int(input("1.1. Enter Your Annual Salary =: "))

# ใส่จำนวน รายได้อื่น ๆ
Other_income = int(input("1.2. Enter Other income =: "))

# คำนวน รวมเงินได้ที่นำไปคำนวณภาษี
print("\n####Total income =:", Annual_salary+Other_income)
total_salary = Annual_salary + Other_income
print("-------------------------------------------------------------------------")

# ยกเว้น เงินสะสมกองทุนสำรองเลี้ยงชีพ
print("1.3. Except for provident fund contributions")
# หักได้ 15% ของเงินได้ทั้งหมด แต่ไม่เกิน 500,000 บาท
print("(15% deductible of total income but not more than 500,000 baht)")
# ใส่จำนวน ยกเว้น เงินสะสมกองทุนสำรองเลี้ยงชีพ
Except_provident = int(input("Enter your amount =: "))
eExcept_provident = total_salary * (15/100)
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดาน สูงสุด 15% แล้ว หักเงินสำรองเลี้ยงชีพ ที่เกิน 10,000 บาท
if Except_provident > eExcept_provident:
    Except_provident = int(eExcept_provident)
    print("!!More than 15% of total income is", Except_provident)
    # หักเงินสำรองเลี้ยงชีพ ที่เกิน 10,000 บาท
    print("**Less provident allowance exceeding 10,000 baht =:", Except_provident - 10000)
else:
    # หักเงินสำรองเลี้ยงชีพ ที่เกิน 10,000 บาท
    print("**Less provident allowance exceeding 10,000 baht =:", Except_provident - 10000)

# ยกเว้น เงินสะสมกบข. + กองทุนสงเคราะห์ครูเอกชน
print("\n1.4. Except GPF savings + Private Teacher Aid Fund")
# หักได้ไม่เกิน 500,000 บาท
print("(Can deduct no more than 500,000 baht)")
# ใส่จำนวน ยกเว้น เงินสะสมกบข. + กองทุนสงเคราะห์ครูเอกชน
Except_GPF = int(input("Enter your amount =: "))
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดาน สูงสุด
if Except_GPF > 500000:
    print("!!More than 500,000 baht")
    print("**Can deduct only =: 500000")
    Except_GPF = 500000
else:
    print("Except GPF savings + Private Teacher Aid Fund deduction =:", Except_GPF)

# ยกเว้น กรณีอายุตั้งแต่ 65 ปี หรือบุคคลพิการ
print("\n1.5. Except for the age of 65 or persons with disabilities")
# หักได้ไม่เกิน 190,000 บาท
print("(Can deduct no more than 190,000 baht)")
# ใส่จำนวน ยกเว้น กรณีอายุตั้งแต่ 65 ปี หรือบุคคลพิการ
Except_AGE_65 = int(input("Enter your amount =: "))
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดาน สูงสุด
if Except_AGE_65 > 190000:
    print("!!More than 190,000 baht")
    print("**Can deduct only =: 190000")
    Except_AGE_65 = 190000
else:
    print("Except for the age of 65 or persons with disabilities deduction =:", Except_AGE_65)

# รวมเงินได้ที่ได้รับการยกเว้น
print("\n####Include exempt income from(1.3,1.4,1.5)=:", (Except_provident-10000)+Except_GPF+Except_AGE_65)
Include_exempt_income = (Except_provident-10000)+Except_GPF+Except_AGE_65
print("-------------------------------------------------------------------------")

# คงเหลือ เงินได้ก่อนหักค่าใช้จ่าย
print("**Remaining income before deducting expenses =:", total_salary - Include_exempt_income)
Remaining_income = total_salary - Include_exempt_income

# หักค่าใช้จ่าย 50% แต่ไม่เกิน 100,000 บาท
print("**Less expense 50% but not exceeding 100,000 baht =: 100000")

# ยอดคงเหลือหลังจากหัก ข้อยกเว้น และหักค่าใช่้จ่าย 100,000 บาท
print("\n####Your balance (net income) =:", Remaining_income - 100000)
print("-------------------------------------------------------------------------")

print("\n****************PART.2 CALCULATE FOR THE DEDUCTIBLE***********************")

# ใส่ค่า ค่าลดหย่อนส่วนตัว
print("2.1 Personal allowance =: 60,000")
Personal_Al = 60000

# ใส่ค่า ค่าลดหย่อนบุตร :
print("\n2.2 Child allowance")
Child_no = int(input("How many children do you have? =: "))
print("(The deductible is 30,000 baht per person.)")
# หักลดหย่อนได้คนละ 30,000 บาท
Child_De = Child_no * 30000
print("Child allowance =:", Child_De)

# ค่าลดหย่อนบุตรบุญธรรม ใส่ได้ไม่เกิน 3 คน
print("\n2.3 Adopted child allowance not more than 3 ")
Adt_child_no = int(input("How many Adopted children do you have? =: "))
print("(The deductible is 30,000 baht per person.)")
# หักลดหย่อนได้คนละ 30,000 บาท
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดาน 3 คน 90000 บาท
if Adt_child_no > 3:
    print("!!More than 3 person")
    print("Adopted child allowance can be only =: 90000")
    Adt_child_De = 90000
else:
    Adt_child_De = Adt_child_no * 30000
    print("Adopted child allowance =:", Adt_child_De)

# ค่าลดหย่อนบิดา-มารดา
print("\n2.4 Parent allowance not more than 2")
Parent_no = int(input("How many parents do you still have? =: "))
print("(The deductible is 30,000 baht per person.)")
# หักลดหย่อนได้คนละ 30,000 บาท
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดาน 2 คน 60000 บาท
if Parent_no > 2:
    print("!!More than 2 person ")
    print("Adopted child allowance can be only =: 60000")
    Parent_De = 60000
else:
    Parent_De = Parent_no * 30000
    print("Parents allowance =:", Parent_De)

# ค่าลดหย่อนคู่สมรส
print("\n2.5 Spouse deduction")
# หากแต่งงาน ลดได้ 60000 บาท
Spouse_bool = str(input("Do you have spouse? (y/n)"))
# if else หากไม่ต้อง yes ให้เป้น 0 บาท
if Spouse_bool == "y":
    print("Spouse deduction is =: 60000")
    Spouse_de = 60000
else:
    print("!!No Spouse deduction")
    Spouse_de = 0

# ค่าฝากครรภ์และคลอดบุตร
print("\n2.6 Antenatal and childbirth fees")
# หักได้ไม่เกิน 60,000 บาท
print("(Can deduct no more than 60,000 baht)")
Alter_childbirth = int(input("Enter amount =: "))
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดานสุูงสุด 60000 บาท
if Alter_childbirth > 60000:
    print("!!More than 60,000 baht")
    print("Antenatal and childbirth fees can deduct only 60000")
    Alter_childbirth = 60000
else:
    print("Antenatal and childbirth fees =:", Alter_childbirth)

# เงินประกันสุขภาพบิดา-มารดา
print("\n2.7 Health insurance, father - mother")
# หักได้ไม่เกิน 15,000 บาท
print("(Can deduct no more than 15,000 baht)")
Health_Insurance_Parent = int(input("Enter amount =: "))
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดานสุูงสุด 15000 บาท
if Health_Insurance_Parent > 15000:
    print("!!More than 15,000 baht")
    print("Health insurance, father - mother can deduct only 15000")
    Health_Insurance_Parent = 15000
else:
    print("Health insurance, father - mother deduction =:", Health_Insurance_Parent)

# เงินประกันสุขภาพ
print("\n2.8 Your health insurance payments")
# หักได้ไม่เกิน 15,000 บาท
print("(Can deduct no more than 15,000 baht)")
Health_Insurance = int(input("Enter amount =: "))
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดานสุูงสุด 15000 บาท
if Health_Insurance > 15000:
    print("!!More than 15,000 baht")
    print("Your health insurance payments can deduct only 15000")
    Health_Insurance = 15000
else:
    print("Your health insurance payments deduction =:", Health_Insurance)

# เงินประกันชีวิต
print("\n2.9 Your Life insurance money")
# ไม่เกิน 100,000 บาท หากรวมกับ เงินประกันสุขภาพ
print("(Can deduct no more than 100,000(Health + Life insurance) baht ")
Life_Insurance = int(input("Enter amount =: "))
dLife_Insurance = Life_Insurance + Health_Insurance
# if else หากเกินจากที่กำหนด
# หากเกิน ก็จะกำหนดตามเพดานสุูงสุด 100000 - 15000 = 85000 บาท
if dLife_Insurance > 100000:
    print("!!(Health + Life insurance)More than 100,000 baht")
    print("Your health insurance payments can deduct only =:", 100000 - Health_Insurance)
    Life_Insurance = 100000 - Health_Insurance
else:
    print("Your Life insurance money deduction =:", Life_Insurance)

# เงินสะสมกองทุนสำรองเลี้ยงชีพ 10000
print("\n2.10 Provident fund contribution =: 10000")
Provident_Fund = 10000

# คำนวน รวมค่าลดหย่อน
Total_Deductible = Personal_Al + Child_De + \
                   Adt_child_De + Parent_De + \
                   Spouse_de + Alter_childbirth + \
                   Health_Insurance_Parent + \
                   Health_Insurance + \
                   Life_Insurance + \
                   Provident_Fund

# คำนวน รวมค่าลดหย่อน
print("\n####Total deductible =:", Total_Deductible)


print("\n*****************PART.3 CALCULATE FOR PAYABLE TAX*************************")

# เงินเดือน ค่าจ้าง โบนัส บำนาญ อื่นๆ
print("3.1. Salaries, wages, bonuses, pensions, etc =:", total_salary)

# หักเงินที่ได้รับยกเว้น
print("3.2. Include exempt income from(1.3,1.4,1.5)=:", Include_exempt_income)

# คงเหลือ
print("3.3. Remaining income before deducting expenses =:", Remaining_income)

# หักค่าใช้จ่าย (ร้อยละ 50 ของ 3. แต่ไม่เกิน 100,000 บาท
print("3.4. Less expense 50% but not exceeding 100,000 baht =: 100000")

# คงเหลือ หลังหักค่าใช้จ่าย (ร้อยละ 50 ของ 3. แต่ไม่เกิน 100,000 บาท
print("3.5. Your balance (net income) =:", Remaining_income - 100000)

# รวมค่าลดหย่อน
print("3.6. Total Deduction fee =:", Total_Deductible)

# รายได้สุทธิคงเหลือ หลังรวมค่าลดหย่อน
net_income_tax = (Remaining_income - 100000) - Total_Deductible
print("#### Net Income for tax calculation =:", net_income_tax)

print("-----------------------------------------------------------------------")
print("|              TABLE FOR PERSONAL TAX RATE YEAR 2020                  |")
print("-----------------------------------------------------------------------")
print("|      NET INCOME       | MIN NET INCOME | TAX RATE | TAX ACCUMULATED |")
print("-----------------------------------------------------------------------")
print("|     0 - 150,000       |        0       |    0%    |        0        |")
print("|   150,001 - 300,000   |     150,000    |    5%    |      7,500      |")
print("|   300,001 - 500,000   |     300,000    |    10%   |      27,500     |")
print("|   500,001 - 750,000   |     500,000    |    15%   |      65,000     |")
print("|  750,001 - 1,000,000  |     750,000    |    20%   |     115,000     |")
print("| 1,000,001 - 2,000,000 |    1,000,000   |    25%   |     365,000     |")
print("| 2,000,001 - 5,000,000 |    2,000,000   |    30%   |    1,265,000    |")
print("|  more than 5,000,000  |    5,000,000   |    35%   |       -         |")
print("-----------------------------------------------------------------------")

# if else การคำนวนภาษี ตามภาษีขั้นบันได อ้างอิงจากตารางด้านบน
if net_income_tax <= 150000:
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -       0       )*   0%   ] +             0            |")
    print("-----------------------------------------------------------------------")
    print("|                   ---> TAX TO BE PAID IS =: 0                       |")
    print("-----------------------------------------------------------------------")

elif (net_income_tax > 150000) and (net_income_tax <= 300000):
    net_income_tax_calculation = round((net_income_tax - 150000) * (5/100), 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -    150,000    )*   5%   ] +             0            |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                      |")
    print("-----------------------------------------------------------------------")

elif (net_income_tax > 300000) and (net_income_tax <= 500000):
    net_income_tax_calculation = round(((net_income_tax - 300000) * (10/100)) + 7500, 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -    300,000    )*  10%   ] +          7,500           |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                    |")
    print("-----------------------------------------------------------------------")


elif (net_income_tax > 500000) and (net_income_tax <= 750000):
    net_income_tax_calculation = round(((net_income_tax - 500000) * (15/100)) + 27500, 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -    500,000    )*  15%   ] +         27,500           |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                    |")
    print("-----------------------------------------------------------------------")

elif (net_income_tax > 750000) and (net_income_tax <= 1000000):
    net_income_tax_calculation = round(((net_income_tax - 750000) * (20/100)) + 65000, 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -    750,000    )*  20%   ] +         65,000           |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                    |")
    print("-----------------------------------------------------------------------")


elif (net_income_tax > 1000000) and (net_income_tax <= 2000000):
    net_income_tax_calculation = round(((net_income_tax - 1000000) * (25/100)) + 115000, 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -   1,000,000   )*  25%  ] +         115,000          |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                   |")
    print("-----------------------------------------------------------------------")

elif (net_income_tax > 2000000) and (net_income_tax <= 5000000):
    net_income_tax_calculation = round(((net_income_tax - 2000000) * (30/100)) + 365000, 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -   2,000,000   )*  30%  ] +         365,000          |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                   |")
    print("-----------------------------------------------------------------------")

elif net_income_tax > 5000000:
    net_income_tax_calculation = round(((net_income_tax - 5000000) * (35/100)) + 1265000, 2)
    print("| [(Net income - Min net income)*TAX RATE] + Previous Tax Accumulated |")
    print("| [( ", net_income_tax, "  -   5,000,000   )*  35%  ] +       1,265,000          |")
    print("-----------------------------------------------------------------------")
    print("|              ---> TAX TO BE PAID IS =: ", net_income_tax_calculation, "                  |")
    print("-----------------------------------------------------------------------")
