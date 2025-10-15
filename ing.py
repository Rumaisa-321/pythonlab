string = input("enter a word:")
if string.endswith("ing"):
   string = string+"ly"
else:
  string = string+"ing"
print(string)
