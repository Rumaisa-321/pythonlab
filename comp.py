# Function to read a complex number from user
def read_complex():
    real = float(input("Enter the real part: "))
    imag = float(input("Enter the imaginary part: "))
    return complex(real, imag)

# Read two complex numbers
print("Enter first complex number:")
c1 = read_complex()

print("Enter second complex number:")
c2 = read_complex()

# Display the numbers
print(f"\nFirst complex number: {c1}")
print(f"Second complex number: {c2}")

# Perform operations
print("\n--- Operations ---")
print(f"Addition: {c1} + {c2} = {c1 + c2}")
print(f"Subtraction: {c1} - {c2} = {c1 - c2}")
print(f"Multiplication: {c1} * {c2} = {c1 * c2}")
if c2 != 0:
    print(f"Division: {c1} / {c2} = {c1 / c2}")
else:
    print("Division: Cannot divide by zero")

