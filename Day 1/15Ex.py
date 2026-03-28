#WAP to accept one single digit and check the entered number is positive,negative,zero

N = int(input("Enter single digit :"))
if N > 0:
    print("Entered number is Positive")
if N < 0:
    print("Negative number")
if N == 0:
    print("Zero")