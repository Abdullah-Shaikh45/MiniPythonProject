# Tasks List
tasks = [
    {"task": "Learn Flutter", "completed": False},
    {"task": "Drink", "completed": True},
]

# Add Task Function


def add_task():
    task_name = input("\nEnter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print("-" * 40)
    print(f"Task: '{task_name}' added successfully!")
    print("-" * 40)

# View Task Function


def view_task():
    print("\n" + "=" * 40)
    print("📋 Your To-Do List".center(40))
    print("=" * 40)

    if len(tasks) == 0:
        print("No tasks currently!")
    else:
        print("[✅] = Completed  |  [ ] = Not Completed")
        print("-" * 40)
        for index, task in enumerate(tasks):
            status = "✅" if task["completed"] else "[ ]"
            print(f"{index + 1}. {status:<3} {task['task']}")
        print("-" * 40)

# Update Task Function


def update_task():
    view_task()
    task_number = int(input("\nEnter the task number to update: "))
    index = task_number - 1
    new_task = input("Enter the new task name: ").strip()
    tasks[index]['task'] = new_task
    print("-" * 40)
    print(f"Task {task_number} updated successfully!")
    print("-" * 40)

# Mark As Completed Function


def mark_task_completed():
    view_task()
    task_number = int(
        input("\nEnter the task number you want to mark as completed: "))
    index = task_number - 1

    if not tasks[index]["completed"]:
        tasks[index]["completed"] = True
        print("-" * 40)
        print(f"Task {task_number} marked as completed ✅")
        print("-" * 40)
    else:
        print(f"Task {task_number} is already marked as completed!")

# Delete Task Function


def delete_task():
    view_task()
    task_number = int(input("\nEnter the task number: "))
    index = task_number - 1
    deleted_task = tasks.pop(index)
    print("-" * 40)
    print(f"Task '{deleted_task['task']}' has been deleted.")
    print("-" * 40)

# Toggle Task Completion Function


def toggle_task_completed():
    view_task()
    task_number = int(
        input("\nEnter the task number to toggle completion status: "))
    index = task_number - 1

    tasks[index]["completed"] = not tasks[index]["completed"]
    status = "completed" if tasks[index]["completed"] else "not completed"
    print("-" * 40)
    print(f"Task {task_number} is now {status}.")
    print("-" * 40)

# Menu function


def menu():
    print("=" * 40)
    print("📋 Welcome to the Task Manager 📋".center(40))
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task Completed")
    print("5. Delete Task")
    print("6. Toggle Task Completion")
    print("7. Exit")
    print("=" * 40)

# Main function using match-case


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                add_task()
            case "2":
                view_task()
            case "3":
                update_task()
            case "4":
                mark_task_completed()
            case "5":
                delete_task()
            case "6":
                toggle_task_completed()
            case "7":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice, please try again.")


# Run the main function
main()
