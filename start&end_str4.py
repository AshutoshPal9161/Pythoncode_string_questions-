#4. Program to check if a string starts and ends with the same character.


w=input("Enter the string: ").split()
for c in w:
    if c[0]==c[-1]:
        print("start and ends is ",c)
    else:
        print("not same",c)
