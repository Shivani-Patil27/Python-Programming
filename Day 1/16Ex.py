#WAP to accept days and check the working day or weekend


day = input("Enter Day:")
if day == "saturday" or day == "SUNDAY" or day == "SATURDAY" or day == "sunday":
    print("Weekend")
else:
    print("Working day")
