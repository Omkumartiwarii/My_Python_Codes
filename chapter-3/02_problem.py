# name = input("Enter name :")
# print(f"Dear {name}\nyou are selected\nDate 11/10/25")

pattern = '''Dear <|Name|>
you are selected
<|Date|>'''
print(pattern.replace("<|Name|>","Om Kumar").replace("<|Date|>","11 october 2025"))