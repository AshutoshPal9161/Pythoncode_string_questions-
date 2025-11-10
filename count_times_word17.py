#17. Program to count how many times each word appears in a paragraph.(later) 

str1 = "todays digital digital landscape mastering Java Java programming"
li1=str1.split()
li=str1.split()
c=0
print(li1,end=" ")
print()
print(li,end=" ")
print()

for r in li1:
    for s in li:
        if r in s:
            c+=1
    print(r,":",c)
    c=0

