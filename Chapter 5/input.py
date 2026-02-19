# input function in python

# input funtion always reads input as string
a = input("Enter No.: ")
print(int(a)+int(a))


name = input("Enter your name: ")
print(f"welcome {name} to python tutorial")

# multiple input from user
# input from user to add two number and print result
x = input("Enter first number: ")
y = input("Enter second number: ")
print(f"Sun of {x} & {y} is {int(x) + int(y)}")

# Q. write a program to input student name and marks of 3 subject
#    print name and percentage
student_name = input("Enter your name: ")
sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))

percentage = (sub1 + sub2 +sub3)/300 *100
print(f"{student_name} pecentage is {percentage}%")