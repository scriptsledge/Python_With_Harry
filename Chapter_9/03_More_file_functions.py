# Reading lines from a file using Python

# Reading all lines at once and storing them in a list
f = open("Chapter_9/file.txt")  # Opens the file in read mode by default
lines = f.readlines()  # Reads all lines and stores them as a list of strings
print(lines, type(lines))  # Prints the list and its type
f.close()  # Closes the file

# Reading file line-by-line
f = open("Chapter_9/file.txt")
line1 = f.readline()  # Reads the first line as a string
print(line1, type(line1))  # Prints the line and its type

line2 = f.readline()  # Reads the second line
print(line2, type(line2))

line3 = f.readline()  # Reads the third line
print(line3, type(line3))

line4 = f.readline()  # Reads the fourth line
print(line4, type(line4))

line5 = f.readline()  # Reads the fifth line (if it exists)
print(line5 == '')  # Checks if the line is empty (indicating end of file)
f.close()

# Reading all lines using a while loop
f = open("Chapter_9/file.txt")
line = f.readline()  # Reads the first line
while(line != ""):  # Continues until the end of the file
    print(line, end='')  # Prints the current line
    line = f.readline()  # Reads the next line
f.close()
