#9. Program to count the number of vowels and consonants in a string.

n = input("Enter the string:").lower()
c=0
v=0
for w in n:
    if w in ['a','e','i','o','u']:
        v+=1
    else:
        c+=1


print("Total vowel is=",v)
print("Total consonent is=",c)
