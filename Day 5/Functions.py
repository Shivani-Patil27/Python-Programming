#1. Built in Function(Predefined Function)

# Example: WAP to implement some predefined functions?
# Name  = 'Prashant Jha'    
# sid   = 101    
# percentage = 77.7    
# Result = True    
# print(type(Name)) # type function returns the data type     
# print(type(sid))  # class of variable    
# print(type(percentage))    
# print(type(Result))    
# # id function returns the address of variable    
# print(id(Name))     
# print(id(sid))      
# print(id(percentage))    
# print(id(Result))

#2. User Defined Function:

#EX 1:
# def message(): #called function
#     print("Hello world!")
# message()#calling function
# message()
# message()

# Ex.2) WAP to implement user defined functions?

# def login():# called function  
#         username = input("Enter your username:")  
#         password = input("Enter your password:")  
#         if username ==  password:  
#             print("login successfully")   
#         else:  
#              print("Invalid credential")  
# login()#calling function 

#Ex 3:
# def add():
#     return 2+3
# print (add())
# result=add()
# print("Result=",result)

#EX 4:
# def add():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add, sub, mul, div #it will display in tuple
# result=add()
# print("Result=",result)

#Positional arguments

# def name(a,b):
#     print(a+b)
# name(2,3)

#WAP to implement user defined functions along with positional argument?

# def personalinfo(firstname,lastname): # called function   
#      print( "First name=", firstname)  
#      print( "Last name=", lastname)  
# personalinfo( "prashant", "jha") # calling function  

#Keyword argument
# def profile(fname, lname):
#     print("FirstName=",fname)
#     print("LastName=",lname)
# profile(fname="prashant", lname="jha")

#Default argument
# def nameOfCity(city ='Nagpur' ):  
#       print('City Name=', city)  
  
# nameOfCity( 'Mumbai' )  
# nameOfCity( 'Pune' )  
# nameOfCity( )#in this case default value will used  

#Variable number of arguments

# def city(*name): #(*) select all / accept all
#     print(name)
# city("Delhi","Nagpur","Mumbai","Pune","Bangalore")

#WAP to do a menu drive program using arithmetic operation(Important)
# import sys
# def addition(): # Model operation 
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print("Addition=",a+b)

# def substraction():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print("Substraction=",a-b)

# def Multiplication():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print("Multiplication",a*b)

# def division():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print("Division=",a/b)

# while True: #it will run infinity times if we didn't have base
#     print("1. Addition")
#     print("2. Substration")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice=int(input("Enter your choice:"))
#     if choice == 1:
#         addition()
#     elif choice == 2:
#         substraction()
#     elif choice == 3:
#         Multiplication()
#     elif choice == 4:
#         division()
#     elif choice == 5:
#         sys.exit()

#Factorial by using functions
# def factorial(n):  
#       if n == 0:  
#           return 1  
#       return n * factorial(n - 1)  
# print(factorial(5))  

#Prime number using functions
import math
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


# Testing with input 11
num = 11
if check_prime(num):
    print("prime")
else:
    print("not prime")