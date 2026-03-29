#Finally block will executed whether try block generate error or not
# try:
#     a=int(input("Enter first integer number:"))
#     b=int(input("Enter second integer number:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as  message:
#     print("Enter correct number:",message)
# finally:
#     print ("I will always executed")

#user defined exception by raise keyword
# bank_bal = 500
# if bank_bal < 2000:
#     raise Exception("Your account balance is below a accessing limit")
# else:
#     print("Your amount has withdrawal")