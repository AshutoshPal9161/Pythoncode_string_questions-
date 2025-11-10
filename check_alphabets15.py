#15. Program to check whether a string contains only alphabets. 

str1 = input("Enter the String: ").split()

for s in str1:
    if s.isalpha():
        print("Contain only alphabets",s)
    else:
        print("Not contain only alphabets",s)
