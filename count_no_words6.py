#6. Program to count the number of words in a sentence. 
sen = input("Enter the sentence: ").split()
c=0

for w in sen:
    c+=1

print("Number of words in sentence is: ",c)
