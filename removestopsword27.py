#27. Program to remove stopwords from a sentence (using a list of stopwords). 

word = input("Enter the word: ").lower().split()
l=['and','the','is','in']
new_word=[]
for w in word:
    if w not in l:
        new_word.append(w)
print(new_word)
