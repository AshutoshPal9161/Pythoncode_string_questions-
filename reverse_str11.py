#11. Program to reverse a string. 

str1 = input("Enter the String: ")
print("The reverse string is:",str1[::-1])

r=" "
for s in range(len(str1)-1,-1,-1):
     r= r+str1[s]

print("The reverse string is:",r)

