import glob
import csv
import os

# Specify the folder containing your txt files
folder_path = "C:/CVSF/Assignment_3/Datasets/OIDv4_ToolKit/OID/Dataset/train/Person_Dog_Cat/Label"  # <-- Change this to your folder path

# Use glob to get a list of all txt files in the folder
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
print(txt_files)
# Open a new CSV file to write the merged data
with open("merged_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Optionally, write a header row (adjust the column names as needed)
    csvwriter.writerow(["filename", "label", "x_min", "y_min", "x_max", "y_max"])
    
    # Process each txt file
    for file in txt_files:
        # Get the file's basename (e.g., "0a004033162a8e8d.txt")
        base_name = os.path.basename(file)
        
        # Open and read the file
        with open(file, "r") as f:
            # Read all lines from the file (in case there are multiple annotations per file)
            lines = f.readlines()

            print(lines)
            for line in lines:
                # Remove any leading/trailing whitespace and split the line by spaces
                parts = line.strip().split()
                print(parts)
                if parts:
                    # Assume the first part is the label and the rest are coordinates
                    label = parts[0]
                    coordinates = parts[1:]
                    # Write the filename, label, and coordinates to the CSV file
                    csvwriter.writerow([base_name, label] + coordinates)

print("Merged CSV created successfully!")
