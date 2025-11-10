#31. Program to compare two strings lexicographically. 


str1 = input('enter the first string: ')
str2 = input('enter the second string: ')

if str1 > str2:
    print(f'"{str1}" comes before "{str2}"')
elif str2 > str1:
    print(f'"{str1}" comes after "{str2}"')
else:
    print("Both strings are equal")
