numbers = input("Enter a list of integers separated by spaces: ").split()


result = []
for num in numbers:
    
    val = int(num)
    if val > 100:
        result.append('over')
    else:
        result.append(val)

print(result)
