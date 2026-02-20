# Operators

# 1. Arithmetic Operators
a = 5
b = 3
print(a+b)  # addition
print(a-b)  # substraction
print(a*b)  # multiplication
print(a/b)  # division
print(a%b)  # modulus(show remider)

# 2. Comparison Operators - output is boolean value (T/F)
a = 5
b = 3
print(a > b)    #greater than
print(a < b)    #less than
print(a == b)   #equals to
print(a != b)   #not equals to

# 3. Assignment Operators
a = 5  # assignment operator

# 4. Logical Operators
#Rule for 'and' operator
# 1. True + True = True
# 2. True + False = False
# 3. False + False = False
a = 10 
b = 20
print(a>10 and b>10) # 'and' operator(both conditoion should be True)
print(a==10 and b==20)

#Rule for 'or' operator
# 1. True + True = True
# 2. True + False = True
# 3. False + False = True
print(a<20 or b<10)  # 'or' operator(any 1 contion should be True)
print(not(a==10 and b==20)) #'not' operator(all contion should False)

# 5. Identity Operators - is, is not
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)   # is operator
print(x is z)

print(x is not z) # 'is not' operator 

# 6. Membership Operators - in, not in
my_list = ['apple', 'orange', 'watermelon']
print('apple' in my_list)  # in operator
print('apple2' in my_list)
print('apple2' not in my_list) # 'not in' operator

# 7. Bitwise Operators - AND &, OR |, XOR ^, NOT ~, etc
a = 5               # 5 in binary- 0101
b = 3               # 3 in binary- 0011
print(a & b)        # 1 in binary- 0001 (here 'and' operators rule applied by comparing a & b)
                    # 0 = False, 1 = True
#Rule for 'AND - &' operator
# 1. True + True = True
# 2. True + False = False
# 3. False + False = False

