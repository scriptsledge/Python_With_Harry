# Check for the presence of the word "python" in a file

with open("Chapter_9/Practice_set/log.txt") as f:
    content = f.read()

# Checking if the word "python" is in the file content
if "python" in content:
    print("Yes, python is present")
else:
    print("Python is not present")
