def remove_words(input_file, output_file):
    words_to_remove = ['a', 'the', 'an']

    try:
        # Open the input file to read
        with open(input_file, 'r') as file:
            content = file.read()

        # Replace specified words with a blank space
        for word in words_to_remove:
            content = content.replace(f" {word} ", " ")
            content = content.replace(f" {word}.", " .")  # handle word at the end of a sentence
            content = content.replace(f" {word},", " ,")  # handle word with commas

        # Write the modified content to the output file
        with open(output_file, 'w') as output:
            output.write(content)

        print(f"File processed and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
input_filename = input("Enter the path of the input text file: ")
output_filename = input("Enter the path of the output text file: ")

remove_words(input_filename, output_filename)
