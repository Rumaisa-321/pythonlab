dict1 = eval(input("enter first dictionary:"))
dict2 = eval(input("enter second dictionary:"))
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)
