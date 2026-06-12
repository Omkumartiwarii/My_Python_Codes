string = "My name is  om  kumar tiwari"
print(string)
print(string.find("  "))

string1 = "My name is om kumar tiwari"
print(string1.find("  "))

#check double occurance of space

print(string.replace("  "," "))
#string is immutable, print(string.replace("  "," ")) <-- yah ek naya string create karta hai main string same rahta hai.