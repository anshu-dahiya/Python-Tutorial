# # Strings in Python
# # strings - characters written in single, double and triple quotes

# name = "Vani"       # creating string
# print(name)

# print(type(name))   # checking data type

# print("Hello world")
# print("It's easy")

# print(''' "kw-double Qoutes" ''')

# print(" \"kw-double Qoutes\" ")

# # Formated strings
# # 1. Old style formatting - % operator

# name = "Vani"
# age = 24
# print("My name is %s and I'm %d" % (name,age))  # %s for strings, %d for numbers

# # 2. str.format() method

# name = "Vani"
# age = 24
# print("My name is {} and I'm {}".format(name,age))  

# #you can reference variables by index or keyword
# print("My name is {0} and I'm {1}".format(name,age))  #index
# print("My name is {1} and I'm {0}".format(name,age))   # wrong output   

# print("My name is {name} and I'm {age}".format(name="Manya",age="22")) #keyword 

# # 3. f-strings

# name = "Vanshika"
# age = 25
# print(f"My name is {name} and I'm {age}")

# print(f"My age after 5 years will be {age + 5}")


# # Escape Characters - backslash with characters
# print(''' "kw-double Qoutes" ''')

# print(" \"kw-double Qoutes\" ")     # double qoutes using \
# print(" \'kw-single Qoutes\' ")     # single qoutes using \

# print("Hello\nWorld")       # new line by \n
# print("Hello\tWorld")       # tab - space by \t


# String Operators in Python
a = "Hello"
b = "Python"

print(a+b)     # concatenate
print(a*2)     # multiple copies
# [] - slice, [:] - range   -- scroll below

if "H" in a:
    print("Yes")
else:
    print("No")

if "i" not in a:        # reverse result
    print("Yes")
else:
    print("No")

print(r"Hello\nWorld")  # Raw string: suppress escape chars
