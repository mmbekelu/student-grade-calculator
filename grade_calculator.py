# ================================
# Student Grade Calculator v2
# ================================

print("\nWelcome to the Student Grade Calculator\n")

# Step 1: Get student name and clean it
raw_name = input("Enter student name: ")
student_name = raw_name.strip().title()

# Step 2: Ask for scores
math = float(input("Enter Math score: "))
english = float(input("Enter English score: "))
science = float(input("Enter Science score: "))
history = float(input("Enter History score: "))

# Step 3: Store scores in a dictionary (JSON-style data)
scores = {
    "Math": math,
    "English": english,
    "Science": science,
    "History": history
}

# Step 4: Calculate average
average = (math + english + science + history) / 4

# Step 5: Decide grade using conditional logic
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Step 6: Output results
print("\n--- RESULTS ---")
print("Student:", student_name)
print("Scores:", scores)
print("Average:", round(average, 2))
print("Final Grade:", grade)
