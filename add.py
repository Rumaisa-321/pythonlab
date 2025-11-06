def add_numbers(*args):
    """add all given numbers."""
    return sum(args)
nums = input("enter numbers separated by space: ").split()
nums = [int(n) for n in nums]
print("Sum =", add_numbers(*nums))
