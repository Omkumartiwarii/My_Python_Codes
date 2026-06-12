def calculate(A, B, C):
    if C == '+':
        return A + B
    elif C == '-':
        return A - B
    elif C == '*':
        return A * B
    elif C == '/':
        return A / B
    else:
        return "Invalid Operator"

A = float(input("Enter 1st Number : "))
B = float(input("Enter 2nd Number : "))
C = input("Enter Operator : ")
print(calculate(A, B, C))