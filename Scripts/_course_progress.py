import pandas as pd
import random

# Load login activity
login_df = pd.read_csv("login_activity.csv")

# Determine segment of each student
student_segments = (
    login_df.groupby("student_id")["student_segment"]
    .first()
    .to_dict()
)

courses = [
    "Python",
    "SQL",
    "Power BI",
    "Excel",
    "Machine Learning",
    "Statistics"
]

course_records = []

record_id = 1

for student_id, segment in student_segments.items():

    # each student enrolls in 2–6 courses
    enrolled_courses = random.sample(
        courses,
        random.randint(2, 6)
    )

    for course in enrolled_courses:

        if segment == "Highly Active":

            progress = random.randint(70, 100)

        elif segment == "Moderate":

            progress = random.randint(30, 85)

        else:

            progress = random.randint(0, 50)

        completed = "Yes" if progress >= 80 else "No"

        course_records.append({
            "course_record_id": f"C{record_id:05}",
            "student_id": student_id,
            "course_name": course,
            "progress_percent": progress,
            "completed": completed
        })

        record_id += 1

course_df = pd.DataFrame(course_records)

course_df.to_csv(
    "course_progress.csv",
    index=False
)

print("course_progress.csv generated successfully!")
print("Total Records:", len(course_df))