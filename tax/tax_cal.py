net_income_tax =5850000
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
