# Write a Python program to print the contents of a directory using the OS module.
# Search online for the function which does that.

import os

# List contents of a specified directory
path = "/"
contents = os.listdir(path)
print("Directory contents:", contents)

# List contents of current working directory
contents = os.listdir()
print("Current directory contents:", contents)
