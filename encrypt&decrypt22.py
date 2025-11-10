#22. Program to encrypt and decrypt strings using a simple Caesar cipher. 

word = input("Enter the sentence: ").split()

for w in word:
        n=len(w)
        if n>=1 and n<3:
            r = w.replace(w,"***")
            print(r,end=" ")
        elif n>=3 and n<5:
            r = w.replace(w,"#####")
            print(r,end=" ")
        elif n>=5 and n<7:
            r = w.replace(w,"%%%%%")
            print(r,end=" ")
        elif n>=7 and n<9:
            r = w.replace(w,"&&&&&&&")
            print(r,end=" ")
        else:
            r = w.replace(w,"#@*^%$&^%*&^")
            print(r,end=" ")
        
        
