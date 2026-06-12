#write a program to calculate square of a number entered by user
A = int(input("enter a number:"))
print("square of this number is :", A**2)  # Using exponentiation operator for squaring
# Alternative way using multiplication
print("square of this number is :", A*A)
print("square of this number is :", A^2) # Note: A^2 is not correct for squaring, it performs bitwise XOR in Python
