#37. Program to find the most frequent word in a sentence. 

str1 = input("ENter the string: ").lower().split()
ue=""

for s in str1:
    c=0
    if s not in ue:
        c=str1.count(s)
        if c>2:
             print(s,"-->",c,"times")
        ue+=s
