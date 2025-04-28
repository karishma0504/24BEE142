import os
import shutil

# Function to create a subdirectory and copy a file
def create_and_copy_file(source_file, target_dir):
    # Create the target subdirectory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Subdirectory '{target_dir}' created successfully.")
    else:
        print(f"Subdirectory '{target_dir}' already exists.")

    # Define the target file path
    target_file = os.path.join(target_dir, os.path.basename(source_file))

    # Copy the file from source to target subdirectory
    try:
        shutil.copy(source_file, target_file)
        print(f"File '{source_file}' has been copied to '{target_file}'")
    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Accept user input for file and directories
source_file = input("Enter the full path of the file to copy: ")
target_dir = input("Enter the path of the subdirectory to create or use for the file: ")

# Call the function to create the subdirectory and copy the file
create_and_copy_file(source_file, target_dir)
