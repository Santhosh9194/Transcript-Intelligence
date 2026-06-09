import os

DATASET_PATH = "dataset"

meeting_count = 0

for folder in os.listdir(DATASET_PATH):

    folder_path = os.path.join(DATASET_PATH, folder)

    if os.path.isdir(folder_path):
        meeting_count += 1

print(f"Total meetings found: {meeting_count}")