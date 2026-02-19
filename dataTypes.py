# Data types in python
a = 1
b = 1
print(a+b)
print(type(a))  # checking data type: int

c = "1"
d = "1"
print(c+d)
print(type(c))  # checking data type: string


# Basic Data types in python:
# 1. Numeric
a1 = 1      #1a. integer
a2 = 1.5    #1b. float
print(type(a2))

a3 = complex(3,5)  #1c. complex
print(type(a3))

# 2. Sequence
b1 = "Gin"   #2a. string
print(type(b1))
b2 = [1,4,7,26,106,'David']   #2b. list
print(type(b2))
b3 = (1,4,7,26,106,'David')   #2c. tuple
print(type(b3))

# 3. Dictionary
my_dictionary = {'name': 'Jon', 'age': 24, 'city': 'Delhi'}
print(type(my_dictionary))

# 4. Sets
my_sets = {1,4,7,26,106,'David'}
print(type(my_sets))

# 5. Boolean
bool1 = True
bool2 = False
print(type(bool1))

# 6. Binary
# bytes, bytearray, memoryview
byte1 = b'Ram'
print(type(byte1))