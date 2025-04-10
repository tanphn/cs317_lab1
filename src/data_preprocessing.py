import os
import shutil
from pathlib import Path
import json

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

def preprocess():
    if (PROCESSED_DIR / "train").exists():
        print("Processed data already exists. Skipping preprocessing.")
        return

    shutil.rmtree(PROCESSED_DIR, ignore_errors=True)
    os.makedirs(PROCESSED_DIR / "train", exist_ok=True)
    os.makedirs(PROCESSED_DIR / "val", exist_ok=True)

    # Giả lập chia 80-20
    for class_dir in RAW_DIR.iterdir():
        if class_dir.is_dir():
            images = list(class_dir.glob("*.jpg"))
            split_idx = int(0.8 * len(images))
            train_imgs, val_imgs = images[:split_idx], images[split_idx:]

            train_class_dir = PROCESSED_DIR / "train" / class_dir.name
            val_class_dir = PROCESSED_DIR / "val" / class_dir.name
            os.makedirs(train_class_dir, exist_ok=True)
            os.makedirs(val_class_dir, exist_ok=True)

            for img in train_imgs:
                shutil.copy(img, train_class_dir / img.name)
            for img in val_imgs:
                shutil.copy(img, val_class_dir / img.name)

    # Ghi log JSON
    with open("metrics/preprocessing.json", "w") as f:
        json.dump({"status": "done"}, f)

if __name__ == "__main__":
    preprocess()
