'''6.	Write a Python program to check whether variable is integer or string. 
'''

# In Python, you can use the `type()` function to check the type of a variable. Here's an example:

 
def check_type(value):
    if isinstance(value, int):
        return "The value is an integer."
    elif isinstance(value, str):
        return "The value is a string."
    else:
        return "The value is neither an integer nor a string."

# Example usage
value1 = 42
value2 = "Hello"

print(value1,check_type(value1))
print(value2,check_type(value2))


