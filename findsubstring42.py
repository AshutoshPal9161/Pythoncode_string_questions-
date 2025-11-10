#42. Program to find all substrings of a string. 

s1 = input('Enter the string: ')

for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        print(s1[i:j])
        
