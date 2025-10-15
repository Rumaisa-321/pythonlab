line = input("Enter a line of text: ")


words = line.split()


word_counts = {}


for word in words:
    word = word.lower()  
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


for word, count in word_counts.items():
    print(f"{word}: {count}")
