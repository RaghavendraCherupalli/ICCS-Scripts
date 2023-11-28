import os

def change_file_names(folder_path):
    # Get a list of all files in the folder

    files = os.listdir(folder_path)

    # Iterate through each file in the folder
    for old_name in files:
        # Construct the full path for the old and new file names
        old_path = os.path.join(folder_path, old_name)
        cur_name=old_name.replace(' ','')
        new_name = f"{cur_name}"
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {old_path} -> {new_path}")

# Example usage: Change all file names in the "example_folder" with a prefix "new_prefix"




change_file_names(os.getcwd())


# Change to the parent directory
