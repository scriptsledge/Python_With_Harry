# Dictionary with word-meaning pairs
words = {
    "madad": "help",
    "kursi": "chair",
    "billi": "cat"
}

# Input to look up the meaning of a word
word = input("Enter the word you want the meaning of:")

# Direct dictionary lookup to get the meaning of the entered word
print(words[word])  # Raises KeyError if word is not found
