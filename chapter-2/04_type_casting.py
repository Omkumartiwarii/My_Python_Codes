A = 1     #integer data type <type 'int'>
B = 1.1   #float data type <type 'float'>
C = "OM"  #character/string data type <type 'str'>
D = True  #boolean data type <type 'bool'>
E = None  #none type of data type <type 'NoneType'>

print(type(A)) 
print(type(B)) 
print(type(C)) 
print(type(D)) 
print(type(E)) 

#type casting
A = "1.1"    #float data type
B = int(float(A)) #string to float to int
print(type(B)) #<class 'int'>
print(str(32))
print(float("32.0"))