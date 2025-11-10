#21. Program to check whether a URL starts with https://. 

url = input("Enter the URL: ")
if url.startswith('https://') and url.endswith('.com'):
    print("Vaild URL")
else:
    print('not valid')
