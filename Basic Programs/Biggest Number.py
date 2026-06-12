A = int(input("Enter 1st Number : "))
B = int(input("Enter 2nd Number : "))
C = int(input("Enter 3rd Number : "))
if A > B and A > C:
    print(f"{A} is the Biggest Number")
elif B > A and B > C:
    print(f"{B} is the Biggest Number")
else:
    print(f"{C} is the Biggest Number")