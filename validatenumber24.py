#24. Program to validate a mobile number (using regex). 

num = input("Enter the number: ")
if num.isdigit() and len(num)==10:
    print("valid number=",num)
else:
    print("Invalid number=",num)
