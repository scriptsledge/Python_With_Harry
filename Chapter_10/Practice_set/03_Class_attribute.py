class Test:
    a = '1'  # Class attribute

obj = Test()
obj.a = 0  # Creates an instance attribute for obj

print(obj.a)  # Outputs: 0 (instance attribute)
print(Test.a)  # Outputs: '1' (class attribute)

# Setting 'a' using 'object.a = 0' does NOT change the class attribute.
# It creates a separate instance attribute for that specific object.
