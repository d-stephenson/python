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