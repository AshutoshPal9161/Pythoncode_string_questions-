#23. Program to find all email IDs from a text (using regex). 

text = input("Enter the text: ").split()

for w in text:
        if w.endswith('@gmail.com'):
            print(w)
