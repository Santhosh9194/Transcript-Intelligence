import pandas as pd

topic_df = pd.read_csv(
    "output/topic_categories.csv"
)

insights = []

for category in topic_df["Category"].unique():

    count = len(
        topic_df[
            topic_df["Category"] == category
        ]
    )

    insights.append(
        [category, count]
    )

df = pd.DataFrame(
    insights,
    columns=[
        "Category",
        "MeetingCount"
    ]
)

df.to_csv(
    "output/bonus_insights.csv",
    index=False
)

print("Bonus insights generated")