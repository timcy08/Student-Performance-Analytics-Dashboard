import pandas as pd
import random

login_df = pd.read_csv("login_activity.csv")

student_segments = (
    login_df.groupby("student_id")["student_segment"]
    .first()
    .to_dict()
)

participation_types = [
    "Hackathon",
    "Workshop",
    "Seminar",
    "Competition",
    "Networking Event"
]

records = []
event_counter = 1

for student_id, segment in student_segments.items():

    if segment == "Highly Active":
        num_events = random.randint(3, 5)

    elif segment == "Moderate":
        num_events = random.randint(1, 3)

    else:
        num_events = random.randint(0, 1)

    selected_events = random.sample(
        participation_types,
        min(num_events, len(participation_types))
    )

    for event in selected_events:

        records.append({
            "event_id": f"E{event_counter:03}",
            "student_id": student_id,
            "participation_type": event
        })

        event_counter += 1

event_df = pd.DataFrame(records)

event_df.to_csv(
    "event_participation.csv",
    index=False
)

print("event_participation.csv generated successfully!")
print("Total Records:", len(event_df))