import os

# Read content from old file
with open("Chapter_9/Practice_set/old.txt") as f:
    content = f.read()

# Remove the old file
os.remove("Chapter_9/Practice_set/old.txt")  # Deletes the file

# Create a new file and write content to it
with open("Chapter_9/Practice_set/renamed_by_python.txt", 'w') as f:
    f.write(content)
