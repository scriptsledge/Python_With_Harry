# Censor multiple words in a file by replacing them with hashtags of equivalent length

words = ["Donkey", "bad", "ganda"]  # Words to be censored
with open("Chapter_9/Practice_set/file.txt", "r") as f:
    content = f.read()

# Replace each word in the list with corresponding hashtags
for word in words:
    content = content.replace(word, "#" * len(word))

# Write the updated content back to the file
with open("Chapter_9/Practice_set/file.txt", "w") as f:
    f.write(content)
