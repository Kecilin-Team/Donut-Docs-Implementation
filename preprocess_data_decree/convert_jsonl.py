import json


json_file = "DecreeData.json"
with open(json_file, 'r') as f:
    data = json.load(f)

# file JSONL
output_file = "DecreeData.jsonl"  


with open(output_file, 'w') as outfile:
    for item in data:
        if "bbox" in item:
            del item["bbox"]
        # get name file images
        file_name = item["ocr"].split("/")[-1]

        gt_parse = {}

        try:
            for i in range(len(item['transcription'])):
                label_name = item['label'][i]['labels']

                if label_name[0] == "Document Title":
                    if "Document_Title" not in gt_parse: 
                        gt_parse["Document_Title"] = []
                    gt_parse["Document_Title"].append(item['transcription'][i])
                    
                if label_name[0] == "Name":
                    if "Name" not in gt_parse: 
                        gt_parse["Name"] = []
                    gt_parse["Name"].append(item['transcription'][i])
                    
                if label_name[0] == "Previous Position":
                    if "Previous_Position" not in gt_parse: 
                        gt_parse["Previous_Position"] = []
                    gt_parse["Previous_Position"].append(item['transcription'][i])

                if label_name[0] == "New Position":
                    if "New_Position" not in gt_parse: 
                        gt_parse["New_Position"] = []
                    gt_parse["New_Position"].append(item['transcription'][i])
                
                if label_name[0] == "Date Appointed to New Position":
                    if "Date_Appointed_to_New_Position" not in gt_parse: 
                        gt_parse["Date_Appointed_to_New_Position"] = []
                    gt_parse["Date_Appointed_to_New_Position"].append(item['transcription'][i])
                   
            for key in gt_parse:
                gt_parse[key] = " ".join(gt_parse[key])
        # Create object JSON for each line
            output_data = {
                "file_name": file_name,
                "ground_truth": json.dumps({"gt_parse": gt_parse}) 
            }

        # Write object to file JSONL
            outfile.write(json.dumps(output_data) + "\n")
        except Exception as e:
            print(e)
            print(file_name)
print(f"File JSONL saved: {output_file}")
