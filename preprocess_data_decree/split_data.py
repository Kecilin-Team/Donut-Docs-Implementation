import os
import shutil
import jsonlines
import random

# Path to the folder containing images and JSONL file
image_folder = "DecreeImages"  
json_file = "DecreeData.jsonl"  

# Read JSONL file containing labels
labels = []
with jsonlines.open(json_file, 'r') as reader:
    for obj in reader:
        labels.append(obj)

# Get a list of all images in a folder from the "file_name" field
image_files = [os.path.basename(item["file_name"]) for item in labels]

# Shuffle image list to randomly split
random.shuffle(image_files)

# train:valid:test = 8:1:1
train_size = int(0.8 * len(image_files))
valid_size = int(0.1 * len(image_files))

# Split data into 3 parts
train_images = image_files[:train_size]
valid_images = image_files[train_size:train_size + valid_size]
test_images = image_files[train_size + valid_size:]

# Create folder: train, valid, test
output_folders = ["train", "valid", "test"]
for folder in output_folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Move images to corresponding folders
def move_images(image_list, folder):
    for image in image_list:
        image_path = os.path.join(image_folder, image)
        if os.path.isfile(image_path):
            shutil.copy(image_path, os.path.join(folder, image))

move_images(train_images, "train")
move_images(valid_images, "valid")
move_images(test_images, "test")

# Make sure to duplicate labels for each dataset
train_labels = [label for label in labels if os.path.basename(label['file_name']) in train_images]
valid_labels = [label for label in labels if os.path.basename(label['file_name']) in valid_images]
test_labels = [label for label in labels if os.path.basename(label['file_name']) in test_images]

# Save labels to JSONL files in each folder
def save_labels(labels, folder):
    output_json = os.path.join(folder, "metadata.jsonl")
    with jsonlines.open(output_json, mode='w') as writer:
        writer.write_all(labels)

save_labels(train_labels, "train")
save_labels(valid_labels, "valid")
save_labels(test_labels, "test")

print("Data has been successfully split into train, valid, and test folders.")
