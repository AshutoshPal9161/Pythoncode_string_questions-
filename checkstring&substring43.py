# 43. Program to check if one string is a substring of another. 

str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')

if str2 in str1:
    print(f'"{str2}" is a substring of "{str1}"')
else:
    print(f'"{str2}" is not a substring of "{str1}"')
    