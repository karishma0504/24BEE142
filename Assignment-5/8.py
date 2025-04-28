# Prompt: Write a menu-driven program to implement the Queue data structure

queue = []

while True:
    print("\n***** Queue Menu *****")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        item = input("Enter item to enqueue: ")
        queue.append(item)
        print(f"Item '{item}' added to the queue.")

    elif choice == 2:
        if not queue:
            print("Queue is empty. Cannot dequeue.")
        else:
            dequeued = queue.pop(0)
            print(f"Dequeued item: {dequeued}")

    elif choice == 3:
        if not queue:
            print("Queue is empty.")
        else:
            print("Current Queue (Front to Rear):")
            for item in queue:
                print(item)

    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1-4.")
