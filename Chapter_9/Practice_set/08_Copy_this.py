# Reading from 'this.txt'
with open("Chapter_9/Practice_set/this.txt") as f:
    content = f.read()

# Writing to 'that.txt'
with open("Chapter_9/Practice_set/that.txt", "w") as j:
    j.write(content + "(Copied)")
