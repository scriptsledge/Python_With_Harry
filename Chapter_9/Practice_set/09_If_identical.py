# Compare contents of two files
with open("Chapter_9/Practice_set/this.txt") as f:
    file1_content = f.read()  # Read the first file

with open("Chapter_9/Practice_set/that.txt") as j:
    file2_content = j.read()  # Read the second file

if file1_content == file2_content:
    print("Both files are identical!")
else:
    print("Files are not identical!")
