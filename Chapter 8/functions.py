# # User Define functions in pyhton

# # 1.  Non-Parameterised Function
# def great():              # creating function
#     print("Hello How are you?")

# # Calling Function
# great()

# # 2. Parameterised Function
# def add2Numbers(a,b):      #parameter(a,b)
#     result = a+b
#     print("Sum is:",result)

# add2Numbers(5,3)    #arguments(5,3)

# # Create a function to add 3 numbers
# def add3Numbers(a,b,c):      #parameter(a,b,c)
#     result = a+b+c
#     print("Sum is:",result)

# add3Numbers(5,3,100)    #arguments(5,3,100)


# # Function with 'return' statement
# def add(a,b):
#     return a+b

# result = add(4,5)
# print(result)

# Function to convert celsius to Fahrenheit
def celsius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

temp_f = celsius_to_fahrenheit(25)   # calling func
print(temp_f)

# Pass Statement
def kuchbhi():
    pass       # code to be updated later
               # We can work ahead after pass and can updated it later