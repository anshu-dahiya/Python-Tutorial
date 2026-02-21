# # Arguments in Python

# # 1. Required Arguments (single/multiple arguments)

# # Eg.-1
# def greetings(name):
#     print("Hello",name, "!")

# greetings("Vani")     # Vani is argument
# # greetings()          # give error required argument

# # Eg.-2
# def intro(course_name, instructor_name):
#     print("Welcome to ",course_name, "course by", instructor_name)

# intro("Python", "Megha")

# # 2. Default Arguments

# def greeting(name = "World"):           # "World" is a default value
#     print("Hello",name,"!")

# greeting()          # runs without error using default value
# greeting("Chanchal")

# # 3. Keyword Arguments (named argument)

# def divide(a,b):
#     return a/b

# result1 = divide(100,20)          # Positional Argument
# print(result1)

# result2 = divide(b= 100,a= 20)    # Keyword Argument
# print(result2)

# # 4. Arbitrary Arguments 
# # Arbitrary Positional Argument (*args)

# # Note: stores arguments as tuple

# # Eg-1
# def add_number(*args):
#     print(type(args))      # stores arguments as tuple
#     return sum(args)

# output = add_number(1,2,3,4)   # various no. of arguments can be given
# print(output)

# # Eg-2
# def greeting2(*names):
#     for name in names:
#         print(f"Hello {name}!")

# greeting2("Vani", "Megha", "Visakha")


# 4. Arbitrary Keyword Arguments (**kwargs)

# Note: stores arguments as dictionary

def print_details(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name = "Vani", age = 24, city = "Delhi")