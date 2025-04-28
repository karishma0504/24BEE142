def merge_alternate_lines(file1, file2, target_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        max_lines = max(len(lines1), len(lines2))

        with open(target_file, 'w') as output_file:
            for i in range(max_lines):
                if i < len(lines1):
                    output_file.write(lines1[i])
                if i < len(lines2):
                    output_file.write(lines2[i])

        print(f"Lines have been merged into '{target_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: One or more source files were not found.")
    except Exception as e:
        print(f"Error: {e}")


file1 = input("Enter the path of the first file: ")
file2 = input("Enter the path of the second file: ")
target_file = input("Enter the path of the target file: ")

merge_alternate_lines(file1, file2, target_file)
