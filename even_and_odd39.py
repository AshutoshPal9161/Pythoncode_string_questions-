#39. Program to print characters at even and odd positions separately. 

str1 = input('Enter the string: ')
even=""
odd=""

for w in range(len(str1)):
    if w%2==0:
        even+=str1[w]
    else:
        odd+=str1[w]
print("even position=",even)
print("odd position=",odd)
