#41. Program to interchange the first and last characters of a string. 

str1 = input("Enter the string: ")
str2 = input("Enter the string: ")

#print(str2[1:-1])
if len(str1) < 2:
    print("String too short to swap.")
else:
    swapped = str1[-1] + str1[1:-1] +  str1[0]
print(swapped)
    
