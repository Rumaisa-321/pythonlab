words = input("enter words separated by spaces:").split()
longest = max(words,key=len)
print("length of the longest word:",len(longest))
