#35. Program to remove duplicate characters from a string. 

sen = input("Enter the string: ")
ue=""
for s in sen:
    if s not in ue:
        ue+=s
        #r=s.replace(s,"")
print(ue)
