import pandas as pd

# =========================
# READ ALL FILES
# =========================

student_df = pd.read_csv("student_master.csv")
login_df = pd.read_csv("login_activity.csv")
course_df = pd.read_csv("course_progress.csv")
forum_df = pd.read_csv("forum_activity.csv")
webinar_df = pd.read_csv("webinar_attendance.csv")
event_df = pd.read_csv("event_participation.csv")
mentor_df = pd.read_csv("mentor_meetings.csv")

# =========================
# LOGIN AGGREGATION
# =========================

login_summary = (
    login_df.groupby("student_id")
    .agg(
        login_frequency=("login_id", "count"),
        avg_session_duration=("session_duration", "mean"),
        student_segment=("student_segment", "first")
    )
    .reset_index()
)

# =========================
# COURSE AGGREGATION
# =========================

course_summary = (
    course_df.groupby("student_id")
    .agg(
        avg_progress=("progress_percent", "mean"),
        total_courses=("course_name", "count"),
        courses_completed=(
            "completed",
            lambda x: (x == "Yes").sum()
        )
    )
    .reset_index()
)

# =========================
# WEBINAR AGGREGATION
# =========================

webinar_summary = (
    webinar_df.groupby("student_id")
    .agg(
        webinars_attended=(
            "attendance_status",
            lambda x: (x == "Attended").sum()
        )
    )
    .reset_index()
)

# =========================
# EVENT AGGREGATION
# =========================

event_summary = (
    event_df.groupby("student_id")
    .agg(
        events_participated=("event_id", "count")
    )
    .reset_index()
)

# =========================
# MENTOR AGGREGATION
# =========================

mentor_summary = (
    mentor_df.groupby("student_id")
    .agg(
        mentor_meetings=("meeting_id", "count"),
        total_mentor_duration=("duration", "sum")
    )
    .reset_index()
)

# =========================
# MERGE EVERYTHING
# =========================

summary = student_df.copy()

summary = summary.merge(
    login_summary,
    on="student_id",
    how="left"
)

summary = summary.merge(
    course_summary,
    on="student_id",
    how="left"
)

summary = summary.merge(
    forum_df,
    on="student_id",
    how="left"
)

summary = summary.merge(
    webinar_summary,
    on="student_id",
    how="left"
)

summary = summary.merge(
    event_summary,
    on="student_id",
    how="left"
)

summary = summary.merge(
    mentor_summary,
    on="student_id",
    how="left"
)

# =========================
# HANDLE NULL VALUES
# =========================

summary.fillna(0, inplace=True)

# =========================
# REMOVE NON-ANALYTICAL COLUMNS
# =========================

summary.drop(
    columns=["student_name", "college"],
    inplace=True
)

# =========================
# SAVE FILE
# =========================

summary.to_csv(
    "student_summary.csv",
    index=False
)

print("student_summary.csv generated successfully!")
print("Rows:", len(summary))
print("Columns:", len(summary.columns))

print("\nFinal Columns:")
print(summary.columns.tolist())