marks1 = int(input("Enter marks of subject 1:"))
marks2 = int(input("Enter marks of subject 2:"))
marks3 = int(input("Enter marks of subject 3:"))

total_percentage = (marks1 + marks2 + marks3) / 3

# Checks if any subject score is below 33 or total percentage is below 40
if marks1 < 33 or marks2 < 33 or marks3 < 33 or total_percentage < 40:
    print("Student failed!")
else:
    print("Student passed!")
    
print("Score:", total_percentage)
