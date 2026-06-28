import os
import shutil
import random

dataset_dir = "Fish dataset"
output_dir = "fish_dataset"

train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

os.makedirs(output_dir, exist_ok=True)

for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

for class_name in os.listdir(dataset_dir):

    class_path = os.path.join(dataset_dir, class_name)

    # Skip hidden files like .DS_Store
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    train_split = int(len(images) * train_ratio)
    val_split = int(len(images) * (train_ratio + val_ratio))

    splits = {
        "train": images[:train_split],
        "val": images[train_split:val_split],
        "test": images[val_split:]
    }

    for split, files in splits.items():

        split_class_dir = os.path.join(output_dir, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)

        for file in files:
            src = os.path.join(class_path, file)
            dst = os.path.join(split_class_dir, file)
            shutil.copy(src, dst)

print("Dataset split completed successfully!")