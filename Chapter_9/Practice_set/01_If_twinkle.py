# Open the file and read its content
f = open("Chapter_9/Practice_set/poem.txt")  # Opens the file in read mode
content = f.read()  # Reads the entire file content

# Check if the word "twinkle" is in the content
if "twinkle" in content:
    print('The word "twinkle" is present in the content.')
else:
    print('The word "twinkle" is not present in the content.')

f.close()  # Closes the file
