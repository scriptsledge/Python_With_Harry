# Reading a file using Python
# Open a file in read mode ('r')
f = open("Chapter_9/file.txt", "r")

# Read the content of the file
data = f.read()
print(data)

# Close the file to free resources
f.close()
