A = 0
B = 1
num = int(input("Enter Number Of Terms To Print Fibonacci Series : "))
print("Fibonacci Series : ", end="")
for i in range(num): #if num-1
    print(A, end=" ")
    A, B = B, A + B
# print(A)