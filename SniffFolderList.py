import os

# Define the target folder path
folder_path = r"F:\VintageWebsite\assets\images\websites"  # Update this path

# Define the output text file
output_file = r"F:\VintageWebsite\assets\images\websites\file_list.txt"  # Update as needed

# Get list of files in the folder
file_list = os.listdir(folder_path)

# Write file names and extensions to the text file
with open(output_file, "w") as f:
    for file in file_list:
        file_name, file_extension = os.path.splitext(file)
        f.write(f"{file_name}{file_extension}\n")

print(f"File list saved to {output_file}")
