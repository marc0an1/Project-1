# Income tax calculator project
# Made by Marco Chaparro

print('Enter the gross income:')
gross_income = round(float(input()) , 2)
print('Enter the number of dependants:')
num_dep = int(input())
gross_deductions = gross_income - 10000 - (3000*num_dep)
if gross_deductions < 0: gross_deductions = 0
income_tax = gross_deductions * 0.20
print('The income tax is $', income_tax)
