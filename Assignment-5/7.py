# Prompt: Write a menu-driven program to implement the stack data structure

stack = []

while True:
    print("\n***** Stack Menu *****")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        item = input("Enter item to push: ")
        stack.append(item)
        print(f"Item '{item}' pushed onto stack.")

    elif choice == 2:
        if not stack:
            print("Stack is empty. Cannot pop.")
        else:
            popped = stack.pop()
            print(f"Popped item: {popped}")

    elif choice == 3:
        if not stack:
            print("Stack is empty.")
        else:
            print("Current Stack (Top to Bottom):")
            for item in reversed(stack):
                print(item)

    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1-4.")
