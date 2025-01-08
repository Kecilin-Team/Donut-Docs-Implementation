import json

# Input and output file paths
input_file_path = "data_rank/train/metadata.jsonl"
output_file_path = "data_rank/train/labels.json"

# Read the JSONL file and parse each line
data = []
with open(input_file_path, "r", encoding="utf-8") as infile:
    for line in infile:
        # Parse each line as a JSON object and append to the list
        data.append(json.loads(line))

# Write the list as a JSON array to the output file
with open(output_file_path, "w", encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(f"Converted JSONL file to JSON format and saved to {output_file_path}")