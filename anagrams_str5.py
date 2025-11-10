#5. Program to check if two strings are anagrams
s1=input("Enter the First String: ")
s2=list(input("Enter the Second String: "))
ana=0
for s in s1:
    if s in s2:
        ana=1
    else:
        ana=0
        break

if ana!=1:
    print("NOt anagrams string")
else:
        print("anagrams string")

    

