# WAP to calculate gross salary from basic salary(HRA=30%,TA=40%,DA=20%)

basic_salary = float(input("Enter Basic Salary: "))

hra = 0.30 * basic_salary
ta = 0.40 * basic_salary
da = 0.20 * basic_salary

gross_salary = basic_salary + hra + ta + da

print("HRA:", hra)
print("TA:", ta)
print("DA:", da)
print("Gross Salary:", gross_salary)