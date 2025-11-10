#26. Program to count word frequency and display top 5 words. 

word = input("Enter the sentence: ").lower().split()

nw=[]
for w in word:
    c=0
    if w not in nw:
        c=word.count(w)
        print(w,"---->",c,end="   ")
        nw.append(w)
        n2=sorted(nw,reverse=True)

