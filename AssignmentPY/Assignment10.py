# Asking the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n--- Arithmetic Operations ---")
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

# Check for division by zero
if num2 != 0:
    print("Division (float):", num1 / num2)
    print("Integer division (floor):", num1 // num2)
    print("Remainder (modulo):", num1 % num2)
else:
    print("Division, floor division, and modulo are not possible (cannot divide by zero).")

print("\n--- Comparison ---")
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("Both numbers are equal.")
