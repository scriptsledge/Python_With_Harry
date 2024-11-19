# Reading a file using the standard method
f = open("file.txt")  # Opens the file in read mode
print(f.read())  # Reads and prints the content
f.close()  # Explicitly closes the file

# Using 'with' for better file handling
with open("file.txt") as f:  # 'with' ensures automatic file closing
    print(f.read())  # Reads and prints the content
