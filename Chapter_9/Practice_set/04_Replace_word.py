word = "Donkey"
with open("Chapter_9/Practice_set/file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")

with open("Chapter_9/Practice_set/file.txt", "w") as f:
    f.write(contentNew)