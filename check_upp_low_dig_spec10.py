#10. Program to count uppercase, lowercase, digits, and special characters in a string.
word = input("Enter the string: ")
u=0
l=0
d=0
sp=0

for w in word:
    if w.isupper():
        u+=1
    elif w.islower():
        l+=1
    elif w.isdigit():
        d+=1
    else:
        sp+=1
print("Uppercase: ",u)
print("Lowercase: ",l)
print("Digits: ",d)
print("Specialcase: ",sp)
    
