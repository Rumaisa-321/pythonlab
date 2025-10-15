color_list1 = input("enter first list of colors:").split()
color_list2 = input("enter second list of colors:").split()
result = [color for color in color_list1
if color not in color_list2]
print("colors in list1 not in list2:",result)
