# List to store student marks
marks = []

# Collecting marks from user input for 6 students
val = int(input("Enter student1 marks:"))
marks.append(val)

val = int(input("Enter student2 marks:"))
marks.append(val)

val = int(input("Enter student3 marks:"))
marks.append(val)

val = int(input("Enter student4 marks:"))
marks.append(val)

val = int(input("Enter student5 marks:"))
marks.append(val)

val = int(input("Enter student6 marks:"))
marks.append(val)

# Sorts the marks in ascending order
marks.sort()

# Print the sorted list of student marks
print(marks)
