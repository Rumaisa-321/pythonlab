def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f
n = int(input("enter n: "))
s = 0
for i in range(1,n+1):
        s += (i**3) / fact(i)
print("sum of series =", s)
