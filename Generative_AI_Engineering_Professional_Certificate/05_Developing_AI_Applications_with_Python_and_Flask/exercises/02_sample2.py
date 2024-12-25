"""
Module to demonstrate a simple addition function.
"""

# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
# The purpose of this function is to add the two numbers and return the result.
def add(number_1, number_2):
    """
    Add two numbers and return the result.

    Args:
        number_1 (int or float): The first number to add.
        number_2 (int or float): The second number to add.

    Returns:
        int or float: The sum of number_1 and number_2.
    """
    return number_1 + number_2


# Constants are usually written in uppercase to indicate that they should not be changed.
NUM1 = 4  # Initialize the constant variable 'NUM1' with the value 4.
NUM2 = 5  # Initialize the constant variable 'NUM2' with the value 5.

# Call the 'add' function with 'NUM1' and 'NUM2' as arguments.
# The result of this addition operation is stored in the variable 'TOTAL'.
TOTAL = add(NUM1, NUM2)

# Print the result.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
