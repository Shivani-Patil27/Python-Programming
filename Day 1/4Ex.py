#WAP to accept three paper marks and calculate total,percentage and if percentage is greater then equal to 60 he/she is eligible for placement else not eligible


math = 60
chem = 70
phy = 60
total = math + chem + phy
percentage = total / 3.0
print("total =", total)
print("percentage =", percentage)
if percentage >= 60:
    print("you are eligible for placement")
else:
    print("you are not eligible")
    