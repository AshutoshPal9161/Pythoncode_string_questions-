'''2. Program to check password strength (must include length, upper, lower, digit, and 
special char).'''
import string
# Input from user 
password = input("Enter your password: ") 

has_alpha = False
has_upper = False 
has_lower = False 
has_digit = False 
has_special = False 
 
# Check each character 
for ch in password:
    if ch.isalpha():
        has_alpha = True
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True 
    if ch.isdigit(): 
        has_digit = True 
    if ch in ['!', '@', '#', '$']:  # special characters like !@#$
        has_special = True


# Print results

print(has_upper,has_alpha,has_lower,has_digit,has_special)


# Checking all conditions 
if len(password) < 8: 
    print("  Password too short! Must be at least 8 characters.") 
elif not has_upper: 
    print("  Password must include at least one uppercase letter.")
elif not has_lower: 
    print("  Password must include at least one lowercase letter.") 
elif not has_digit: 
    print("  Password must include at least one digit.") 
elif not has_special:
    print("  Password must include at least one special character (!@#$ etc.)")
elif not has_alpha:
    print("  Password must include at least one alpha character.)")     
else:
    print(" Strong password! Well done.") 



