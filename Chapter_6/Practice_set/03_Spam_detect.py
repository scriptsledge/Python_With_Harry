p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment:")

# 'in' checks if a specified substring exists within the input string
if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is spam!")
else:
    print("This comment is not a spam.")
