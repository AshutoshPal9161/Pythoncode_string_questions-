#25. Program to extract hashtags and mentions from a tweet text. 

word = input("Enter the tweet text: ").split()
h=""
m=""
for w in word:
    if w.startswith('@'):
        m=m+"\n"+w
    elif w.startswith('#'):
        h+="\n"+w
print("hashtag:",h)
print()
print("mention: ",m)
