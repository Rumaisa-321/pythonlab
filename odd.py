def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
n = int(input("enter a number:"))
result = check_even_odd(n)
print("the number is", result)
