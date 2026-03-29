#Basic Example
# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value")

#Handling multiple different kinds of exception with single except block.
# try:
#     a=int(input("Enter first integer number:"))
#     b=int(input("Enter second integer number:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

#The concept of default except block,generally we used for writing normal message or showing normal error
# try:
#     a=int(input("Enter first integer number:"))
#     b=int(input("Enter second integer number:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# except:
#     print("This is default part of except block")

# try:
#     a=int(input("Enter first integer number:"))
#     b=int(input("Enter second integer number:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# else:
#     print ("Everything is okay")

#Nested try except block 
# try:
#     a=int(input("Enter first number:"))
#     b=int(input("Enter second number:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)