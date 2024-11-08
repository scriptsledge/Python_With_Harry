post = input("Enter the post heading:")

# Convert the post to lowercase and check if "harry" is mentioned
if "harry" in post.lower():
    print("The post is talking about Harry.")
else:
    print("The post is not talking about Harry.")
