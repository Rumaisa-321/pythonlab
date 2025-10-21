
names = input("Enter a list of first names separated by spaces: ").split()


last_name = names[-1]


count_a = last_name.lower().count('a')

print(f"The letter 'a' occurs {count_a} times in the last name '{last_name}'.")

