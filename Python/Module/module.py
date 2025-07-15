# Importing math module
import math
pie = math.pi
print("The value of pi is:", pie)

# Importing specific function
from math import pi
print(pi)

# Importing random number
import random
# Generate a random number between 1 and 10
res = random.randint(1, 10)
print("Random Number:", res)

# Importing Modules with Aliases
import math as m
# Use the alias to call a function
result = m.sqrt(25)
print("Square root of 25:", result)

# Importing Everything from a Module (*)
from math import *
print(pi)         # Accessing the constant 'pi'
print(factorial(6))  # Using the factorial function

# Handling Import Errors in Python
try:
    import mathematics  # Incorrect module name
    print(mathematics.pi)
except ImportError:
    print("Module not found! Please check the module name or install it if necessary.")


# Importing  module calc.py
import calc
print(calc.add(10, 2))

# importing sqrt() and factorial from the
from math import sqrt, factorial
print(sqrt(16))
print(factorial(6))

# importing sys module
import sys
# importing sys.path
print(sys.path)

# importing sqrt() and factorial from the
import math as mt
print(mt.sqrt(16))
print(mt.factorial(6))
