import pandas as pd
import random
from datetime import datetime, timedelta

# Load student master data
students_df = pd.read_csv("student_master.csv")

student_ids = students_df["student_id"].tolist()

# Shuffle students
random.shuffle(student_ids)

# Segmentation
high_active = student_ids[:100]
moderate = student_ids[100:350]
at_risk = student_ids[350:]

login_records = []

login_counter = 1

devices = ["Mobile", "Laptop", "Tablet"]

for student in high_active:

    num_logins = random.randint(20, 40)

    for _ in range(num_logins):

        login_date = datetime.today() - timedelta(
            days=random.randint(0, 90)
        )

        login_records.append({
            "login_id": f"L{login_counter:05}",
            "student_id": student,
            "login_date": login_date.date(),
            "login_time": login_date.strftime("%H:%M:%S"),
            "device": random.choice(devices),
            "session_duration": random.randint(60, 180),
            "student_segment": "Highly Active"
        })

        login_counter += 1


for student in moderate:

    num_logins = random.randint(8, 20)

    for _ in range(num_logins):

        login_date = datetime.today() - timedelta(
            days=random.randint(0, 90)
        )

        login_records.append({
            "login_id": f"L{login_counter:05}",
            "student_id": student,
            "login_date": login_date.date(),
            "login_time": login_date.strftime("%H:%M:%S"),
            "device": random.choice(devices),
            "session_duration": random.randint(20, 90),
            "student_segment": "Moderate"
        })

        login_counter += 1


for student in at_risk:

    num_logins = random.randint(1, 7)

    for _ in range(num_logins):

        login_date = datetime.today() - timedelta(
            days=random.randint(0, 90)
        )

        login_records.append({
            "login_id": f"L{login_counter:05}",
            "student_id": student,
            "login_date": login_date.date(),
            "login_time": login_date.strftime("%H:%M:%S"),
            "device": random.choice(devices),
            "session_duration": random.randint(5, 30),
            "student_segment": "At Risk"
        })

        login_counter += 1


login_df = pd.DataFrame(login_records)

login_df.to_csv("login_activity.csv", index=False)

print("login_activity.csv generated successfully!")
print("Total Records:", len(login_df))