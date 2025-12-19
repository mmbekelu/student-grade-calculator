# Beginner Student Grade Calculator 

# Step 1: Ask for each score
math = float(input("Enter your Math score: "))
english = float(input("Enter your English score: "))
science = float(input("Enter your Science score: "))
history = float(input("Enter your History score: "))

# Step 2: Store them in a dictionary
scores = {
    "Math": math,
    "English": english,
    "Science": science,
    "History": history
}

# Step 3: Calculate the average
average = (math + english + science + history) / 4

# Step 4: Put grade letters in a list based on ranges
# We aren't calculating the grade using if.3
# Instead, we decide the grade AFTER running the program.

grades = ["A", "B", "C", "D", "F"]  # Just storing options

# Step 5: Show results (YOU choose the grade by looking at the number)
print("\n--- RESULTS ---")
print("Scores:", scores)
print("Average:", average)
print("Pick the correct grade from this list based on your teacher's rules:", grades)
