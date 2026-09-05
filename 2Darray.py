import numpy as np

# Marks of 5 students in 3 subjects
marks = np.array([ 
    [78, 85, 90],   # Student 0
    [65, 72, 80],   # Student 1
    [88, 91, 84],   # Student 2
    [70, 68, 75],   # Student 3
    [95, 89, 92]    # Student 4
])

print("Marks Array:")
print(marks)

# 1. Find maximum marks
print("Maximum marks:", np.max(marks))

# 2. Find minimum marks
print("Minimum marks:", np.min(marks))

# 3. Find average marks
print("Average marks:", np.mean(marks))

# 4. Find student ID who scored maximum marks in subject 1
student_id = np.argmax(marks[:, 1])
print("Student ID with maximum marks in Subject 1:", student_id)

# 5. Find maximum marks subject-wise
print("Maximum marks subject-wise:", np.max(marks, axis=0))

# 6. Find average marks subject-wise
print("Average marks subject-wise:", np.mean(marks, axis=0))
