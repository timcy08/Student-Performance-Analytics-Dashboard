import pandas as pd
import random

# Read login activity
login_df = pd.read_csv("login_activity.csv")

# Get student segments
student_segments = (
    login_df.groupby("student_id")["student_segment"]
    .first()
    .to_dict()
)

webinars = [
    "AI Workshop",
    "Data Science Bootcamp",
    "Resume Building",
    "Interview Preparation",
    "Power BI Masterclass"
]

records = []

for webinar_num, webinar_name in enumerate(webinars, start=1):

    webinar_id = f"W{webinar_num:03}"

    for student_id, segment in student_segments.items():

        if segment == "Highly Active":
            attended = random.random() < 0.85

        elif segment == "Moderate":
            attended = random.random() < 0.55

        else:
            attended = random.random() < 0.20

        records.append({
            "webinar_id": webinar_id,
            "student_id": student_id,
            "webinar_name": webinar_name,
            "attendance_status":
                "Attended" if attended else "Absent"
        })

webinar_df = pd.DataFrame(records)

webinar_df.to_csv(
    "webinar_attendance.csv",
    index=False
)

print("webinar_attendance.csv generated successfully!")
print("Total Records:", len(webinar_df))