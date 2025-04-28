def get_integer_input():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter an integer: ")

            # Try to convert the input to an integer
            num = int(user_input)

            # If successful, return the integer
            return num
        except ValueError:
            # If there's a ValueError, it means the input wasn't an integer
            print("Error: That is not a valid integer. Please try again.")


# Example usage:
result = get_integer_input()
print(f"You entered the integer: {result}")
