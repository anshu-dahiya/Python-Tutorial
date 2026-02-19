# Assignment - 1

# Q1: Write a Python program that prints the following text exactly as it appears:
# Python is fun.
# "Quotes" and 'single quotes' can be  tricky.

print("Python is fun.")
print('''"Quotes" and 'single quotes' can be tricky.''')  # way1: triple quotes can be used
print("\"Quotes\" and 'single quotes' can be tricky.")  # way2: backword slash can be used

print("Python is fun.\n \"Quotes\" and 'single quotes' can be tricky.")  # Opitmised Way

# Q2: For a bussiness create 3 variables to store- name, age, and city.
#     Then print a sentence that uses these variables.

name = "Tim"
age = 24
city = "Delhi"
print("Hey i am",name,"i am",age,"years old. I live in",city)

print(f"Hey i am {name} i am {age} years old. I live in {city}")  #optimised way