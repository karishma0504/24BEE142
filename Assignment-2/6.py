# Prompt: Accept a number from the user and print number of digits in it

num = int(input("Enter a number: "))
count = len(str(abs(num)))

print(f"The number of digits in {num} is {count}")
