# Generate multiplication tables from 1 to 20
for i in range(1, 21):
    with open(f"Chapter_9/Practice_set/Tables/tableOf_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i * j}\n")
