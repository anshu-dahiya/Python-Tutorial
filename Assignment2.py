# Q1. write a program to input student name and marks of 3 subject
#     print name and percentage
student_name = input("Enter your name: ")
sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))

percentage = ((sub1 + sub2 +sub3)/300) *100
print(f"{student_name} pecentage is {int(percentage)}%")

# Q2. Write a program that collects multiple types of data 
#     (eg. name,age,height,and student status) from user input, 
#     store them is dictionary, and then prints out collected data.

student_info = {
    "Name"  : input("Enter your name: ") ,
    "age"   : int(input("Enter your age: ")),
    "height": float(input("Enter your height: ")) ,
    "status": input("Are you student (yes/no): ") 
}

print(student_info)