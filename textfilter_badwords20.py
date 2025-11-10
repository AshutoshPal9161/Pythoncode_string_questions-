#20. Program to detect and replace bad words (text filtering). 

word = input("Enter the sentence: ").split()
bad_words = ["badword", "stupid", "idiot", "dumb"]

for w in word:
    if w in bad_words:
        w = "***"
    print(w,end=" ")
