#3. Program to find the longest word in a sentence.
lw=" "
large_word=input("Enter the string: ").split()
for w in large_word:
    if len(w)>len(lw):
        lw=w

print("Largest word is: ",lw)
