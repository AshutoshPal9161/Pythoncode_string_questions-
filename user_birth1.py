# Program to create a username from full name and birth year.
user_name= input("Enter the User name: ")
birth_year=input("Enter the birth year: ")

user_part=user_name.strip().split()
if len(user_part)>=2:
    first_name=user_part[0].lower()
    last_name=user_part[-1].lower()
    username=first_name+last_name+birth_year
else:
    username=user_part.lower()+birth_year

print("User name is: ",username)
