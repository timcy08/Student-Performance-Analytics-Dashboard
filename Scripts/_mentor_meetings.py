import pandas as pd
import random

# =========================
# READ STUDENT MASTER
# =========================

student_df = pd.read_csv("student_master.csv")

student_ids = student_df["student_id"].tolist()

# =========================
# CREATE MENTOR MEETINGS
# =========================

mentor_ids = [
    "M001",
    "M002",
    "M003",
    "M004",
    "M005"
]

records = []
meeting_counter = 1

for student_id in student_ids:

    # Some students may have 0 meetings
    num_meetings = random.randint(0, 3)

    for _ in range(num_meetings):

        records.append({
            "meeting_id": f"MT{meeting_counter:04}",
            "student_id": student_id,
            "mentor_id": random.choice(mentor_ids),
            "duration": random.randint(15, 90)  # minutes
        })

        meeting_counter += 1

# =========================
# SAVE CSV
# =========================

mentor_df = pd.DataFrame(records)

mentor_df.to_csv(
    "mentor_meetings.csv",
    index=False
)

print("mentor_meetings.csv generated successfully!")
print("Total Records:", len(mentor_df))