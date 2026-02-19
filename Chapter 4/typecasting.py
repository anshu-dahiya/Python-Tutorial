# TypeCasting in Python

a = 1
print(type(a))

b = "1"
print(type(b))
# print(a+b)   # it will give error

c = int(b)      #typeCasting
print(type(c))  
print(a+c)

print(a+int(b))  #we can also do typeCasting while print

# all str type can not be cast into numerical
# name = 'Gopi'
# newname = int(name)


# all numerical type can be cast into str
mynum = 26
mynum2 = str(mynum)
print(type(mynum2))

f1 = 22.56
f2 = int(f1)
print(f2)
print(type(f2))

in1 = 26
print(type(float(in1)))

# implicit type casting
var1 = 20   # int
var2 = 10.5 # float
var3 = var1+var2
print(var3)
print(type(var3))

# explicit type casting
int_num = 102
str_num = str(int_num)
print(type(str_num))

a0 = bool(0)
print(a0)
print(type(a0))

a1 = bool(1)
print(a1)
print(type(a1))