def compare(s1, s2, n):
    if s1[:n] == s2[:n]:
        return True
    else:
        return False
s1 = input("enter first string:")
s2 = input("enter second string:")
n = int(input("enter number of characters to compare:"))
result = compare(s1, s2, n)
print("result:", result)
