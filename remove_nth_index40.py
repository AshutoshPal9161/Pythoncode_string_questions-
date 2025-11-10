#40. Program to remove the nth index character from a string. 


str1 = input('Enter the string: ')
r = int(input("Enter the index to remove char: "))

for w in range(len(str1)):
    if r==w:
        str1=str1.replace(str1[w],"")
print(str1)
