import os
import json
import pandas as pd

dataset_path = "dataset"

results = []

for folder in os.listdir(dataset_path):

    folder_path = os.path.join(dataset_path, folder)

    summary_file = os.path.join(
        folder_path,
        "summary.json"
    )

    if not os.path.exists(summary_file):
        continue

    with open(summary_file) as f:
        summary = json.load(f)

    topics = summary.get("topics", [])

    category = "Other"

    for topic in topics:

        topic = topic.lower()

        if "competitive" in topic:
            category = "Competitive Analysis"

        elif "product" in topic:
            category = "Product Gaps"

        elif "pricing" in topic:
            category = "Pricing"

        elif "roadmap" in topic:
            category = "Roadmap"

    results.append(
        [folder, category]
    )

df = pd.DataFrame(
    results,
    columns=["MeetingID", "Category"]
)

df.to_csv(
    "output/topic_categories.csv",
    index=False
)

print("Topic categorization completed")