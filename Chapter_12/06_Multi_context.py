# Using a single `with` statement to manage multiple file contexts
with ( 
    open('C:\\Bits\\Python_With_Harry\\Chapter_12\\file1.txt', 'w') as f1, 
    open('C:\\Bits\\Python_With_Harry\\Chapter_12\\file2.txt', 'w') as f2 
):
    pass  # Both files are safely opened, and resources will be released automatically when done.
