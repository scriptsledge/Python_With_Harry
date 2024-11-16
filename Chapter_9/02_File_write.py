# Writing content to a file using Python

# The text to write, with \n representing a new line
st = "This line will be written\nin myfile.txt"

# Open the file in write mode ('w')
f = open("Chapter_9/myfile.txt", "w")
# 'f' is a file object returned by open(), which allows interaction with the file.

f.write(st)  # Writes the string content to the file

f.close()  # Closes the file to ensure changes are saved and resources are freed
