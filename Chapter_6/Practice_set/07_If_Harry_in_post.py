post = input("Enter the post heading:")

# Check if "Harry" (case-insensitive) is mentioned in the post
if "Harry" in post or "harry" in post:
    print("The post is talking about Harry.")
else:
    print("The post is not talking about Harry.")
