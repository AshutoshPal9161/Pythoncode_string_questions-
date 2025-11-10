#28. Program to detect palindrome words in a given paragraph. 

sen = input('Enter the sentence: ').lower().split()
ue=[]
for w in sen:
    if w not in ue:
        ue.append(w)
for i in ue:
    if i[::-1]==i:
        print(i)
