import pandas as pd
import random

# Read login activity
login_df = pd.read_csv("login_activity.csv")

# Get unique student segments
student_segments = (
    login_df.groupby("student_id")["student_segment"]
    .first()
    .to_dict()
)

forum_records = []

for student_id, segment in student_segments.items():

    if segment == "Highly Active":

        questions = random.randint(5, 20)
        answers = random.randint(10, 40)
        comments = random.randint(20, 80)

    elif segment == "Moderate":

        questions = random.randint(1, 10)
        answers = random.randint(1, 20)
        comments = random.randint(5, 40)

    else:

        questions = random.randint(0, 2)
        answers = random.randint(0, 5)
        comments = random.randint(0, 10)

    forum_records.append({
        "student_id": student_id,
        "questions": questions,
        "answers": answers,
        "comments": comments
    })

forum_df = pd.DataFrame(forum_records)

forum_df.to_csv(
    "forum_activity.csv",
    index=False
)

print("forum_activity.csv generated successfully!")
print("Total Records:", len(forum_df))