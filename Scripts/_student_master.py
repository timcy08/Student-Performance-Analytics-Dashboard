import pandas as pd
import random
from faker import Faker

# Create Faker object
fake = Faker("en_IN")

# Number of students
num_students = 500

# Colleges
colleges = [
    "IIT Delhi",
    "NIT Jaipur",
    "BITS Pilani",
    "Delhi University",
    "Rajasthan University"
]

# Departments
departments = [
    "Computer Science",
    "Information Technology",
    "Electronics",
    "Mechanical",
    "Civil"
]

# Status
status_list = [
    "Active",
    "Inactive"
]

students = []

for i in range(1, num_students + 1):

    student = {
        "student_id": f"ST{i:03}",
        "student_name": fake.name(),
        "college": random.choice(colleges),
        "department": random.choice(departments),
        "batch": random.choice([2022, 2023, 2024]),
        "status": random.choice(status_list)
    }

    students.append(student)

# Convert to DataFrame
df = pd.DataFrame(students)

# Save CSV
df.to_csv("student_master.csv", index=False)

print("student_master.csv generated successfully!")