# 47. Program to remove punctuation from a string. 

str1 = input("Enter a string: ")
punctuations = '''!()-[]{};:'"/,<>./?@#$%^&*_~'''
no_punct = ""
for char in str1:
    if char not in punctuations:
        no_punct = no_punct + char
print("String without punctuation:", no_punct)
