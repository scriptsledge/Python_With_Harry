with open("Chapter_9/Practice_set/log.txt") as f:
    lines = f.readlines()  # Read all lines into a list

lineno = 1
for line in lines:
    if "python" in line:  # Check if "python" is in the current line
        print(f"python is present in line no: {lineno}")
        break
    lineno += 1
else:
    print("Python is not present")
