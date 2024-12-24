try:
    with(
    open("C:\\Bits\\Python_With_Harry\\Chapter_12\\Practice_set\\1.txt", "w") as x,
    open("C:\\Bits\\Python_With_Harry\\Chapter_12\\Practice_set\\2.txt", "r") as y,
    open("C:\\Bits\\Python_With_Harry\\Chapter_12\\Practice_set\\3.txt", 'w') as z
    ):
        pass
except Exception as e:
    print(f"Kuch to gadbad hai Daya😕\n{e}")

print("But program ran successfully!")