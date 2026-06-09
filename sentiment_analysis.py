import os
import json
import pandas as pd

results = []

for folder in os.listdir("dataset"):

    summary_file = f"dataset/{folder}/summary.json"

    if not os.path.exists(summary_file):
        continue

    with open(summary_file) as f:
        summary = json.load(f)

    sentiment = summary.get(
        "overallSentiment",
        "neutral"
    )

    score = summary.get(
        "sentimentScore",
        3
    )

    results.append(
        [folder, sentiment, score]
    )

df = pd.DataFrame(
    results,
    columns=[
        "MeetingID",
        "Sentiment",
        "Score"
    ]
)

df.to_csv(
    "output/sentiment_report.csv",
    index=False
)

print("Sentiment analysis completed")