# Appending content to an existing file
f = open("Chapter_9/myfile.txt", "a")  # Opens the file in append mode
f.write("This line is inserted through append function.")  # Appends content to the file
f.close()  # Closes the file
