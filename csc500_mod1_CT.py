##### Module 1 Criticle Thinking
##### Colorado State University Global Campus
##### csc500-1
##### Dr Jessica SCwartz 

# Part 1.
## Write a Python Program to find addition and subtraction of two numbers.
### - Ask the user to input the two numbers (num1 & num2.)
### - Given those two numbers, add them together to find the output.
### - Also, subtract the two numbers to find the output.

# Part1: Code
# Function to add two numbers, 'the sum fiunction'.
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers, 'the differnece function'.
def subtract(num1, num2):
    return num1 - num2  

#User input:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# calculate the sum and difference functions
sum= add(num1, num2)
difference= subtract(num1, num2)

print(f"The sum of {num1} and {num2} is {sum:,.5f}!")

#calculate the difference function
print(f"The difference of {num1} and {num2} is {difference:,.5f}")

# Part 2.
#### Write a Python program to find the multiplication and division of two numbers.
##### - Ask the user to input two numbers (num1 and num2). 
# Given those two numbers, multiply them together to find the output.
#  Also, divide num1/num2 to find the output.
##### - Compile and submit your pseudocode, source code, and screenshots of the application executing the code from parts 1 and 2,
#  the results and GIT repository in a single document (Word is preferred).

# Part1: Code

# Function to Multiply two numbers, 'the multiple function'.
def multiply(num1, num2):
    return num1 * num2

# Function to subtract two numbers, 'the differnece function'.
def divide(num1, num2):
    return num1 / num2  

#User input:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# calculate the sum and difference functions
multiply= multiply(num1, num2)
divide= divide(num1, num2)

print(f"The multiple of {num1} by {num2} is {multiply:,.5f}!")

#calculate the difference function
print(f"The division of {num1} by {num2} is {divide:,.5f}! ")
