# # Condition Statements in Python

# # 1. if statement
# # if statement only works in True condition

# a = 26
# b = 108
# if b > a:
#     print("b is greater than a")

# age = int(input("Enter your age: "))
# if age > 19:
#     print("You are a adult")

# # 2. if-else statement
# # else handles false condition

# age = int(input("Enter your age: "))
# if age > 19:
#     print("You are a adult")
# else:
#     print("You are Chota Bacha")

# # 3. if-elif-else statement
# # multiple condtion

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A+")
# elif marks >= 80:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: B")
# elif marks >= 40:
#     print("Grade: C")
# else:
#     print("Grade: D")

# # 4. Nested if-else statement
# # if-else inside if-else statement
# # multiple conditions depend on each other

# number = int(input("Enter a number: "))

# if number > 0:
#     if number % 2 == 0:
#         print("This is a Even number")
#     else:
#         print("This is a Odd number")
# else:
#     if number == 0:
#         print("Number is Zero")
#     else:
#         print("Number is Negative")

# # 5. Conditional Expressions (ternary operator)

# age = int(input("Enter your age: "))
# status = "Major" if age >= 18 else "Minor"
# print(status)
        

# HW.: What is expected output and reason?
value = None

if value:
    print("Value is True")
else:
    print("Value is False")
