# Step 1: Define a Task class
class Task:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Task ID: {self.id}, Name: {self.name}, Description: {self.description}"

# In-memory list to store tasks
tasks = []
next_id = 1

# Step 2: Implement functionality to create a new task
def create_task():
    global next_id
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    task = Task(next_id, name, description)
    tasks.append(task)
    print(f"Task created with ID {next_id}")
    next_id += 1

# Step 3: Develop a method to read and display tasks
def read_tasks():
    if tasks:
        print("\nList of tasks:")
        for task in tasks:
            print(task)
    else:
        print("\nNo tasks available.")

# Step 4: Allow users to update task details
def update_task():
    task_id = int(input("Enter the task ID to update: "))
    for task in tasks:
        if task.id == task_id:
            task.name = input("Enter new task name: ")
            task.description = input("Enter new task description: ")
            print(f"Task ID {task_id} updated.")
            return
    print(f"Task ID {task_id} not found.")

# Step 5: Provide an option to delete tasks
def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task ID {task_id} deleted.")

# Main loop to interact with the user
def main():
    while True:
        print("\nTask Manager:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Step 6: Test the application with various scenarios
if __name__ == "__main__":
    main()
