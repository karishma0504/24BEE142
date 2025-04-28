def copy_and_convert_case(source_file, target_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src_file:
            # Read all content from the source file
            content = src_file.read()

        # Convert the content to uppercase
        modified_content = content.upper()

        # Open the target file in write mode and write the modified content
        with open(target_file, 'w') as dest_file:
            dest_file.write(modified_content)

        print(
            f"Contents of '{source_file}' have been copied to '{target_file}' with lowercase characters converted to uppercase.")

    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    except Exception as e:
        print(f"Error: {e}")


# Accept user input for source and target files
source_file = input("Enter the path of the source file: ")
target_file = input("Enter the path of the target file: ")

# Call the function to copy and convert the case
copy_and_convert_case(source_file, target_file)
