list1 = list(map(int, input("Enter the first list of integers: ").split()))
list2 = list(map(int, input("Enter the second list of integers: ").split()))


same_length = len(list1) == len(list2)


same_sum = sum(list1) == sum(list2)


common_values = set(list1) & set(list2)  
any_common = len(common_values) > 0


print("Same length:", same_length)
print("Same sum:", same_sum)
print("Common values exist:", any_common)
