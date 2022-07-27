Comments
A comment is a piece of text within a program that is not executed. It can be used to provide additional information to aid in understanding the code.

The # character is used to start a comment and it continues until the end of the line.

# Comment on a single line
 
user = "JDoe" # Comment after code

# ////////////////////////////////////////////

Arithmetic Operations
Python supports different types of arithmetic operations that can be performed on literal numbers, variables, or some combination. The primary arithmetic operators are:

+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus (returns the remainder)
** for exponentiation

# Arithmetic operations
 
result = 10 + 30
result = 40 - 10
result = 50 * 5
result = 16 / 4
result = 25 % 2
result = 5 ** 3

# ////////////////////////////////////////////

Plus-Equals Operator +=
The plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable. In the case where the variable and the value are strings, this operator performs string concatenation instead of addition.

The operation is performed in-place, meaning that any other variable which points to the variable being updated will also be updated.

# Plus-Equal Operator
 
counter = 0
counter += 10
 
# This is equivalent to
 
counter = 0
counter = counter + 10
 
# The operator will also perform string concatenation
 
message = "Part 1 of message "
message += "Part 2 of message"

# ////////////////////////////////////////////

Variables
A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character _.

The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed.

# These are all valid variable names and assignment
 
user_name = "codey"
user_id = 100
verified = False
 
# A variable's value can be changed after assignment
 
points = 100
points = 120

# ////////////////////////////////////////////

Modulo Operator %
A modulo calculation returns the remainder of a division between the first and second number. For example:

The result of the expression 4 % 2 would result in the value 0, because 4 is evenly divisible by 2 leaving no remainder.
The result of the expression 7 % 3 would return 1, because 7 is not evenly divisible by 3, leaving a remainder of 1.

# Modulo operations
 
zero = 8 % 4
 
nonzero = 12 % 5

# ////////////////////////////////////////////

Integers
An integer is a number that can be written without a fractional part (no decimal). An integer can be a positive number, a negative number or the number 0 so long as there is no decimal portion.

The number 0 represents an integer value but the same number written as 0.0 would represent a floating point number.

# Example integer numbers
 
chairs = 4
tables = 1
broken_chairs = -2
sofas = 0
 
# Non-integer numbers
 
lights = 2.5
left_overs = 0.0

# ////////////////////////////////////////////