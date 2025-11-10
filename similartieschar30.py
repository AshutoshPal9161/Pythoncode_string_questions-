#30. Program to find similarity between two strings.

str1 = input('enter the first string: ').lower()
str2 = input('enter the second string: ').lower()

for s in str1:
    if s in str2:
        print(s,end=" ")

