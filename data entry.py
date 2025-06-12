import csv
import os


filename = "student_data.csv"


subjects = ["Math", "Science", "English", "Social", "Computer"]


if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = ["Name", "Roll No"] + subjects
        writer.writerow(headers)

num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    print("\nEnter student details:")
    name = input("Name: ")
    roll_no = input("Roll No: ")

    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll_no] + marks)

print(f"\nData saved to {filename}")
