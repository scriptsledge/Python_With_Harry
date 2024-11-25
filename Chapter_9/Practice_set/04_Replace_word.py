# Replace occurrences of the word "Donkey" with "######" in a file

word = "Donkey"  # Word to be censored
with open("Chapter_9/Practice_set/file.txt", "r") as f:
    content = f.read()

# Replacing all occurrences of the target word with censorship
contentNew = content.replace(word, "######")

# Writing the updated content back to the file
with open("Chapter_9/Practice_set/file.txt", "w") as f:
    f.write(contentNew)
