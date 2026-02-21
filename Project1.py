# Calculator

# Step-1: Create functions

# Function to add numbers
def add(num1,num2):
    return num1 + num2

# Function to subtract numbers
def sub(num1,num2):
    return num1 - num2

# Function to multiply numbers
def multiply(num1,num2):
    return num1 * num2

# Function to divide numbers
def divide(num1,num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

# Function to find average of numbers
def avg(num1,num2):
    return (num1 + num2)/2


# Step-2: User Input

print("""Please Select the Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Average""")

select = int(input("Select a Operation form (1-5): "))

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Step-3: Print the result

if select == 1:
    print(f"{number1} + {number2} = ", \
          add(number1,number2))

elif select == 2:
    print(f"{number1} - {number2} = ", \
          sub(number1,number2))

elif select == 3:
    print(f"{number1} * {number2} = ", \
          multiply(number1,number2))
    
elif select == 4:
    print(f"{number1} / {number2} = ", \
          divide(number1,number2))
    
elif select == 5:
    print(f"({number1} + {number2})/2 = ", \
          avg(number1,number2))
    
else:
    print("Invalid Operation! Please select again")
