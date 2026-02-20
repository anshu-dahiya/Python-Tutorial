# # Q1: Leap Year: Write a simple program to determine if a given
# #     year is leap year or not. Using user input

# # Note:
# # Leap year occurs once every four years.
# # A year is leap year if it is divisible by 4,
# # but not if it is divisible by 100 unless it also div. by 400

# year = int(input("Enter the Year (eg. 2024): "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is Leap Year")
# else:
#     print(f"{year} is Normal Year")


# # Q2. 'Login Authentication' using conditinal statement. Assume you
# # have predefined username and password.
# # Write a program that prompts the user to enter a username and password
# # and checks whether theynn match.
# # Provide appropriate messages for following cases:
# # --> Both username and password are correct.
# # --> Username is correct but password is incorrect.
# # --> Username is incorrect

# users = {
#     'Tim'  : {'pass' : 'Tim123'},
#     'David': {'pass' : 'David123'},
#     'Vani' : {'pass' : 'Vani123'},
# }

# username = input("Username: ")
# password = input("Password: ")

# if username in users:
#     if password == users[username]['pass']:
#         print("Login Successful!")
#     else:
#         print("Password Incorrect")
# else:
#     print("Username Incorrect")
        

# Q3.'Admission Eligility': A University has the following eligibility
# criteria for admission:
# --> Marks in Maths >= 65
# --> Marks in Physics >= 55
# --> Marks in Chemistry >= 50
# --> Total marks in all three subjects >= 180 OR Total marks 
#     Maths and Physics >= 140
# Write a program that takes marks in three subjects as input and 
# prints whether the student is eligible for admission.

print("Enter PCM Marks out of 100")
maths = int(input("Enter your Maths Marks: "))
physics = int(input("Enter your Physics Marks: "))
chemistry = int(input("Enter your Chemistry Marks: "))
total = (maths + physics + chemistry)

if (
    maths >= 65 and 
    physics >= 55 and 
    chemistry >= 50 and 
    (total >= 200 or (maths+physics) >= 140)
    ):
    print("🎉 Congratulations! You are eligible for admission.")
else:
    print("❌ Get lost don't come here")
