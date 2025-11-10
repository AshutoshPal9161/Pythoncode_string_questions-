n=int(input('Enter the any number: '))
s=0
while n>0:
    r= n%10
    n= n//10
    s= s+r
print("Sum of digits is: ",s)
