#33. Program to validate an email address format. 

emails = input('enter the email id: ')
l=False
n=False
sy=False
d=False

for email in emails:
    if email.isdigit():
         l=True
    elif email.islower():
         n=True
    elif email in "@":
       sy=True
    elif email.endswith('gmail.com'):
         d=True
    else:
        print("not valid")

if l!=False:
    print('write in lowercase')
elif n!=False:
    print('enter some number')
elif sy!=False:
    print('add @ symbol')
elif d!=False:
    print('add in last gmail.com')





