#12. Program to check if a string is a palindrome. 

word = input("Ente the string: ")
s=word
r=" "

for w in range(len(word)-1,-1,-1):
    r+=word[w]
print(r)

if s==r:
    print("Palindrome String")
else:
    print("Not palindrome string ")
