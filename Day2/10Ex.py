#Basic examples of if else statements
username=input("Enter Username:")
password=input("Enter password:")
if username==password:
    print("login successful")
else:
    print("Invalid login")
#
brand=input("Enter your colddrink name either in upper case or in lower case but not combine:")
if brand=="pepsi" or brand=="PEPSI":
    print("swag")
elif brand=="dew" or brand=="DEW":
    print("dar age jeet hai")
elif brand=='thusup' or brand=='THUMSUP':
    print('taste the thunder')
else:
    print('go with your brand')
#Finding Smallest Numbers
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Bigger Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else:
    print("Biggest Number is:",n3)
#Finding Smallest Number
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1<n2 and n1<n3:
    print("Smallest Number is:",n1)
elif n2<n3:
    print("Smallest Number is:",n2)
else:
    print("Smallest Number is:",n3)
